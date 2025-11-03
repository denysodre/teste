"""
Dados de signos, planetas, casas e aspectos
"""

SIGNS = [
    "Áries", "Touro", "Gêmeos", "Câncer",
    "Leão", "Virgem", "Libra", "Escorpião",
    "Sagitário", "Capricórnio", "Aquário", "Peixes"
]

PLANETS = {
    0: {"name": "Sol", "symbol": "☉", "color": "#FDB813"},
    1: {"name": "Lua", "symbol": "☽", "color": "#C0C0C0"},
    2: {"name": "Mercúrio", "symbol": "☿", "color": "#87CEEB"},
    3: {"name": "Vênus", "symbol": "♀", "color": "#FF69B4"},
    4: {"name": "Marte", "symbol": "♂", "color": "#FF4500"},
    5: {"name": "Júpiter", "symbol": "♃", "color": "#FFD700"},
    6: {"name": "Saturno", "symbol": "♄", "color": "#8B4513"},
    7: {"name": "Urano", "symbol": "♅", "color": "#4169E1"},
    8: {"name": "Netuno", "symbol": "♆", "color": "#6A5ACD"},
    9: {"name": "Plutão", "symbol": "♇", "color": "#8B0000"},
    10: {"name": "Nodo Norte", "symbol": "☊", "color": "#800080"},
    11: {"name": "Quiron", "symbol": "⚷", "color": "#A0522D"}
}

ASPECTS = {
    "conjunction": {"angle": 0, "orb": 8, "symbol": "☌", "name": "Conjunção"},
    "opposition": {"angle": 180, "orb": 8, "symbol": "☍", "name": "Oposição"},
    "trine": {"angle": 120, "orb": 8, "symbol": "△", "name": "Trígono"},
    "square": {"angle": 90, "orb": 7, "symbol": "□", "name": "Quadratura"},
    "sextile": {"angle": 60, "orb": 6, "symbol": "⚹", "name": "Sextil"},
    "quincunx": {"angle": 150, "orb": 3, "symbol": "⚻", "name": "Quincúncio"},
    "semisextile": {"angle": 30, "orb": 2, "symbol": "⚺", "name": "Semi-sextil"},
    "semisquare": {"angle": 45, "orb": 2, "symbol": "∠", "name": "Semi-quadratura"},
    "sesquiquadrate": {"angle": 135, "orb": 2, "symbol": "⚼", "name": "Sesqui-quadratura"}
}

HOUSE_SYSTEMS = {
    'P': 'Placidus',
    'K': 'Koch',
    'O': 'Porphyrius',
    'R': 'Regiomontanus',
    'C': 'Campanus',
    'E': 'Equal',
    'W': 'Whole Sign'
}

ELEMENTS = {
    "Fogo": ["Áries", "Leão", "Sagitário"],
    "Terra": ["Touro", "Virgem", "Capricórnio"],
    "Ar": ["Gêmeos", "Libra", "Aquário"],
    "Água": ["Câncer", "Escorpião", "Peixes"]
}

MODALITIES = {
    "Cardinal": ["Áries", "Câncer", "Libra", "Capricórnio"],
    "Fixo": ["Touro", "Leão", "Escorpião", "Aquário"],
    "Mutável": ["Gêmeos", "Virgem", "Sagitário", "Peixes"]
}
