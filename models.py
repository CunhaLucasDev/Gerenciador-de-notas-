from dataclasses import dataclass, field
from typing import List

@dataclass
class Aluno:
    nome: str
    cpf: str
    email: str
    notas: List[float] = field(default_factory=list)