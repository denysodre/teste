#!/usr/bin/env python3
"""
Interface Web do Calculador de Mapa Natal
Execute: streamlit run web_app.py
"""

import streamlit as st
from birth_chart import BirthChart
import os
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Mapa Natal - Calculadora Profissional",
    page_icon="🌟",
    layout="wide"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #4A90E2;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 40px;
    }
    .planet-item {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    .aspect-item {
        background-color: #e8f4f8;
        padding: 8px;
        border-radius: 5px;
        margin: 3px 0;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<div class="main-header">🌟 MAPA NATAL</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Cálculos Astronômicos Precisos com Swiss Ephemeris</div>', unsafe_allow_html=True)

# Sidebar com instruções
with st.sidebar:
    st.header("ℹ️ Como Usar")
    st.markdown("""
    1. Preencha seus dados de nascimento
    2. Clique em **Calcular Mapa Natal**
    3. Explore as abas com:
       - Posições planetárias
       - Imagem do mapa
       - Resumo de 5 linhas
       - Interpretação completa

    ---

    ### 📌 Nota
    - Use formato DD/MM/AAAA para data
    - Use formato HH:MM para hora
    - Seja específico no local (Cidade, Estado)
    """)

    st.markdown("---")
    st.markdown("**Desenvolvido com:**")
    st.markdown("- Python 🐍")
    st.markdown("- Swiss Ephemeris 🌌")
    st.markdown("- Streamlit 🎈")

# Formulário de entrada
st.header("📝 Seus Dados de Nascimento")

col1, col2, col3 = st.columns(3)

with col1:
    nome = st.text_input("Nome (opcional)", placeholder="Ex: João Silva")

with col2:
    data_nascimento = st.text_input(
        "Data de Nascimento *",
        placeholder="DD/MM/AAAA",
        help="Formato: 19/05/1991"
    )

with col3:
    hora_nascimento = st.text_input(
        "Hora de Nascimento *",
        placeholder="HH:MM",
        help="Formato: 07:55"
    )

local_nascimento = st.text_input(
    "Local de Nascimento *",
    placeholder="Cidade, Estado, País",
    help="Ex: São Paulo, SP, Brazil ou Vinhedo, SP, Brazil"
)

# Botão de cálculo
calcular = st.button("🔮 Calcular Mapa Natal", type="primary", use_container_width=True)

# Processar quando o botão for clicado
if calcular:
    if not data_nascimento or not hora_nascimento or not local_nascimento:
        st.error("⚠️ Por favor, preencha todos os campos obrigatórios!")
    else:
        try:
            with st.spinner("🔄 Calculando posições planetárias com precisão astronômica..."):
                # Criar mapa natal
                chart = BirthChart(
                    date=data_nascimento,
                    time=hora_nascimento,
                    location=local_nascimento
                )

                # Armazenar no session state
                st.session_state['chart'] = chart
                st.session_state['nome'] = nome if nome else "Seu Mapa"

            st.success("✅ Mapa calculado com sucesso!")

        except Exception as e:
            st.error(f"❌ Erro ao calcular mapa: {e}")
            st.info("💡 Verifique se a data e hora estão no formato correto.")

# Exibir resultados se o mapa foi calculado
if 'chart' in st.session_state:
    chart = st.session_state['chart']
    nome_exibir = st.session_state.get('nome', 'Seu Mapa')

    st.markdown("---")
    st.header(f"🌟 {nome_exibir}")

    # Criar abas
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🌍 Visão Geral",
        "🪐 Planetas Completos",
        "🖼️ Imagem do Mapa",
        "📋 Resumo",
        "📖 Interpretação Completa"
    ])

    with tab1:
        st.subheader("Seus Planetas Principais")

        sol = chart.planets[0]
        lua = chart.planets[1]
        asc = chart.houses["ascendant"]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #FDB813 0%, #FF8C00 100%); padding: 20px; border-radius: 10px; color: white; text-align: center;">
                <h2>☉ SOL</h2>
                <h3>{sol['degree_int']}° {sol['sign']}</h3>
                <p>Sua essência e identidade</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #C0C0C0 0%, #E8E8E8 100%); padding: 20px; border-radius: 10px; color: #333; text-align: center;">
                <h2>☽ LUA</h2>
                <h3>{lua['degree_int']}° {lua['sign']}</h3>
                <p>Suas emoções e necessidades</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #4A90E2 0%, #357ABD 100%); padding: 20px; border-radius: 10px; color: white; text-align: center;">
                <h2>⬆ ASC</h2>
                <h3>{int(asc['degree'])}° {asc['sign']}</h3>
                <p>Como você se apresenta</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # Aspectos principais
        st.subheader("🔗 Aspectos Principais")

        major_aspects = [a for a in chart.aspects if a['type'] in ['Conjunção', 'Oposição', 'Trígono', 'Quadratura']]

        if major_aspects:
            for i, asp in enumerate(major_aspects[:8], 1):
                exact = " ⭐ EXATO" if asp['exact'] else ""
                st.markdown(f"""
                <div class="aspect-item">
                    <strong>{i}.</strong> {asp['planet1']} {asp['symbol']} {asp['planet2']}
                    - <em>{asp['type']}</em> (orbe {asp['orb']:.1f}°){exact}
                </div>
                """, unsafe_allow_html=True)

            if len(major_aspects) > 8:
                st.info(f"... e mais {len(major_aspects) - 8} aspectos principais")
        else:
            st.info("Nenhum aspecto principal forte encontrado.")

    with tab2:
        st.subheader("🪐 Todas as Posições Planetárias")

        # Lista completa de planetas
        planetas_nomes = {
            0: ("☉ Sol", "Essência, identidade, vitalidade"),
            1: ("☽ Lua", "Emoções, necessidades, instintos"),
            2: ("☿ Mercúrio", "Comunicação, pensamento, lógica"),
            3: ("♀ Vênus", "Amor, valores, prazer, beleza"),
            4: ("♂ Marte", "Ação, desejo, energia, raiva"),
            5: ("♃ Júpiter", "Expansão, sorte, filosofia, fé"),
            6: ("♄ Saturno", "Disciplina, limites, maturidade"),
            7: ("♅ Urano", "Inovação, rebeldia, liberdade"),
            8: ("♆ Netuno", "Espiritualidade, ilusão, dissolução"),
            9: ("♇ Plutão", "Transformação, poder, renascimento"),
            10: ("☊ Nodo Norte", "Propósito evolutivo, destino")
        }

        for key, planet in chart.planets.items():
            if key in planetas_nomes:
                nome_planeta, descricao = planetas_nomes[key]
                retro = " (Retrógrado)" if planet.get('retrograde', False) else ""

                st.markdown(f"""
                <div class="planet-item">
                    <strong>{nome_planeta}</strong> - {planet['degree_int']}°{planet['minute']:02}' {planet['sign']}{retro}
                    <br><small style="color: #666;">{descricao}</small>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("🏠 Casas Astrológicas")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
            **Ascendente:** {int(asc['degree'])}°{int((asc['degree'] % 1) * 60):02}' {asc['sign']}
            """)

            for cusp in chart.houses["cusps"][:6]:
                st.markdown(f"""
                **Casa {cusp['house']}:** {int(cusp['degree'])}°{int((cusp['degree'] % 1) * 60):02}' {cusp['sign']}
                """)

        with col2:
            mc = chart.houses["mc"]
            st.markdown(f"""
            **Meio do Céu (MC):** {int(mc['degree'])}°{int((mc['degree'] % 1) * 60):02}' {mc['sign']}
            """)

            for cusp in chart.houses["cusps"][6:]:
                st.markdown(f"""
                **Casa {cusp['house']}:** {int(cusp['degree'])}°{int((cusp['degree'] % 1) * 60):02}' {cusp['sign']}
                """)

    with tab3:
        st.subheader("🖼️ Visualização do Mapa Natal")

        # Gerar imagem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f"mapa_{timestamp}.png"

        with st.spinner("🎨 Gerando imagem do mapa..."):
            try:
                chart.generate_image(image_filename)

                if os.path.exists(image_filename):
                    st.image(image_filename, caption="Seu Mapa Natal", use_container_width=True)

                    # Botão de download
                    with open(image_filename, "rb") as file:
                        st.download_button(
                            label="💾 Baixar Imagem",
                            data=file,
                            file_name=f"mapa_natal_{nome_exibir.replace(' ', '_')}.png",
                            mime="image/png"
                        )
                else:
                    st.error("Erro ao gerar imagem")
            except Exception as e:
                st.error(f"Erro ao gerar imagem: {e}")

    with tab4:
        st.subheader("📋 Resumo do Seu Mapa")

        resumo = chart.get_summary()
        st.markdown(f"```\n{resumo}\n```")

    with tab5:
        st.subheader("📖 Interpretação Profissional Completa")

        st.info("⚠️ Esta interpretação usa linguagem direta e honesta. Prepare-se para insights profundos.")

        with st.spinner("✍️ Gerando interpretação profissional..."):
            try:
                interpretacao = chart.get_full_interpretation()
                st.markdown(interpretacao)
            except Exception as e:
                st.error(f"Erro ao gerar interpretação: {e}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>Desenvolvido com Swiss Ephemeris para cálculos astronômicos de precisão</p>
    <p><small>Este mapa não é destino - é um mapa. Mostra tendências, não certezas.</small></p>
</div>
""", unsafe_allow_html=True)
