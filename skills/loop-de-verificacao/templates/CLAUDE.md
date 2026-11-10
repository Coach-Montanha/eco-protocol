# CLAUDE.md (Template de Verificação Autônoma)

## Como provar que ficou pronto
- **Código e API**: `npm test` e `npm run build` (ou `pytest`), ambos saindo com código 0 e sem avisos de linter/typecheck.
- **Edição de Vídeo**: `python conferir_video.py render/final.mp4 --formato 1080x1920 --sonda`, com o relatório terminando em `APROVADO`.
- **Copy e Redação**: Cada item da régua em `regras-copy.md` conferido e comprovado em tabela (primeira linha, limite de caracteres, zero palavras proibidas, CTA presente).
- **Tráfego Pago**: Planilha de campanha com conferência de soma de orçamento, teto individual por conjunto, UTMs e taxonomia de nomes.
- **Landing Page / Web**: Navegador aberto em 390px (mobile) e 1440px (desktop), console sem erros, rede sem 4xx/5xx e fluxo de checkout preenchido até a tela de obrigado.

> **Regra Obrigatória do Agente**:
> Antes de declarar que terminou a tarefa, execute a checagem correspondente e apresente o comando executado e a saída completa na conversa. Se não for possível conferir de forma automatizada, declare explicitamente o que faltou e por que não pôde ser verificado.
