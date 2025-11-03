"""
Módulo de cálculos astronômicos precisos usando Swiss Ephemeris
"""

import swisseph as swe
from datetime import datetime
from dateutil import parser
import pytz
from geopy.geocoders import Nominatim
from typing import Dict, List, Tuple, Optional
import math

from .data import SIGNS, PLANETS, ASPECTS


class BirthChart:
    """Classe principal para cálculo de mapa natal"""

    def __init__(self, date: str, time: str, location: str, house_system: str = 'P'):
        """
        Inicializa o mapa natal

        Args:
            date: Data de nascimento (formato: YYYY-MM-DD ou DD/MM/YYYY)
            time: Hora de nascimento (formato: HH:MM ou HH:MM:SS)
            location: Local de nascimento (cidade, país)
            house_system: Sistema de casas (padrão: 'P' - Placidus)
        """
        self.date_str = date
        self.time_str = time
        self.location_str = location
        self.house_system = house_system

        # Parse da data e hora
        self._parse_datetime()

        # Obter coordenadas do local
        self._get_coordinates()

        # Calcular posições planetárias
        self.planets = self._calculate_planets()

        # Calcular casas
        self.houses = self._calculate_houses()

        # Calcular aspectos
        self.aspects = self._calculate_aspects()

    def _parse_datetime(self):
        """Parse da data e hora de nascimento"""
        # Tentar diferentes formatos de data
        try:
            if '/' in self.date_str:
                dt = datetime.strptime(self.date_str, "%d/%m/%Y")
            else:
                dt = datetime.strptime(self.date_str, "%Y-%m-%d")
        except:
            dt = parser.parse(self.date_str)

        # Parse da hora
        try:
            time_parts = self.time_str.split(':')
            hour = int(time_parts[0])
            minute = int(time_parts[1])
            second = int(time_parts[2]) if len(time_parts) > 2 else 0
        except:
            hour, minute, second = 12, 0, 0

        self.birth_datetime = dt.replace(hour=hour, minute=minute, second=second)

    def _get_coordinates(self):
        """Obtém coordenadas geográficas do local de nascimento"""
        try:
            geolocator = Nominatim(user_agent="birth_chart_calculator")
            location = geolocator.geocode(self.location_str)

            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
            else:
                # Coordenadas padrão (São Paulo) se não encontrar
                self.latitude = -23.5505
                self.longitude = -46.6333
        except:
            # Coordenadas padrão (São Paulo) em caso de erro
            self.latitude = -23.5505
            self.longitude = -46.6333

    def _get_julian_day(self) -> float:
        """Calcula o dia juliano para a data/hora de nascimento"""
        year = self.birth_datetime.year
        month = self.birth_datetime.month
        day = self.birth_datetime.day
        hour = self.birth_datetime.hour + self.birth_datetime.minute / 60.0 + self.birth_datetime.second / 3600.0

        jd = swe.julday(year, month, day, hour)
        return jd

    def _calculate_planets(self) -> Dict:
        """Calcula posições de todos os planetas"""
        jd = self._get_julian_day()
        planets_data = {}

        # Planetas principais (0-9: Sol a Plutão)
        planet_ids = list(range(10))

        # Adicionar Nodo Norte (10) e Quiron (15)
        planet_ids.extend([swe.MEAN_NODE, swe.CHIRON])

        for i, planet_id in enumerate(planet_ids):
            if i < 10:
                actual_id = planet_id
                data_key = planet_id
            elif planet_id == swe.MEAN_NODE:
                actual_id = planet_id
                data_key = 10
            else:  # Quiron
                actual_id = planet_id
                data_key = 11

            # Calcular posição
            result = swe.calc_ut(jd, actual_id)
            position = result[0][0]  # Longitude eclíptica
            speed = result[0][3]     # Velocidade

            # Determinar signo e grau
            sign_num = int(position / 30)
            degree = position % 30

            planets_data[data_key] = {
                "name": PLANETS[data_key]["name"],
                "symbol": PLANETS[data_key]["symbol"],
                "position": position,
                "sign": SIGNS[sign_num],
                "degree": degree,
                "degree_int": int(degree),
                "minute": int((degree % 1) * 60),
                "speed": speed,
                "retrograde": speed < 0
            }

        return planets_data

    def _calculate_houses(self) -> Dict:
        """Calcula cúspides das casas astrológicas"""
        jd = self._get_julian_day()

        # Calcular casas usando o sistema especificado
        houses_cusps, ascmc = swe.houses(jd, self.latitude, self.longitude, self.house_system.encode())

        houses_data = {
            "ascendant": {
                "position": ascmc[0],
                "sign": SIGNS[int(ascmc[0] / 30)],
                "degree": ascmc[0] % 30
            },
            "mc": {
                "position": ascmc[1],
                "sign": SIGNS[int(ascmc[1] / 30)],
                "degree": ascmc[1] % 30
            },
            "cusps": []
        }

        # Processar cúspides das 12 casas
        for i, cusp in enumerate(houses_cusps[:12], 1):
            houses_data["cusps"].append({
                "house": i,
                "position": cusp,
                "sign": SIGNS[int(cusp / 30)],
                "degree": cusp % 30
            })

        return houses_data

    def _calculate_aspects(self) -> List[Dict]:
        """Calcula aspectos entre planetas"""
        aspects_list = []
        planet_keys = list(self.planets.keys())

        # Comparar cada par de planetas
        for i, p1_key in enumerate(planet_keys):
            for p2_key in planet_keys[i+1:]:
                p1 = self.planets[p1_key]
                p2 = self.planets[p2_key]

                # Calcular diferença angular
                diff = abs(p1["position"] - p2["position"])
                if diff > 180:
                    diff = 360 - diff

                # Verificar cada tipo de aspecto
                for aspect_type, aspect_data in ASPECTS.items():
                    angle = aspect_data["angle"]
                    orb = aspect_data["orb"]

                    if abs(diff - angle) <= orb:
                        aspects_list.append({
                            "planet1": p1["name"],
                            "planet2": p2["name"],
                            "type": aspect_data["name"],
                            "symbol": aspect_data["symbol"],
                            "angle": angle,
                            "orb": abs(diff - angle),
                            "exact": abs(diff - angle) < 1
                        })
                        break

        return aspects_list

    def get_planet_list(self) -> str:
        """Retorna lista formatada de posições planetárias"""
        output = "=" * 60 + "\n"
        output += "POSIÇÕES PLANETÁRIAS\n"
        output += "=" * 60 + "\n\n"

        for key, planet in self.planets.items():
            retro = " (R)" if planet["retrograde"] else ""
            output += f"{planet['symbol']} {planet['name']:12} {planet['degree_int']:2}°{planet['minute']:02}' {planet['sign']:12}{retro}\n"

        output += "\n" + "=" * 60 + "\n"
        output += "CASAS\n"
        output += "=" * 60 + "\n\n"

        # Ascendente e MC
        asc = self.houses["ascendant"]
        mc = self.houses["mc"]
        output += f"Ascendente:  {int(asc['degree']):2}°{int((asc['degree'] % 1) * 60):02}' {asc['sign']}\n"
        output += f"Meio do Céu: {int(mc['degree']):2}°{int((mc['degree'] % 1) * 60):02}' {mc['sign']}\n\n"

        # Cúspides das casas
        for cusp in self.houses["cusps"]:
            output += f"Casa {cusp['house']:2}:  {int(cusp['degree']):2}°{int((cusp['degree'] % 1) * 60):02}' {cusp['sign']}\n"

        return output

    def get_summary(self) -> str:
        """Retorna resumo de 5 linhas do mapa natal"""
        sol = self.planets[0]
        lua = self.planets[1]
        asc = self.houses["ascendant"]

        # Contar elementos e modalidades
        elements = {"Fogo": 0, "Terra": 0, "Ar": 0, "Água": 0}

        for planet in self.planets.values():
            sign = planet["sign"]
            if sign in ["Áries", "Leão", "Sagitário"]:
                elements["Fogo"] += 1
            elif sign in ["Touro", "Virgem", "Capricórnio"]:
                elements["Terra"] += 1
            elif sign in ["Gêmeos", "Libra", "Aquário"]:
                elements["Ar"] += 1
            elif sign in ["Câncer", "Escorpião", "Peixes"]:
                elements["Água"] += 1

        dominant_element = max(elements, key=elements.get)

        # Aspectos importantes
        major_aspects = [a for a in self.aspects if a["type"] in ["Conjunção", "Oposição", "Trígono", "Quadratura"]]

        summary = f"""RESUMO DO MAPA NATAL

Sol em {sol['sign']}, Lua em {lua['sign']}, Ascendente em {asc['sign']}. Elemento dominante: {dominant_element} com {elements[dominant_element]} planetas.
A combinação de Sol em {sol['sign']} com Ascendente em {asc['sign']} indica uma pessoa que {'busca estabilidade' if dominant_element == 'Terra' else 'busca movimento' if dominant_element == 'Fogo' else 'busca conexões' if dominant_element == 'Ar' else 'busca profundidade'}.
Lua em {lua['sign']} revela necessidades emocionais {'práticas e concretas' if lua['sign'] in ['Touro', 'Virgem', 'Capricórnio'] else 'intensas e profundas' if lua['sign'] in ['Câncer', 'Escorpião', 'Peixes'] else 'dinâmicas e expansivas' if lua['sign'] in ['Áries', 'Leão', 'Sagitário'] else 'intelectuais e sociais'}.
{len(major_aspects)} aspectos principais modelam a dinâmica entre as diferentes partes da personalidade.
Este mapa sugere {'desafios importantes de integração' if any(a['type'] == 'Quadratura' for a in major_aspects[:3]) else 'fluidez natural entre as energias'} que {'exigem trabalho consciente' if elements[dominant_element] > 6 else 'podem se desenvolver organicamente'}.
"""
        return summary

    def generate_image(self, filename: str):
        """Gera imagem do mapa natal"""
        from .chart_image import ChartImageGenerator
        generator = ChartImageGenerator(self)
        generator.generate(filename)

    def get_full_interpretation(self) -> str:
        """Retorna interpretação completa e profissional do mapa"""
        from .interpreter import ChartInterpreter
        interpreter = ChartInterpreter(self)
        return interpreter.generate_full_interpretation()
