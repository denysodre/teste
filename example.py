#!/usr/bin/env python3
"""
Exemplo de uso da API do Birth Chart Calculator
"""

from birth_chart import BirthChart


def example_1():
    """Exemplo básico: criar mapa e ver resumo"""
    print("="*80)
    print("EXEMPLO 1: Uso básico")
    print("="*80)

    chart = BirthChart(
        date="15/01/1990",
        time="14:30",
        location="São Paulo, Brazil"
    )

    print(chart.get_summary())
    print("\n")


def example_2():
    """Exemplo 2: Ver todas as posições planetárias"""
    print("="*80)
    print("EXEMPLO 2: Posições planetárias detalhadas")
    print("="*80)

    chart = BirthChart(
        date="1990-03-21",
        time="08:00",
        location="Rio de Janeiro, Brazil"
    )

    print(chart.get_planet_list())
    print("\n")


def example_3():
    """Exemplo 3: Gerar imagem"""
    print("="*80)
    print("EXEMPLO 3: Gerar imagem do mapa")
    print("="*80)

    chart = BirthChart(
        date="1985-12-10",
        time="18:45",
        location="Brasília, Brazil"
    )

    print("Gerando imagem...")
    chart.generate_image("exemplo_mapa.png")
    print("✅ Imagem salva como: exemplo_mapa.png")
    print("\n")


def example_4():
    """Exemplo 4: Interpretação completa"""
    print("="*80)
    print("EXEMPLO 4: Interpretação completa")
    print("="*80)

    chart = BirthChart(
        date="1992-07-04",
        time="12:00",
        location="Salvador, Brazil"
    )

    print("Gerando interpretação profissional...")
    interpretation = chart.get_full_interpretation()
    print(interpretation)
    print("\n")


def example_5():
    """Exemplo 5: Acessar dados programaticamente"""
    print("="*80)
    print("EXEMPLO 5: Acessar dados do mapa programaticamente")
    print("="*80)

    chart = BirthChart(
        date="2000-01-01",
        time="00:00",
        location="Porto Alegre, Brazil"
    )

    # Acessar planetas
    sol = chart.planets[0]
    lua = chart.planets[1]

    print(f"Sol: {sol['degree_int']}° de {sol['sign']}")
    print(f"Lua: {lua['degree_int']}° de {lua['sign']}")

    # Acessar ascendente
    asc = chart.houses["ascendant"]
    print(f"Ascendente: {int(asc['degree'])}° de {asc['sign']}")

    # Ver aspectos
    print(f"\nTotal de aspectos: {len(chart.aspects)}")

    # Aspectos principais
    major_aspects = [a for a in chart.aspects if a['type'] in ['Conjunção', 'Oposição', 'Trígono', 'Quadratura']]
    print(f"Aspectos principais: {len(major_aspects)}")

    for aspect in major_aspects[:3]:  # Primeiros 3
        print(f"  • {aspect['planet1']} {aspect['symbol']} {aspect['planet2']}")

    print("\n")


if __name__ == "__main__":
    # Executar todos os exemplos
    example_1()
    example_2()
    example_3()
    # example_4()  # Comentado porque gera muito texto
    example_5()

    print("="*80)
    print("Exemplos concluídos!")
    print("="*80)
