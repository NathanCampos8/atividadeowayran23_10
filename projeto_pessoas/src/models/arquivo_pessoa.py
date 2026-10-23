import re
from datetime import date, datetime
from pathlib import Path

FORMATO_PASTA = "%Y%m%d_%H:%M:%S"  # ex.: 20261023_19:43:10


class ArquivoPessoaError(Exception):
    """Tratativa de erro exclusiva da classe ArquivoPessoa."""


class ArquivoPessoa:
    """Mesma ideia da Pessoa, com a capacidade de ser salva em arquivo."""

    def __init__(self, nome: str, data_nascimento: date, data_atual: date | None = None):
        if not nome or not nome.strip():
            raise ArquivoPessoaError("O nome não pode ser vazio.")

        self.nome = nome.strip()
        self.data_nascimento = data_nascimento
        self.data_atual = data_atual or date.today()

        if self.data_nascimento > self.data_atual:
            raise ArquivoPessoaError(
                "A data de nascimento não pode ser maior que a data atual."
            )

    @property
    def idade(self) -> int:
        anos = self.data_atual.year - self.data_nascimento.year
        ja_fez_aniversario = (self.data_atual.month, self.data_atual.day) >= (
            self.data_nascimento.month,
            self.data_nascimento.day,
        )
        return anos if ja_fez_aniversario else anos - 1

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    def salvar(self, pasta_base: Path) -> Path:
        """Salva em <pasta_base>/<AAAAMMDD_HH:MM:SS>/<nome>.txt e retorna o caminho."""
        try:
            pasta = Path(pasta_base) / datetime.now().strftime(FORMATO_PASTA)
            pasta.mkdir(parents=True, exist_ok=True)

            nome_arquivo = re.sub(r"[^\w-]+", "_", self.nome).strip("_").lower() or "pessoa"
            caminho = pasta / f"{nome_arquivo}.txt"

            conteudo = (
                f"nome: {self.nome}\n"
                f"data_nascimento: {self.data_nascimento.isoformat()}\n"
                f"data_atual: {self.data_atual.isoformat()}\n"
                f"idade: {self.idade}\n"
                f"apresentacao: {self.apresentar()}\n"
            )
            caminho.write_text(conteudo, encoding="utf-8")
            return caminho
        except OSError as erro:
            raise ArquivoPessoaError(f"Não foi possível salvar o arquivo: {erro}") from erro
