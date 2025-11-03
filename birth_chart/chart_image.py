"""
Gerador de imagem visual do mapa natal
"""

from PIL import Image, ImageDraw, ImageFont
import math
from typing import Tuple

from .data import SIGNS, PLANETS


class ChartImageGenerator:
    """Gera visualização gráfica do mapa natal"""

    def __init__(self, birth_chart):
        self.chart = birth_chart
        self.size = 1200
        self.center = self.size // 2
        self.bg_color = "#0a0a0a"
        self.fg_color = "#e8e8e8"
        self.grid_color = "#2a2a2a"

    def generate(self, filename: str):
        """Gera a imagem do mapa natal"""
        # Criar imagem
        img = Image.new('RGB', (self.size, self.size), self.bg_color)
        draw = ImageDraw.Draw(img)

        # Desenhar círculos base
        self._draw_circles(draw)

        # Desenhar signos zodiacais
        self._draw_signs(draw)

        # Desenhar casas
        self._draw_houses(draw)

        # Desenhar aspectos (linhas entre planetas)
        self._draw_aspects(draw)

        # Desenhar planetas
        self._draw_planets(draw)

        # Adicionar informações de texto
        self._draw_info(draw)

        # Salvar imagem
        img.save(filename)

    def _draw_circles(self, draw):
        """Desenha os círculos concêntricos do mapa"""
        radii = [500, 450, 400, 350, 100]

        for i, radius in enumerate(radii):
            color = self.grid_color if i > 0 else self.fg_color
            width = 3 if i == 0 else 1

            draw.ellipse(
                [self.center - radius, self.center - radius,
                 self.center + radius, self.center + radius],
                outline=color,
                width=width
            )

    def _draw_signs(self, draw):
        """Desenha os 12 signos do zodíaco"""
        radius = 475

        for i, sign in enumerate(SIGNS):
            # Ângulo do signo (0° = Áries começa à esquerda, 0°)
            # Ajustar para que Áries comece à esquerda
            angle = math.radians(180 - (i * 30 + 15))

            x = self.center + radius * math.cos(angle)
            y = self.center + radius * math.sin(angle)

            # Desenhar símbolo do signo
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
            except:
                font = ImageFont.load_default()

            # Símbolos dos signos em Unicode
            symbols = ["♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓"]

            draw.text((x, y), symbols[i], fill=self.fg_color, anchor="mm", font=font)

        # Desenhar linhas divisórias dos signos
        for i in range(12):
            angle = math.radians(180 - (i * 30))

            x1 = self.center + 400 * math.cos(angle)
            y1 = self.center + 400 * math.sin(angle)
            x2 = self.center + 500 * math.cos(angle)
            y2 = self.center + 500 * math.sin(angle)

            draw.line([x1, y1, x2, y2], fill=self.grid_color, width=1)

    def _draw_houses(self, draw):
        """Desenha as cúspides das casas"""
        # A primeira casa começa no Ascendente
        asc_position = self.chart.houses["ascendant"]["position"]

        for i, cusp_data in enumerate(self.chart.houses["cusps"], 1):
            # Posição da cúspide
            position = cusp_data["position"]

            # Converter para ângulo na imagem (ajustado para Ascendente)
            # Subtrair posição do ascendente e ajustar
            angle = math.radians(180 - position)

            x1 = self.center + 100 * math.cos(angle)
            y1 = self.center + 100 * math.sin(angle)
            x2 = self.center + 400 * math.cos(angle)
            y2 = self.center + 400 * math.sin(angle)

            # Linha da cúspide
            color = "#4a9eff" if i in [1, 4, 7, 10] else "#2a5a9f"
            width = 2 if i in [1, 10] else 1

            draw.line([x1, y1, x2, y2], fill=color, width=width)

            # Número da casa
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
            except:
                font = ImageFont.load_default()

            # Posicionar número no meio da casa
            next_cusp = self.chart.houses["cusps"][i % 12]["position"]
            mid_angle = math.radians(180 - ((position + next_cusp) / 2 if next_cusp > position else (position + next_cusp + 360) / 2))

            x_num = self.center + 250 * math.cos(mid_angle)
            y_num = self.center + 250 * math.sin(mid_angle)

            draw.text((x_num, y_num), str(i), fill="#4a9eff", anchor="mm", font=font)

    def _draw_planets(self, draw):
        """Desenha os planetas no mapa"""
        try:
            font_symbol = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
            font_degree = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        except:
            font_symbol = ImageFont.load_default()
            font_degree = ImageFont.load_default()

        # Raio onde os planetas serão desenhados
        planet_radius = 425

        # Desenhar cada planeta
        for key, planet in self.chart.planets.items():
            position = planet["position"]
            angle = math.radians(180 - position)

            x = self.center + planet_radius * math.cos(angle)
            y = self.center + planet_radius * math.sin(angle)

            # Cor do planeta
            color = PLANETS[key]["color"]

            # Desenhar símbolo do planeta
            symbol = planet["symbol"]
            draw.text((x, y), symbol, fill=color, anchor="mm", font=font_symbol)

            # Desenhar grau
            degree_text = f"{planet['degree_int']}°"
            draw.text((x, y + 20), degree_text, fill=color, anchor="mm", font=font_degree)

            # Indicador de retrógrado
            if planet.get("retrograde", False):
                draw.text((x + 15, y - 15), "R", fill="#ff4444", anchor="mm", font=font_degree)

    def _draw_aspects(self, draw):
        """Desenha linhas de aspectos entre planetas"""
        aspect_radius = 370

        # Cores dos aspectos
        aspect_colors = {
            "Conjunção": "#ffeb3b",
            "Oposição": "#f44336",
            "Trígono": "#4caf50",
            "Quadratura": "#ff9800",
            "Sextil": "#2196f3",
        }

        for aspect in self.chart.aspects:
            # Apenas aspectos principais
            if aspect["type"] not in aspect_colors:
                continue

            # Encontrar posições dos planetas
            p1_pos = None
            p2_pos = None

            for planet in self.chart.planets.values():
                if planet["name"] == aspect["planet1"]:
                    p1_pos = planet["position"]
                if planet["name"] == aspect["planet2"]:
                    p2_pos = planet["position"]

            if p1_pos is None or p2_pos is None:
                continue

            # Calcular coordenadas
            angle1 = math.radians(180 - p1_pos)
            angle2 = math.radians(180 - p2_pos)

            x1 = self.center + aspect_radius * math.cos(angle1)
            y1 = self.center + aspect_radius * math.sin(angle1)
            x2 = self.center + aspect_radius * math.cos(angle2)
            y2 = self.center + aspect_radius * math.sin(angle2)

            # Desenhar linha do aspecto
            color = aspect_colors[aspect["type"]]
            width = 2 if aspect["exact"] else 1
            alpha = 200 if aspect["exact"] else 100

            # PIL não suporta alpha diretamente em draw.line, então usar cor mais clara
            draw.line([x1, y1, x2, y2], fill=color, width=width)

    def _draw_info(self, draw):
        """Desenha informações textuais no mapa"""
        try:
            font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            font_info = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        except:
            font_title = ImageFont.load_default()
            font_info = ImageFont.load_default()

        # Título
        draw.text((self.center, 30), "MAPA NATAL", fill=self.fg_color, anchor="mm", font=font_title)

        # Informações de data e local
        info_text = f"{self.chart.date_str} às {self.chart.time_str}"
        draw.text((self.center, 60), info_text, fill=self.fg_color, anchor="mm", font=font_info)

        location_text = f"{self.chart.location_str}"
        draw.text((self.center, 85), location_text, fill=self.fg_color, anchor="mm", font=font_info)

        # Informações principais no centro
        sol = self.chart.planets[0]
        lua = self.chart.planets[1]
        asc = self.chart.houses["ascendant"]

        center_info = f"☉ {sol['sign']}  ☽ {lua['sign']}  ASC {asc['sign']}"
        draw.text((self.center, self.center), center_info, fill=self.fg_color, anchor="mm", font=font_info)
