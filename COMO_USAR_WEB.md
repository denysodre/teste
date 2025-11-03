# 🌐 Como Usar a Interface Web

## 🚀 Iniciar a Interface Web

No terminal, execute:

```bash
streamlit run web_app.py
```

Isso abrirá automaticamente seu navegador em `http://localhost:8501`

Se não abrir automaticamente, acesse manualmente: **http://localhost:8501**

---

## 📱 Como Usar

### 1. Preencha o Formulário

- **Nome** (opcional): Seu nome ou da pessoa
- **Data de Nascimento**: Use formato `DD/MM/AAAA` (ex: 19/05/1991)
- **Hora de Nascimento**: Use formato `HH:MM` (ex: 07:55)
- **Local**: Cidade, Estado, País (ex: Vinhedo, SP, Brazil)

### 2. Clique em "Calcular Mapa Natal"

O sistema vai:
- Calcular todas as posições planetárias com precisão astronômica
- Gerar a imagem do mapa
- Preparar as interpretações

### 3. Explore as Abas

A interface tem 5 abas:

#### 🌍 **Visão Geral**
- Mostra Sol, Lua e Ascendente em destaque
- Lista os aspectos principais

#### 🪐 **Planetas Completos**
- Todos os 11 planetas com posições exatas
- Descrição de cada planeta
- Todas as 12 casas astrológicas

#### 🖼️ **Imagem do Mapa**
- Visualização gráfica completa do mapa
- Botão para baixar a imagem

#### 📋 **Resumo**
- Resumo de 5 linhas do mapa
- Visão rápida das principais características

#### 📖 **Interpretação Completa**
- Interpretação profissional detalhada
- Linguagem direta e honesta
- Análise profunda de todos os aspectos

---

## 💡 Dicas

- A interface salva os dados automaticamente enquanto você navega pelas abas
- Você pode calcular múltiplos mapas em sequência
- As imagens são geradas com timestamp único
- Para fechar: pressione `Ctrl+C` no terminal

---

## 🖥️ Modo Terminal (alternativa)

Se preferir o modo terminal tradicional:

```bash
python main.py
```

Ou use a API diretamente:

```python
from birth_chart import BirthChart

chart = BirthChart(
    date="19/05/1991",
    time="07:55",
    location="Vinhedo, SP, Brazil"
)

print(chart.get_summary())
chart.generate_image("mapa.png")
```

---

## ⚠️ Troubleshooting

**Erro de porta ocupada?**
```bash
streamlit run web_app.py --server.port 8502
```

**Erro de import?**
```bash
pip install -r requirements.txt
```

**Navegador não abre automaticamente?**

Acesse manualmente: http://localhost:8501
