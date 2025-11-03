# Birth Chart Calculator

Aplicativo para cálculos precisos de mapa natal com geração de imagem e interpretação profissional.

## Características

- Cálculos astronômicos extremamente precisos usando Swiss Ephemeris
- Geração de imagem visual do mapa natal
- Lista completa de posições planetárias
- Resumo inicial de 5 linhas
- Interpretação completa profissional em linguagem natural (sob demanda)

## Instalação

```bash
pip install -r requirements.txt
```

## Uso

```python
from birth_chart import BirthChart

# Criar mapa natal
chart = BirthChart(
    date="1990-01-15",
    time="14:30",
    location="São Paulo, Brazil"
)

# Gerar imagem
chart.generate_image("mapa.png")

# Obter resumo
print(chart.get_summary())

# Obter interpretação completa
print(chart.get_full_interpretation())
```
