"""Roda as Partes 0 a 5 do assistente de políticas internas, em ordem."""

import argparse
from pathlib import Path

from assistente.corpus import REGRA_CONTAGEM_PALAVRAS, carregar_documentos, tabela_palavras

PASTA_INSUMOS_PADRAO = Path(__file__).resolve().parent / "data"


def ler_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--insumos",
        type=Path,
        default=PASTA_INSUMOS_PADRAO,
        help="pasta com corpus/, metadados.csv e perguntas_gabarito.csv (padrão: data/)",
    )
    return parser.parse_args()


def main() -> None:
    argumentos = ler_argumentos()

    print("## Parte 0: Setup e leitura do corpus\n")
    documentos = carregar_documentos(argumentos.insumos)
    print(tabela_palavras(documentos).to_string(index=False))
    print(f"\n{REGRA_CONTAGEM_PALAVRAS}")


if __name__ == "__main__":
    main()
