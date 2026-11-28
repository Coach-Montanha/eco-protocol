#!/usr/bin/env python3
"""
@eco Omni-Trimmer — Next-Action Log Compressor
Filtra saídas ruidosas de compilação, testes, linters e git,
preservando estritamente:
- Código de retorno / status
- Arquivo e linha exata de falhas / exceções
- Mensagens de erro críticas

Uso:
  python trim_output.py --command "npm test"
  ou via pipe:
  npm test | python trim_output.py
"""

import sys
import re
import subprocess
import argparse

CRITICAL_PATTERNS = [
    re.compile(r"(error|fatal|fail|failed|failure|exception|traceback|syntaxerror|typeerror|referenceerror)", re.IGNORECASE),
    re.compile(r"^\s*(at |file \".*\", line \d+)", re.IGNORECASE),
    re.compile(r"(\:\d+\:\d+\:|\:\d+\:)", re.IGNORECASE),
    re.compile(r"(exit code|exited with code) \d+", re.IGNORECASE),
]

NOISE_PATTERNS = [
    re.compile(r"^\s*(\[?\d+%\s*\]?|downloading|fetching|\.{3,})", re.IGNORECASE),
    re.compile(r"(npm warn|warning: LF will be replaced|up to date in|\d+ packages are looking for funding)", re.IGNORECASE),
    re.compile(r"^\s*[-=~_*]{5,}\s*$"),
]

def is_critical(line: str) -> bool:
    for pat in CRITICAL_PATTERNS:
        if pat.search(line):
            return True
    return False

def is_noise(line: str) -> bool:
    for pat in NOISE_PATTERNS:
        if pat.search(line):
            return True
    return False

def trim_text(text: str, max_head=10, max_tail=15) -> str:
    lines = text.splitlines()
    total_lines = len(lines)
    if total_lines <= (max_head + max_tail + 5):
        return text

    critical_lines = []
    for i, line in enumerate(lines):
        if is_critical(line) and not is_noise(line):
            critical_lines.append((i + 1, line))

    if not critical_lines:
        # Se não há erros, devolve apenas cabeçalho e rodapé compacto
        trimmed = lines[:max_head]
        trimmed.append(f"\n... [ @eco trimmed {total_lines - max_head - max_tail} lines of clean output ] ...\n")
        trimmed.extend(lines[-max_tail:])
        return "\n".join(trimmed)

    # Se há erros, foca nas linhas críticas
    output = []
    output.append(f"[ @eco trimmer: {total_lines} lines -> {len(critical_lines)} critical lines isolated ]")
    for lineno, line in critical_lines:
        output.append(f"L{lineno}: {line}")
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="@eco Next-Action Log Compressor")
    parser.add_argument("--command", "-c", type=str, help="Comando a ser executado e filtrado")
    args = parser.parse_args()

    if args.command:
        proc = subprocess.Popen(args.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        stdout, _ = proc.communicate()
        filtered = trim_text(stdout)
        print(filtered)
        sys.exit(proc.returncode)
    else:
        if not sys.stdin.isatty():
            content = sys.stdin.read()
            print(trim_text(content))
        else:
            parser.print_help()

if __name__ == "__main__":
    main()
