# Gerenciamento de Notas
Sistema simples em Python para cadastro e avaliação de alunos com validação de CPF e e‑mail.

## Estrutura do projeto
- models.py — definição da classe Aluno
- input_utils.py — leitura de input e validações (CPF e e‑mail)
- processor.py — regras de cálculo de média e avaliação (recuperação)
- gerenciadordenotas.py — script principal (interface via terminal)
- README.md — este arquivo

## Requisitos
- Python 3.8+

## Validações implementadas
- CPF: validação do formato (aceita com ou sem pontuação) e cálculo dos dígitos verificadores.
- E‑mail: deve conter exatamente um `@`, ter parte local não vazia, domínio contendo `.` e terminar com `.com`.

Observação: atualmente o validador exige domínio terminando em `.com`. Para aceitar `.com.br` ou outros domínios, edite a função `is_valid_email` em `input_utils.py`.

## Como executar (Windows)
Abra o terminal (CMD ou PowerShell) na pasta do projeto e execute:
```bash
python gerenciadordenotas.py
```

## Uso
- Siga as instruções no terminal para cadastrar alunos.
- São solicitadas 3 notas iniciais (0 a 10). Se a média inicial for < 6.0, será pedida a nota de recuperação para recalcular a média.

## Contribuição
Pull requests são bem-vindos. Sugestões comuns:
- Suporte a outros domínios de e‑mail (.com.br, .org, etc.)
- Exportar resultados para CSV
- Adicionar testes unitários

## Licença
Escolha uma licença adequada ao publicar no
