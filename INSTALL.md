# Guia de Instalação - Birth Chart Calculator

## Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- Conexão com internet (para geocodificação de locais)

## Instalação

### 1. Clone ou baixe o repositório

```bash
git clone <url-do-repositorio>
cd teste
```

### 2. (Opcional mas recomendado) Crie um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/Mac
# ou
venv\Scripts\activate  # No Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Teste a instalação

```bash
python test_basic.py
```

Se todos os testes passarem, a instalação foi bem-sucedida!

## Uso Rápido

### Interface Interativa

```bash
python main.py
```

Siga as instruções na tela para inserir data, hora e local de nascimento.

### Uso Programático

```python
from birth_chart import BirthChart

# Criar mapa natal
chart = BirthChart(
    date="15/01/1990",
    time="14:30",
    location="São Paulo, Brazil"
)

# Ver resumo
print(chart.get_summary())

# Ver lista de planetas
print(chart.get_planet_list())

# Gerar imagem
chart.generate_image("meu_mapa.png")

# Interpretação completa
print(chart.get_full_interpretation())
```

### Exemplos

Veja mais exemplos em:

```bash
python example.py
```

## Resolução de Problemas

### Erro: "No module named 'swisseph'"

Instale novamente as dependências:

```bash
pip install pyswisseph
```

### Erro ao gerar imagem: "cannot open resource"

As fontes padrão não foram encontradas. O aplicativo usará fontes alternativas automaticamente, mas a qualidade pode ser inferior.

### Erro: "Unable to geocode location"

Verifique sua conexão com internet e certifique-se de que o local está no formato correto:
- "Cidade, País" (ex: "São Paulo, Brazil")
- "Cidade, Estado, País" (ex: "Porto Alegre, RS, Brazil")

Se o problema persistir, o aplicativo usará coordenadas padrão (São Paulo).

## Precisão dos Cálculos

Este aplicativo usa a biblioteca Swiss Ephemeris, que é o padrão de ouro em cálculos astronômicos para astrologia. A precisão é da ordem de frações de segundo de arco.

## Suporte

Para problemas ou dúvidas, abra uma issue no repositório.
