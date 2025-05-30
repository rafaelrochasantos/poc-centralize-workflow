import sys
import re
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    commit_msg_file = sys.argv[1]

    with open(commit_msg_file, 'r', encoding='utf-8') as f:
        commit_msg = f.read().strip()

    # Regex simples para Conventional Commits
    pattern = r'^(build|ci|docs|feat|fix|perf|refactor|style|test|chore)(\([a-zA-Z0-9_-]+\))?: .+'

    if re.match(pattern, commit_msg):
        print("✅ Commit message is valid.")
        return 0
    else:
        print("❌ Commit message is invalid.")
        print()
        print("👉 Use o formato do Conventional Commits:")
        print("   <type>(<scope>): <descrição>")
        print()
        print("Exemplo válido: feat(login): adiciona autenticação via Google")
        return 1

if __name__ == '__main__':
    sys.exit(main())