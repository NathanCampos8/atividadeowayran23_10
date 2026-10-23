from datetime import date, datetime

from src.models.arquivo_pessoa import ArquivoPessoaError
from src.services.arquivo_pessoa_service import ArquivoPessoaService
from src.services.pessoa_service import PessoaService


def ler_data_nascimento() -> date:
    while True:
        texto = input("Data de nascimento (DD/MM/AAAA): ").strip()
        try:
            return datetime.strptime(texto, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida. Digite no formato DD/MM/AAAA.")


def main() -> None:
    pessoa_service = PessoaService()
    arquivo_service = ArquivoPessoaService()

    print("=" * 36)
    print("       CADASTRO DE PESSOAS")
    print("=" * 36)

    nome = input("Nome completo: ").strip()
    nascimento = ler_data_nascimento()

    try:
        pessoa = pessoa_service.criar(nome, nascimento)
        print("\n--- Resumo do cadastro ---")
        print(pessoa_service.apresentar(pessoa))
        print(f"Data de nascimento: {pessoa.data_nascimento.strftime('%d/%m/%Y')}")

        opcao = input("\nDeseja salvar os dados em um arquivo? (s/n): ").strip().lower()
        if opcao == "s":
            arquivo_pessoa = arquivo_service.criar(nome, nascimento)
            caminho = arquivo_service.salvar(arquivo_pessoa)
            print(f"Cadastro salvo com sucesso em:\n{caminho}")
        else:
            print("Cadastro exibido, sem salvar arquivo.")
    except (ValueError, ArquivoPessoaError) as erro:
        print(f"Não foi possível concluir o cadastro: {erro}")

    input("\nPressione Enter para encerrar...")


if __name__ == "__main__":
    main()
