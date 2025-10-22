from typing import Callable, Dict
from models import Aluno

def calcula_media(notas):
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def avalia_aluno(aluno: Aluno, obter_nota_recuperacao: Callable[[Aluno], float]) -> Dict:
    """
    Avalia um aluno. Se precisar de recuperação, usa a função obter_nota_recuperacao(aluno)
    para obter a nota de recuperação (injetada para separar I/O da lógica).
    Retorna um dicionário com resultados (media_inicial, status, nota_recuperacao opc., nova_media opc.).
    """
    media_inicial = calcula_media(aluno.notas)
    resultado = {"aluno": aluno, "media_inicial": media_inicial}

    if media_inicial >= 6.0:
        resultado["status"] = "APROVADO_DIRETO"
        return resultado

    # Recuperação necessária
    nota_rec = obter_nota_recuperacao(aluno)
    nova_media = calcula_media(aluno.notas + [nota_rec])
    resultado["nota_recuperacao"] = nota_rec
    resultado["nova_media"] = nova_media

    if nova_media >= 5.0:
        resultado["status"] = "APROVADO_RECUPERACAO"
    else:
        resultado["status"] = "REPROVADO"

    return resultado