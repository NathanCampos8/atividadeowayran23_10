
import re
from datetime import date, datetime
from pathlib import Path

FORMATO_PASTA = "%Y%m%d_%H-%M-%S"


class ArquivoPessoaError(Exception):
    """Erro exclusivo da classe ArquivoPessoa."""
    pass


class ArquivoPessoa:
    """Classe que representa uma pessoa e permite salvar seus dados."""

    def __init__(
        self,
        nome: str,
        data_nascimento: date,
        data_atual: date | None = None
    ):
        try:
            if not nome or not nome.strip():
                raise ArquivoPessoaError("O nome não pode ser vazio.")

            self.nome = nome.strip()
            self.data_nascimento = data_nascimento
            self.data_atual = data_atual or date.today()

            if self.data_nascimento > self.data_atual:
                raise ArquivoPessoaError(
                    "A data de nascimento não pode ser maior que a data atual."
                )

        except AttributeError as erro:
            raise ArquivoPessoaError(
                "Confira se o nome e as datas foram informados corretamente."
            ) from erro

    @property
    def idade(self) -> int:
        anos = self.data_atual.year - self.data_nascimento.year

        ja_fez_aniversario = (
            self.data_atual.month,
            self.data_atual.day
        ) >= (
            self.data_nascimento.month,
            self.data_nascimento.day
        )

        if not ja_fez_aniversario:
            anos -= 1

        return anos

    def apresentar(self) -> str:
        return (
            f"Olá, meu nome é {self.nome} "
            f"e tenho {self.idade} anos."
        )

    def salvar(self, pasta_base: Path) -> Path:
        """Salva os dados da pessoa em um arquivo de texto."""

        try:
            pasta = Path(pasta_base) / datetime.now().strftime(
                FORMATO_PASTA
            )

            pasta.mkdir(parents=True, exist_ok=True)

            nome_arquivo = re.sub(
                r"[^\w-]+",
                "_",
                self.nome
            ).strip("_").lower()

            if not nome_arquivo:
                nome_arquivo = "pessoa"

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
            raise ArquivoPessoaError(
                f"Não foi possível salvar o arquivo: {erro}"
            ) from erro
