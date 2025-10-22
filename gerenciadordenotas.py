from input_utils import coleta_dados_aluno, pedir_nota_recuperacao
from processor import avalia_aluno

def imprime_resultado(resultado: dict):
    aluno = resultado["aluno"]
    print("\n" + "="*50)
    print(f"Aluno: {aluno.nome} | Média Inicial: {resultado['media_inicial']:.2f}")

    status = resultado["status"]
    if status == "APROVADO_DIRETO":
        print("STATUS: APROVADO DIRETAMENTE")
        print(f"Parabéns! {aluno.nome} (CPF: {aluno.cpf}, e-mail: {aluno.email}) — média: {resultado['media_inicial']:.2f}.")
    else:
        print("STATUS: RECUPERAÇÃO NECESSÁRIA (Média abaixo de 6.0)")
        print(f"Nota de recuperação: {resultado.get('nota_recuperacao', 0):.2f}")
        print(f"Nova Média (com recuperação): {resultado.get('nova_media', 0):.2f}")

        if status == "APROVADO_RECUPERACAO":
            print(f"STATUS: APROVADO NA RECUPERAÇÃO — {aluno.nome} (CPF: {aluno.cpf}, e-mail: {aluno.email})")
        else:
            print(f"STATUS: REPROVADO APÓS RECUPERAÇÃO — {aluno.nome} ficou com média: {resultado.get('nova_media', 0):.2f}.")

def main():
    lista_alunos = []
    print("Bem-vindo ao Sistema de Gerenciamento de Notas de Alunos!")

    while True:
        aluno = coleta_dados_aluno()
        lista_alunos.append(aluno)

        continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").strip().lower()
        if continuar != 's':
            break

    if not lista_alunos:
        print("\nNenhum aluno foi cadastrado. Programa encerrado.")
        return

    for aluno in lista_alunos:
        resultado = avalia_aluno(aluno, pedir_nota_recuperacao)
        imprime_resultado(resultado)

if __name__ == "__main__":
    main()