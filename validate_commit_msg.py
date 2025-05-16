import sys
import re

commit_msg_file = sys.argv[1]

with open(commit_msg_file, 'r', encoding='utf-8') as f:
    commit_msg = f.read().strip()

# Padrão: tipo(en-US) ou pt-br seguido de descrição, tudo em minúsculas
pattern = r'^(feat|fix|docs|style|refactor|test|chore)(\([a-zA-Z0-9]+\))?: .+'

if not re.match(pattern, commit_msg):
    print("Mensagem de commit inválida.")
    print("Use o padrão: 'tipo(scope)?: descrição' em minúsculas, conforme o padrão Conventional Commit.")
    sys.exit(1)