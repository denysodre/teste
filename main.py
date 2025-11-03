#!/usr/bin/env python3
"""
Birth Chart Calculator - Interface principal
Uso: python main.py
"""

from birth_chart import BirthChart
import sys


def print_separator():
    print("\n" + "="*80 + "\n")


def main():
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║              CALCULADORA DE MAPA NATAL - CÁLCULOS PRECISOS                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

    # Entrada de dados
    print("Digite os dados de nascimento:\n")

    data = input("Data de nascimento (DD/MM/YYYY ou YYYY-MM-DD): ").strip()
    if not data:
        data = "15/01/1990"  # Exemplo padrão

    hora = input("Hora de nascimento (HH:MM): ").strip()
    if not hora:
        hora = "14:30"  # Exemplo padrão

    local = input("Local de nascimento (Cidade, País): ").strip()
    if not local:
        local = "São Paulo, Brazil"  # Exemplo padrão

    print("\n🔄 Calculando posições planetárias...")
    print("   (Usando Swiss Ephemeris para precisão astronômica)\n")

    try:
        # Criar mapa natal
        chart = BirthChart(
            date=data,
            time=hora,
            location=local
        )

        print("✅ Mapa calculado com sucesso!")

        # Menu de opções
        while True:
            print_separator()
            print("O que você gostaria de ver?")
            print()
            print("1 - Lista de posições planetárias")
            print("2 - Resumo de 5 linhas do mapa")
            print("3 - Gerar imagem do mapa natal")
            print("4 - Interpretação completa profissional")
            print("5 - Ver tudo (lista + resumo + gerar imagem)")
            print("0 - Sair")
            print()

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                print_separator()
                print(chart.get_planet_list())

            elif opcao == "2":
                print_separator()
                print(chart.get_summary())

            elif opcao == "3":
                filename = input("\nNome do arquivo de imagem (ex: mapa.png): ").strip()
                if not filename:
                    filename = "mapa_natal.png"

                if not filename.endswith('.png'):
                    filename += '.png'

                print(f"\n🎨 Gerando imagem do mapa natal...")
                chart.generate_image(filename)
                print(f"✅ Imagem salva em: {filename}")

            elif opcao == "4":
                print_separator()
                print("📖 Gerando interpretação completa...")
                print("   (Isso pode levar alguns segundos)\n")
                print(chart.get_full_interpretation())

            elif opcao == "5":
                # Mostrar tudo
                print_separator()
                print(chart.get_planet_list())

                print_separator()
                print(chart.get_summary())

                print_separator()
                filename = "mapa_natal.png"
                print(f"🎨 Gerando imagem do mapa natal...")
                chart.generate_image(filename)
                print(f"✅ Imagem salva em: {filename}")

            elif opcao == "0":
                print("\n👋 Até logo!\n")
                break

            else:
                print("\n❌ Opção inválida. Tente novamente.")

    except Exception as e:
        print(f"\n❌ Erro ao calcular mapa natal: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
