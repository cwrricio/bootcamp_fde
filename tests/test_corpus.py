import shutil
from pathlib import Path

import pytest

from assistente.corpus import carregar_documentos, contar_palavras, tabela_palavras

PASTA_INSUMOS = Path(__file__).resolve().parent.parent / "data"


@pytest.fixture
def copia_insumos(tmp_path: Path) -> Path:
    destino = tmp_path / "insumos"
    shutil.copytree(PASTA_INSUMOS, destino)
    return destino


def test_carrega_doze_documentos_com_texto():
    documentos = carregar_documentos(PASTA_INSUMOS)
    assert len(documentos) == 12
    assert documentos["texto"].str.len().gt(0).all()


def test_status_tem_onze_vigentes_e_um_revogado():
    documentos = carregar_documentos(PASTA_INSUMOS)
    assert documentos["status"].value_counts().to_dict() == {"vigente": 11, "revogada": 1}
    assert documentos.loc[documentos["status"] == "revogada", "doc_id"].tolist() == ["POL-004"]


def test_tabela_palavras_tem_colunas_da_evidencia():
    tabela = tabela_palavras(carregar_documentos(PASTA_INSUMOS))
    assert list(tabela.columns) == ["doc_id", "status", "palavras"]
    assert tabela["palavras"].gt(0).all()


def test_contar_palavras_separa_por_espaco_em_branco():
    assert contar_palavras("## Como solicitar\nA solicitação  deve ser feita") == 8


@pytest.mark.parametrize("ausente", ["corpus", "metadados.csv", "perguntas_gabarito.csv"])
def test_falha_se_faltar_insumo(copia_insumos: Path, ausente: str):
    caminho = copia_insumos / ausente
    if caminho.is_dir():
        shutil.rmtree(caminho)
    else:
        caminho.unlink()
    with pytest.raises(ValueError, match=ausente):
        carregar_documentos(copia_insumos)


def test_falha_se_corpus_nao_tiver_doze_arquivos(copia_insumos: Path):
    (copia_insumos / "corpus" / "POL-011_codigo_conduta.md").unlink()
    with pytest.raises(ValueError, match="12 arquivos"):
        carregar_documentos(copia_insumos)


def test_falha_se_contagem_de_status_estiver_errada(copia_insumos: Path):
    metadados = copia_insumos / "metadados.csv"
    metadados.write_text(
        metadados.read_text(encoding="utf-8").replace(",revogada,", ",vigente,"), encoding="utf-8"
    )
    with pytest.raises(ValueError, match="11 documentos vigentes"):
        carregar_documentos(copia_insumos)
