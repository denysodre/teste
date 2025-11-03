"""
Sistema de interpretação profissional de mapas natais
Linguagem direta, sem clichês, focada em insights reais
"""

from typing import Dict, List
from .data import ELEMENTS, MODALITIES


class ChartInterpreter:
    """Interpreta o mapa natal de forma profissional e humanizada"""

    def __init__(self, birth_chart):
        self.chart = birth_chart
        self.sol = birth_chart.planets[0]
        self.lua = birth_chart.planets[1]
        self.mercurio = birth_chart.planets[2]
        self.venus = birth_chart.planets[3]
        self.marte = birth_chart.planets[4]
        self.asc = birth_chart.houses["ascendant"]

    def generate_full_interpretation(self) -> str:
        """Gera interpretação completa do mapa natal"""

        sections = []

        # Cabeçalho
        sections.append(self._header())

        # Sol, Lua e Ascendente - O núcleo da personalidade
        sections.append(self._core_interpretation())

        # Planetas pessoais (Mercúrio, Vênus, Marte)
        sections.append(self._personal_planets())

        # Análise de elementos e modalidades
        sections.append(self._elemental_analysis())

        # Aspectos principais e dinâmicas
        sections.append(self._major_aspects())

        # Casas e áreas de vida
        sections.append(self._houses_analysis())

        # Síntese final
        sections.append(self._synthesis())

        return "\n\n".join(sections)

    def _header(self) -> str:
        return f"""{'='*80}
INTERPRETAÇÃO COMPLETA DO MAPA NATAL
{'='*80}

Data: {self.chart.date_str} às {self.chart.time_str}
Local: {self.chart.location_str}
"""

    def _core_interpretation(self) -> str:
        """Interpretação do Sol, Lua e Ascendente"""
        text = "SOL, LUA E ASCENDENTE: Quem você é\n" + "-"*80 + "\n\n"

        # Sol
        text += f"SOL EM {self.sol['sign'].upper()}\n\n"
        text += self._interpret_sun_sign(self.sol['sign'])

        # Lua
        text += f"\n\nLUA EM {self.lua['sign'].upper()}\n\n"
        text += self._interpret_moon_sign(self.lua['sign'])

        # Ascendente
        text += f"\n\nASCENDENTE EM {self.asc['sign'].upper()}\n\n"
        text += self._interpret_ascendant(self.asc['sign'])

        # Interação entre os três
        text += "\n\nA COMBINAÇÃO\n\n"
        text += self._interpret_core_combo()

        return text

    def _interpret_sun_sign(self, sign: str) -> str:
        """Interpretações diretas do Sol por signo"""
        interpretations = {
            "Áries": "Você não espera as coisas acontecerem, você as faz acontecer. Há uma urgência natural em como você vive - não por ansiedade, mas porque ficar parado simplesmente não faz sentido. Conflito não te assusta; na verdade, você funciona bem sob pressão. O problema é que nem todo mundo opera nessa velocidade, e isso pode criar atritos.",

            "Touro": "Você constrói as coisas devagar porque sabe que o que importa precisa de fundação. Mudança pela mudança te irrita - você muda quando faz sentido, não porque alguém está apressando. Tem uma relação visceral com o mundo físico: comida, toque, beleza, conforto. Isso não é superficial, é como você processa a vida.",

            "Gêmeos": "Sua mente não para, e isso é um recurso, não um defeito. Você conecta ideias que outras pessoas não veriam juntas. A conversa não é só social pra você - é como você pensa, como processa. Ficar preso em uma coisa só te sufoca. Você precisa de variedade, não por tédio, mas porque é assim que você aprende.",

            "Câncer": "Você sente as coisas de forma profunda, mas não necessariamente mostra isso. Há uma camada protetora, porque vulnerabilidade é algo que você só oferece quando confia. Lar não é só um lugar - é um estado emocional. Você constrói segurança ao redor de quem ama, às vezes até demais.",

            "Leão": "Você foi feito para ser visto, mas não no sentido superficial. É que você tem algo a oferecer e sabe disso. Generosidade vem naturalmente quando você se sente valorizado. O problema surge quando você não recebe reconhecimento - aí a insegurança pode virar drama. Mas no fundo, você só quer que sua contribuição importe.",

            "Virgem": "Você vê o que está errado, o que pode melhorar, o que precisa de ajuste. Isso te torna incrivelmente útil, mas também te coloca numa posição de crítica constante - de você mesmo e dos outros. A perfeição não existe, mas você não consegue parar de tentar alcançá-la. Servir os outros te dá propósito, desde que não vire autossacrifício.",

            "Libra": "Você busca equilíbrio, mas não porque é indeciso - é porque vê todos os lados. Relacionamentos são onde você se encontra, mas também onde pode se perder. Harmonia é importante, mas não a qualquer custo. Você tem opinião forte, só precisa confiar mais nela em vez de ajustá-la para manter a paz.",

            "Escorpião": "Você não faz nada pela metade. Intensidade é sua natureza, não uma escolha. Você vai fundo, seja em emoções, interesses ou relacionamentos. Poder e controle importam porque vulnerabilidade te assusta, mesmo que você não admita. Transformação não é metáfora pra você - é literal. Você morre e renasce várias vezes na vida.",

            "Sagitário": "Você precisa de significado, não só de experiência. Viajar, aprender, explorar - isso não é hobby, é necessidade. Você vê possibilidades onde outros veem limites. Mas às vezes você foge do que é difícil ou desconfortável vendendo como 'ir além'. Liberdade é sagrada, mas intimidade não precisa ser prisão.",

            "Capricórnio": "Você leva responsabilidade a sério, às vezes sério demais. Há uma maturidade em você que sempre esteve lá, mesmo quando criança. Você constrói, planeja, executa. Sucesso importa, não por ego, mas porque você precisa saber que seu esforço valeu a pena. Só não se esqueça de viver enquanto constrói.",

            "Aquário": "Você vê o mundo de um ângulo diferente, e isso pode te fazer sentir isolado ou especial, dependendo do dia. Individualidade é inegociável. Você se importa com causas, com coletivo, mas intimidade emocional pode ser desconfortável. Sua mente é futurista, mas às vezes você esquece que vive no presente.",

            "Peixes": "Você absorve tudo ao seu redor - emoções, energias, atmosferas. Fronteiras entre você e os outros são porosas. Isso te dá empatia profunda, mas também te drena. Você vive num mundo interno rico, às vezes mais rico que o externo. Escapismo é tentador porque a realidade pode ser pesada demais."
        }

        return interpretations.get(sign, "")

    def _interpret_moon_sign(self, sign: str) -> str:
        """Interpretações diretas da Lua por signo"""
        interpretations = {
            "Áries": "Você precisa de ação para se sentir bem. Sentar com sentimentos é difícil - você quer fazer algo sobre eles. Raiva aparece rápido, mas também passa rápido. Você se acalma quando tem autonomia emocional, quando pode reagir do seu jeito, no seu tempo.",

            "Touro": "Você precisa de estabilidade emocional. Mudanças bruscas te desregulam. Conforto físico não é luxo, é autocuidado. Você processa emoções devagar, e isso está ok. Segurança material te acalma porque representa segurança emocional. Você ama profundamente, mas também pode se apegar demais.",

            "Gêmeos": "Você precisa falar sobre o que sente para entender o que sente. Silêncio emocional te sufoca. Variedade te nutre - mesma rotina todo dia te deixa emocionalmente vazio. Você se acalma quando pode processar verbalmente, quando alguém realmente te escuta.",

            "Câncer": "Suas emoções são profundas e mutáveis como maré. Você precisa de lar, de pertencimento. Cuidar dos outros te nutre, mas você também precisa ser cuidado. Memória emocional é forte - você não esquece quem te machucou nem quem te acolheu. Vulnerabilidade é sua força, não fraqueza.",

            "Leão": "Você precisa se sentir especial para quem você ama. Generosidade emocional vem fácil, mas você também precisa receber. Ignorância emocional te dói mais que raiva. Você se nutre quando pode brilhar, quando sua presença é reconhecida e celebrada.",

            "Virgem": "Você processa emoções analisando elas. Preocupação é sua forma de cuidar. Você se sente melhor quando pode fazer algo útil, quando pode ajudar. Perfeição emocional não existe, mas você tenta alcançá-la. Autocrítica pode ser devastadora. Servir te nutre, desde que seja valorizado.",

            "Libra": "Você precisa de paz emocional. Conflito te desregula profundamente. Relacionamentos te nutrem, mas solidão também é necessária. Você busca equilíbrio, mas pode se perder tentando agradar. Beleza e harmonia te acalmam - ambiente importa para seu estado emocional.",

            "Escorpião": "Suas emoções são intensas e você sabe disso. Você não consegue sentir superficialmente. Controle emocional é uma ilusão que você tenta manter. Você precisa de profundidade, de verdade, de transformação. Segredos te protegem, mas também te isolam. Confiança é tudo.",

            "Sagitário": "Você precisa de espaço emocional. Clausura afetiva te sufoca. Você se nutre quando pode explorar, aprender, crescer. Otimismo é genuíno, mas às vezes você usa ele para evitar sentimentos difíceis. Liberdade emocional não significa não se comprometer - significa se comprometer por escolha.",

            "Capricórnio": "Você controla suas emoções porque elas te assustam. Vulnerabilidade parece fraqueza, mas não é. Você se nutre com estrutura, com objetivos, com realização. Emoções precisam ser 'úteis' para você dar atenção. Mas às vezes você só precisa sentir, não resolver.",

            "Aquário": "Você racionaliza sentimentos. Distância emocional te protege, mas também te isola. Você se nutre quando pode ser diferente, quando sua individualidade é respeitada. Emoções intensas te desconfortam. Você prefere amizade que paixão, clareza que confusão. Mas permitir caos emocional às vezes é necessário.",

            "Peixes": "Você sente tudo. Fronteiras emocionais são difíceis. Você absorve emoções dos outros como se fossem suas. Isso te dá empatia incrível, mas também te sobrecarrega. Você se nutre em solidão, em arte, em imaginação. Realidade pode ser dura demais. Escapar às vezes é sobrevivência."
        }

        return interpretations.get(sign, "")

    def _interpret_ascendant(self, sign: str) -> str:
        """Interpretações do Ascendente por signo"""
        interpretations = {
            "Áries": "Você chega com energia, às vezes antes de pensar. Primeira impressão: direto, corajoso, impaciente. Você lidera naturalmente, mesmo sem querer. Mas pode parecer agressivo quando só está sendo honesto.",

            "Touro": "Você chega com presença sólida e calma. Primeira impressão: confiável, sensual, teimoso. Você não se apre pressa, e isso incomoda quem está com pressa. Beleza e conforto importam na forma como você se apresenta.",

            "Gêmeos": "Você chega com curiosidade e conversa. Primeira impressão: esperto, sociável, disperso. Você se adapta ao ambiente facilmente. Mas pode parecer superficial quando está só coletando informação.",

            "Câncer": "Você chega com cautela emocional. Primeira impressão: acolhedor, protetor, fechado. Você lê o ambiente antes de se abrir. Pode parecer frio até se sentir seguro, aí é puro calor.",

            "Leão": "Você chega com confiança e presença. Primeira impressão: carismático, generoso, dramático. Você ilumina o ambiente naturalmente. Mas pode parecer arrogante quando só está sendo você.",

            "Virgem": "Você chega observando e analisando. Primeira impressão: útil, modesto, crítico. Você nota detalhes que outros ignoram. Pode parecer frio ou distante, mas você só processa primeiro.",

            "Libra": "Você chega com charme e diplomacia. Primeira impressão: agradável, elegante, indeciso. Você equilibra o ambiente. Mas pode parecer falso quando está só sendo educado.",

            "Escorpião": "Você chega com intensidade silenciosa. Primeira impressão: magnético, misterioso, intimidador. Você vê através das pessoas. Pode parecer desconfiado, porque é.",

            "Sagitário": "Você chega com entusiasmo e honestidade. Primeira impressão: livre, otimista, sem filtro. Você abre portas com seu jeito expansivo. Mas pode parecer irresponsável quando só está sendo espontâneo.",

            "Capricórnio": "Você chega com seriedade e maturidade. Primeira impressão: competente, ambicioso, frio. Você inspira respeito. Mas pode parecer distante quando está só focado.",

            "Aquário": "Você chega sendo diferente, mesmo sem tentar. Primeira impressão: original, descolado, excêntrico. Você desafia expectativas. Pode parecer alienado quando está só sendo autêntico.",

            "Peixes": "Você chega com sensibilidade etérea. Primeira impressão: empático, artístico, confuso. Você se adapta camaleão. Pode parecer perdido quando está só absorvendo o ambiente."
        }

        return interpretations.get(sign, "")

    def _interpret_core_combo(self) -> str:
        """Interpreta a combinação de Sol, Lua e Ascendente"""
        sol_sign = self.sol['sign']
        lua_sign = self.lua['sign']
        asc_sign = self.asc['sign']

        # Analisar compatibilidade de elementos
        elements_analysis = self._analyze_element_harmony(sol_sign, lua_sign, asc_sign)

        text = f"Sol em {sol_sign}, Lua em {lua_sign}, Ascendente em {asc_sign}. "

        if elements_analysis["harmony_level"] == "alta":
            text += "Há uma fluidez natural entre quem você é (Sol), o que você precisa (Lua), e como você se apresenta (Ascendente). Essas partes conversam bem, o que facilita autenticidade. "
        elif elements_analysis["harmony_level"] == "média":
            text += "Há tensão produtiva entre quem você é (Sol), o que você precisa (Lua), e como você se apresenta (Ascendente). Essas partes às vezes puxam em direções diferentes, mas isso pode gerar crescimento. "
        else:
            text += "Há conflito interno real entre quem você é (Sol), o que você precisa (Lua), e como você se apresenta (Ascendente). Essas partes lutam entre si, e integração exige trabalho consciente. "

        # Adicionar insight específico baseado nos elementos
        text += elements_analysis["insight"]

        return text

    def _analyze_element_harmony(self, sol_sign: str, lua_sign: str, asc_sign: str) -> Dict:
        """Analisa harmonia entre elementos do Sol, Lua e Ascendente"""
        # Identificar elementos
        sol_element = self._get_element(sol_sign)
        lua_element = self._get_element(lua_sign)
        asc_element = self._get_element(asc_sign)

        # Compatibilidade de elementos
        compatible_pairs = [
            {"Fogo", "Ar"}, {"Terra", "Água"}
        ]

        same_count = len(set([sol_element, lua_element, asc_element]))

        if same_count == 1:
            # Todos no mesmo elemento
            return {
                "harmony_level": "alta",
                "insight": f"Todos em {sol_element}, você é consistente, mas pode precisar conscientemente desenvolver qualidades dos outros elementos."
            }

        # Verificar compatibilidade
        elements_set = {sol_element, lua_element, asc_element}

        if elements_set in compatible_pairs or elements_set.issubset(pair) for pair in compatible_pairs:
            return {
                "harmony_level": "alta",
                "insight": f"A mistura de {sol_element} e {lua_element} with {asc_element} funciona bem - elementos que se apoiam."
            }

        # Elementos conflitantes
        conflicts = [
            ({"Fogo", "Água"}, "Fogo quer ação, Água quer sentir. Pode haver vapor ou pode haver equilíbrio."),
            ({"Terra", "Ar"}, "Terra quer concreto, Ar quer abstrato. Pode haver conflito ou complementaridade."),
        ]

        for conflict_elements, insight in conflicts:
            if elements_set == conflict_elements or conflict_elements.issubset(elements_set):
                return {
                    "harmony_level": "baixa",
                    "insight": insight
                }

        return {
            "harmony_level": "média",
            "insight": "Combinação complexa que exige navegação consciente entre diferentes necessidades."
        }

    def _get_element(self, sign: str) -> str:
        """Retorna o elemento de um signo"""
        for element, signs in ELEMENTS.items():
            if sign in signs:
                return element
        return ""

    def _personal_planets(self) -> str:
        """Interpretação de Mercúrio, Vênus e Marte"""
        text = "PLANETAS PESSOAIS: Como você pensa, ama e age\n" + "-"*80 + "\n\n"

        text += f"MERCÚRIO EM {self.mercurio['sign'].upper()}: Como você pensa e se comunica\n\n"
        text += self._interpret_mercury(self.mercurio['sign'])

        text += f"\n\nVÊNUS EM {self.venus['sign'].upper()}: Como você ama e valoriza\n\n"
        text += self._interpret_venus(self.venus['sign'])

        text += f"\n\nMARTE EM {self.marte['sign'].upper()}: Como você age e deseja\n\n"
        text += self._interpret_mars(self.marte['sign'])

        return text

    def _interpret_mercury(self, sign: str) -> str:
        """Interpretação breve de Mercúrio"""
        # Implementação simplificada - você pode expandir
        return f"Mercúrio em {sign} colore sua forma de processar informação e se comunicar. [Interpretação completa seria adicionada aqui]"

    def _interpret_venus(self, sign: str) -> str:
        """Interpretação breve de Vênus"""
        return f"Vênus em {sign} define o que você valoriza em relacionamentos e prazer. [Interpretação completa seria adicionada aqui]"

    def _interpret_mars(self, sign: str) -> str:
        """Interpretação breve de Marte"""
        return f"Marte em {sign} mostra como você persegue o que quer e expressa raiva. [Interpretação completa seria adicionada aqui]"

    def _elemental_analysis(self) -> str:
        """Análise de distribuição de elementos e modalidades"""
        text = "ELEMENTOS E MODALIDADES: Seu equilíbrio energético\n" + "-"*80 + "\n\n"

        # Contar elementos
        elements = {"Fogo": 0, "Terra": 0, "Ar": 0, "Água": 0}
        modalities = {"Cardinal": 0, "Fixo": 0, "Mutável": 0}

        for planet in self.chart.planets.values():
            sign = planet["sign"]
            element = self._get_element(sign)
            if element:
                elements[element] += 1

            for modality, signs in MODALITIES.items():
                if sign in signs:
                    modalities[modality] += 1

        # Análise
        dominant_element = max(elements, key=elements.get)
        lacking_element = min(elements, key=elements.get)

        text += f"Elemento dominante: {dominant_element} ({elements[dominant_element]} planetas)\n"
        text += f"Elemento ausente/fraco: {lacking_element} ({elements[lacking_element]} planetas)\n\n"

        text += f"Isso significa que você naturalmente opera em modo {dominant_element.lower()}, "
        text += f"mas pode precisar desenvolver conscientemente qualidades de {lacking_element.lower()}.\n\n"

        # Modalidades
        dominant_modality = max(modalities, key=modalities.get)
        text += f"Modalidade dominante: {dominant_modality} ({modalities[dominant_modality]} planetas)\n"

        return text

    def _major_aspects(self) -> str:
        """Análise dos aspectos principais"""
        text = "ASPECTOS PRINCIPAIS: Dinâmicas internas\n" + "-"*80 + "\n\n"

        major = [a for a in self.chart.aspects if a["type"] in ["Conjunção", "Oposição", "Trígono", "Quadratura"]]

        if not major:
            text += "Poucos aspectos maiores - energia mais independente e menos dinâmica interna.\n"
            return text

        text += f"{len(major)} aspectos principais modelam a dinâmica entre diferentes partes de você.\n\n"

        # Listar alguns aspectos importantes
        for aspect in major[:5]:  # Primeiros 5
            text += f"• {aspect['planet1']} {aspect['symbol']} {aspect['planet2']} ({aspect['type']})\n"

        return text

    def _houses_analysis(self) -> str:
        """Análise rápida das casas"""
        text = "CASAS: Áreas de vida em foco\n" + "-"*80 + "\n\n"

        # Análise simplificada - você pode expandir
        text += "A distribuição de planetas pelas casas mostra onde sua energia se concentra.\n"
        text += "[Análise detalhada de casas seria adicionada aqui]\n"

        return text

    def _synthesis(self) -> str:
        """Síntese final"""
        text = "SÍNTESE\n" + "-"*80 + "\n\n"

        sol_sign = self.sol['sign']
        lua_sign = self.lua['sign']
        asc_sign = self.asc['sign']

        text += f"Você é alguém que carrega a essência de {sol_sign} (identidade), "
        text += f"precisa de {lua_sign} (segurança emocional), "
        text += f"e se apresenta como {asc_sign} (máscara social). "

        text += "Essas camadas nem sempre concordam, e isso é normal. "
        text += "O trabalho é integrá-las conscientemente, não eliminar a tensão.\n\n"

        text += "Este mapa não é destino - é mapa. Mostra tendências, não certezas. "
        text += "Você sempre tem escolha em como vive essas energias."

        return text
