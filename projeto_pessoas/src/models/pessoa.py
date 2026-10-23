from datetime import date


class Pessoa:
    """Representa uma pessoa. A idade é calculada: data_atual - data_nascimento."""

    def __init__(self, nome: str, data_nascimento: date, data_atual: date | None = None):
        if not nome or not nome.strip():
            raise ValueError("O nome não pode ser vazio.")

        self.nome = nome.strip()
        self.data_nascimento = data_nascimento
        self.data_atual = data_atual or date.today()

        if self.data_nascimento > self.data_atual:
            raise ValueError("A data de nascimento não pode ser maior que a data atual.")

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
