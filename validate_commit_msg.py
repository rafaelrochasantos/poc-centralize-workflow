import sys
import re

commit_msg = sys.stdin.read().strip()

# Padrão: tipos do Conventional Commit em lowercase e com uma mensagem
pattern = r'^(feat|fix|docs|style|refactor|test|chore)(\([a-zA-Z0-9]+\))?: .+'

if not re.match(pattern, commit_msg):
    print("Mensagem de commit inválida. Use o padrão 'tipo(scope)?: descrição' em minúsculas.")
    sys.exit(1)