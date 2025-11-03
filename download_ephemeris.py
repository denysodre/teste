#!/usr/bin/env python3
"""
Script para baixar arquivos de efemérides do Swiss Ephemeris
"""

import urllib.request
import os

EPHEMERIS_DIR = "swisseph_data"
EPHEMERIS_URL = "https://www.astro.com/ftp/swisseph/ephe/"

# Arquivos essenciais para cálculos de 1800-2399
ESSENTIAL_FILES = [
    "seas_18.se1",  # 1800-2399
    "semo_18.se1",  # Moon 1800-2399
    "sepl_18.se1",  # Planets 1800-2399
]

def download_file(filename):
    """Baixa um arquivo de efemérides"""
    url = EPHEMERIS_URL + filename
    filepath = os.path.join(EPHEMERIS_DIR, filename)

    if os.path.exists(filepath):
        print(f"✓ {filename} já existe")
        return True

    try:
        print(f"Baixando {filename}... ", end="", flush=True)
        urllib.request.urlretrieve(url, filepath)
        print("✓")
        return True
    except Exception as e:
        print(f"✗ Erro: {e}")
        return False

def main():
    print("="*60)
    print("BAIXANDO ARQUIVOS DE EFEMÉRIDES DO SWISS EPHEMERIS")
    print("="*60)
    print()

    # Criar diretório se não existir
    os.makedirs(EPHEMERIS_DIR, exist_ok=True)

    success_count = 0
    for filename in ESSENTIAL_FILES:
        if download_file(filename):
            success_count += 1

    print()
    print("="*60)
    if success_count == len(ESSENTIAL_FILES):
        print("✅ TODOS OS ARQUIVOS BAIXADOS COM SUCESSO!")
    else:
        print(f"⚠️  {success_count}/{len(ESSENTIAL_FILES)} arquivos baixados")
    print("="*60)

if __name__ == "__main__":
    main()
