#!/usr/bin/env python3
"""
Testes básicos do Birth Chart Calculator
Execute: python test_basic.py
"""

from birth_chart import BirthChart
import os


def test_create_chart():
    """Teste 1: Criar um mapa natal básico"""
    print("Teste 1: Criar mapa natal... ", end="")

    try:
        chart = BirthChart(
            date="15/01/1990",
            time="14:30",
            location="São Paulo, Brazil"
        )

        assert chart is not None
        assert chart.planets is not None
        assert len(chart.planets) > 0
        assert chart.houses is not None

        print("✅ PASSOU")
        return True
    except Exception as e:
        print(f"❌ FALHOU: {e}")
        return False


def test_planet_positions():
    """Teste 2: Verificar posições planetárias"""
    print("Teste 2: Verificar posições planetárias... ", end="")

    try:
        chart = BirthChart(
            date="2000-01-01",
            time="00:00",
            location="Rio de Janeiro, Brazil"
        )

        # Verificar que temos os planetas principais
        assert 0 in chart.planets  # Sol
        assert 1 in chart.planets  # Lua
        assert 2 in chart.planets  # Mercúrio

        # Verificar que cada planeta tem os dados necessários
        sol = chart.planets[0]
        assert "name" in sol
        assert "sign" in sol
        assert "position" in sol
        assert "degree" in sol

        # Verificar que a posição está no range válido (0-360)
        assert 0 <= sol["position"] < 360

        print("✅ PASSOU")
        return True
    except Exception as e:
        print(f"❌ FALHOU: {e}")
        return False


def test_houses():
    """Teste 3: Verificar cálculo de casas"""
    print("Teste 3: Verificar cálculo de casas... ", end="")

    try:
        chart = BirthChart(
            date="1995-06-15",
            time="18:00",
            location="Brasília, Brazil"
        )

        # Verificar que temos ascendente e MC
        assert "ascendant" in chart.houses
        assert "mc" in chart.houses

        # Verificar que temos 12 cúspides
        assert len(chart.houses["cusps"]) == 12

        # Verificar que cada cúspide tem os dados necessários
        cusp = chart.houses["cusps"][0]
        assert "house" in cusp
        assert "position" in cusp
        assert "sign" in cusp

        print("✅ PASSOU")
        return True
    except Exception as e:
        print(f"❌ FALHOU: {e}")
        return False


def test_aspects():
    """Teste 4: Verificar cálculo de aspectos"""
    print("Teste 4: Verificar cálculo de aspectos... ", end="")

    try:
        chart = BirthChart(
            date="1988-03-20",
            time="12:00",
            location="Salvador, Brazil"
        )

        # Verificar que temos aspectos
        assert chart.aspects is not None
        assert isinstance(chart.aspects, list)

        # Se houver aspectos, verificar estrutura
        if len(chart.aspects) > 0:
            aspect = chart.aspects[0]
            assert "planet1" in aspect
            assert "planet2" in aspect
            assert "type" in aspect
            assert "angle" in aspect

        print("✅ PASSOU")
        return True
    except Exception as e:
        print(f"❌ FALHOU: {e}")
        return False


def test_get_summary():
    """Teste 5: Verificar geração de resumo"""
    print("Teste 5: Verificar geração de resumo... ", end="")

    try:
        chart = BirthChart(
            date="1992-11-10",
            time="08:30",
            location="Porto Alegre, Brazil"
        )

        summary = chart.get_summary()

        assert summary is not None
        assert isinstance(summary, str)
        assert len(summary) > 100  # Resumo deve ter conteúdo

        # Verificar que menciona signos principais
        sol_sign = chart.planets[0]["sign"]
        assert sol_sign in summary

        print("✅ PASSOU")
        return True
    except Exception as e:
        print(f"❌ FALHOU: {e}")
        return False


def test_get_planet_list():
    """Teste 6: Verificar lista de planetas"""
    print("Teste 6: Verificar lista de planetas... ", end="")

    try:
        chart = BirthChart(
            date="1985-07-04",
            time="15:45",
            location="Recife, Brazil"
        )

        planet_list = chart.get_planet_list()

        assert planet_list is not None
        assert isinstance(planet_list, str)
        assert len(planet_list) > 100

        # Verificar que menciona alguns planetas
        assert "Sol" in planet_list or "☉" in planet_list
        assert "Lua" in planet_list or "☽" in planet_list

        print("✅ PASSOU")
        return True
    except Exception as e:
        print(f"❌ FALHOU: {e}")
        return False


def test_generate_image():
    """Teste 7: Verificar geração de imagem"""
    print("Teste 7: Verificar geração de imagem... ", end="")

    try:
        chart = BirthChart(
            date="1990-12-25",
            time="20:00",
            location="Curitiba, Brazil"
        )

        test_filename = "test_chart.png"

        # Remover arquivo se já existe
        if os.path.exists(test_filename):
            os.remove(test_filename)

        # Gerar imagem
        chart.generate_image(test_filename)

        # Verificar que arquivo foi criado
        assert os.path.exists(test_filename)

        # Verificar que arquivo tem tamanho razoável (> 1KB)
        file_size = os.path.getsize(test_filename)
        assert file_size > 1000

        # Limpar arquivo de teste
        os.remove(test_filename)

        print("✅ PASSOU")
        return True
    except Exception as e:
        print(f"❌ FALHOU: {e}")
        # Tentar limpar arquivo de teste
        if os.path.exists("test_chart.png"):
            os.remove("test_chart.png")
        return False


def run_all_tests():
    """Executar todos os testes"""
    print("\n" + "="*80)
    print("EXECUTANDO TESTES DO BIRTH CHART CALCULATOR")
    print("="*80 + "\n")

    tests = [
        test_create_chart,
        test_planet_positions,
        test_houses,
        test_aspects,
        test_get_summary,
        test_get_planet_list,
        test_generate_image,
    ]

    results = []
    for test in tests:
        results.append(test())

    # Resumo
    print("\n" + "="*80)
    print("RESUMO DOS TESTES")
    print("="*80)
    print(f"\nTotal de testes: {len(results)}")
    print(f"Passou: {sum(results)}")
    print(f"Falhou: {len(results) - sum(results)}")

    if all(results):
        print("\n✅ TODOS OS TESTES PASSARAM!\n")
    else:
        print("\n❌ ALGUNS TESTES FALHARAM\n")

    return all(results)


if __name__ == "__main__":
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)
