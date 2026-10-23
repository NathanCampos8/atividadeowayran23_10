from datetime import date

from src.models.pessoa import Pessoa


class PessoaService:
    def criar(self, nome: str, data_nascimento: date, data_atual: date | None = None) -> Pessoa:
        return Pessoa(nome, data_nascimento, data_atual)

    def apresentar(self, pessoa: Pessoa) -> str:
        return pessoa.apresentar()
