from typing import Callable
from models import Aluno
import re

def ler_texto(prompt: str) -> str:
    return input(prompt).strip()

def ler_nota(prompt: str) -> float:
    while True:
        try:
            nota = float(input(prompt))
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número para a nota.")

def is_valid_cpf(cpf: str) -> bool:
    s = re.sub(r'\D', '', cpf)
    if len(s) != 11:
        return False
    if s == s[0] * 11:
        return False
    # primeiro dígito verificador
    soma = sum(int(s[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(s[9]):
        return False
    # segundo dígito verificador
    soma = sum(int(s[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(s[10]):
        return False
    return True

def is_valid_email(email: str) -> bool:
    email = email.strip()
    # Verifica a presença de exatamente um @, pelo menos um caractere antes do @,
    # domínio com '.' e termina em '.com'
    if email.count('@') != 1:
        return False
    local, dominio = email.split('@')
    if not local:
        return False
    if not dominio or '.' not in dominio:
        return False
    if not dominio.endswith('.com'):
        return False
    # checagem simples de caracteres válidos
    if not re.match(r'^[A-Za-z0-9._%+\-@]+$', email):
        return False
    return True

def coleta_dados_aluno() -> Aluno:
    print("\n--- Cadastro de Novo Aluno ---")
    while True:
        nome = ler_texto("Digite o nome do aluno: ")
        if nome:
            break
        print("Nome não pode ser vazio. Tente novamente.")

    while True:
        cpf = ler_texto("Digite o CPF do aluno (apenas números ou com pontuação): ")
        if is_valid_cpf(cpf):
            break
        print("CPF inválido. Verifique e tente novamente.")

    while True:
        email = ler_texto("Digite o e-mail do aluno: ")
        if is_valid_email(email):
            break
        print("E-mail inválido. Deve conter '@' e terminar em '.com'. Tente novamente.")

    notas = []
    for i in range(1, 4):
        notas.append(ler_nota(f"Digite a {i}ª nota do aluno (0 a 10): "))

    return Aluno(nome=nome, cpf=re.sub(r'\D', '', cpf), email=email, notas=notas)

def pedir_nota_recuperacao(aluno: Aluno) -> float:
    return ler_nota(f"Por favor, insira a nota da recuperação de {aluno.nome} (0 a 10): ")