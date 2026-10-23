from datetime import date
from pathlib import Path

from src.models.arquivo_pessoa import ArquivoPessoa

# <raiz do projeto>/arquivos_criados
PASTA_ARQUIVOS = Path(__file__).resolve().parents[2] / "arquivos_criados"


class ArquivoPessoaService:
    def criar(
        self, nome: str, data_nascimento: date, data_atual: date | None = None
    ) -> ArquivoPessoa:
        return ArquivoPessoa(nome, data_nascimento, data_atual)

    def salvar(self, arquivo_pessoa: ArquivoPessoa) -> Path:
        return arquivo_pessoa.salvar(PASTA_ARQUIVOS)
