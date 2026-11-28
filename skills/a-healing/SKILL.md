---
name: a-healing
description: Motor autonomo de autocura, diagnostico cirurgico de causa-raiz, correcao definitiva e imunizacao contra regressoes com motor @eco integrado.
---

# 🩺 `/a-healing` (ou `/healing`) — Sistema Autônomo de Autocura & Resolução Definitiva

O **`/a-healing`** é o comando mestre unificado de resolução de quebras de build, bugs, falhas em testes e exceções do Ecossistema Montanha.
Funde oficialmente **8 skills satélites**: `healing`, `debugging-and-error-recovery`, `loop-de-verificacao`, `ralph-loop`, `ralpho`, `karpathy-skills`, `ponytail`, `meta-prompt-deep`, `superpowers`.

---

## ⚡ Motor `@eco` & Tolerância Zero a Chutes (*No Shotgun Debugging*)
- **Inspeção Cirúrgica**: Proibido alterar múltiplos arquivos aleatoriamente esperando que compile.
- **Menor Diff Possível**: Correções pontuais no padrão Karpathy/Ponytail, preservando comentários e contexto adjacente.
- **Auto-Elevação por Objetivo Profundo (`meta-prompt-deep`)**: Toda correção ataca a causa-raiz arquitetural e não apenas o sintoma estético.

---

## 🧬 O Pipeline de Autocura Stop-the-Line em 5 Fases

1. **Stop-the-Line & Isolamento (5 Porquês)**:
   - Diante do erro, congele qualquer nova funcionalidade. Isole o log exato e determine a causa primária.
2. **Princípio da Sonda (Anti-Cegueira / Erro Plantado)**:
   - "Conferência que nunca reprova não está conferindo nada". Escreva um teste ou sonda que comprove a falha antes da correção.
3. **Correção Cirúrgica & Imunização**:
   - Aplique o ajuste cirúrgico mínimo. Proibido blocos try/catch vazios que mascaram exceções.
4. **Ralph-Loop Persistente (Iteração Autônoma até Exit 0)**:
   - Reexecução contínua dos testes orientada pelo sistema de arquivos até que todos os testes passem com código 0.
   - Stop Hooks interceptam falhas com código 2 e devolvem para autocorreção.
5. **Revisor Cego Independente**:
   - Subagente somente-leitura audita o diff final para garantir que nenhum efeito colateral foi introduzido.
