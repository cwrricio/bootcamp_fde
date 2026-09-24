"""Fase 0: conferência dos insumos e leitura do corpus."""

from pathlib import Path

import pandas as pd

TOTAL_ARQUIVOS_CORPUS = 12
TOTAL_VIGENTES = 11
TOTAL_REVOGADOS = 1

REGRA_CONTAGEM_PALAVRAS = (
    "Número de palavras = tokens separados por espaço em branco (`len(texto.split())`) "
    "no arquivo completo, incluindo título, cabeçalho `Empresa:` e títulos de seção."
)


def verificar_insumos(pasta: Path) -> None:
    """Para com mensagem clara se a pasta de insumos estiver incompleta."""
    esperados = {
        "corpus/": pasta / "corpus",
        "metadados.csv": pasta / "metadados.csv",
        "perguntas_gabarito.csv": pasta / "perguntas_gabarito.csv",
    }
    faltando = [nome for nome, caminho in esperados.items() if not caminho.exists()]
    if faltando:
        raise ValueError(f"Insumos incompletos em {pasta}: falta {', '.join(faltando)}.")

    arquivos = sorted(p.name for p in (pasta / "corpus").glob("*.md"))
    if len(arquivos) != TOTAL_ARQUIVOS_CORPUS:
        raise ValueError(
            f"A pasta corpus/ deveria ter {TOTAL_ARQUIVOS_CORPUS} arquivos .md, "
            f"mas tem {len(arquivos)}: {arquivos}"
        )


def contar_palavras(texto: str) -> int:
    return len(texto.split())


def carregar_documentos(pasta: Path) -> pd.DataFrame:
    """Lê metadados.csv e guarda o texto completo de cada documento na coluna `texto`."""
    verificar_insumos(pasta)
    documentos = pd.read_csv(pasta / "metadados.csv", encoding="utf-8")

    ausentes = [a for a in documentos["arquivo"] if not (pasta / "corpus" / a).exists()]
    if ausentes:
        raise ValueError(f"metadados.csv aponta para arquivos inexistentes em corpus/: {ausentes}")

    documentos["texto"] = [
        (pasta / "corpus" / arquivo).read_text(encoding="utf-8")
        for arquivo in documentos["arquivo"]
    ]

    contagem = documentos["status"].value_counts()
    vigentes = int(contagem.get("vigente", 0))
    revogados = int(contagem.get("revogada", 0))
    if (vigentes, revogados) != (TOTAL_VIGENTES, TOTAL_REVOGADOS) or len(documentos) != (
        TOTAL_VIGENTES + TOTAL_REVOGADOS
    ):
        raise ValueError(
            f"Esperados {TOTAL_VIGENTES} documentos vigentes e {TOTAL_REVOGADOS} revogado, "
            f"mas a coluna status tem: {contagem.to_dict()}"
        )
    return documentos


def tabela_palavras(documentos: pd.DataFrame) -> pd.DataFrame:
    """Evidência da Parte 0: `doc_id`, `status` e número de palavras de cada documento."""
    return documentos.assign(palavras=documentos["texto"].map(contar_palavras))[
        ["doc_id", "status", "palavras"]
    ]
