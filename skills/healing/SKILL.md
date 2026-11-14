---
name: healing
description: Motor autônomo de autocura, diagnóstico cirúrgico de causa-raiz, correção definitiva e imunização contra regressões com motor @eco integrado para economia extrema de tokens.
---

# 🩺 `/healing` — Sistema Autônomo de Autocura & Resolução Definitiva de Erros

O `/healing` (ou `@healing`) é a skill de **resolução definitiva de falhas, quebras de build, bugs e exceções**. Ele funde as melhores metodologias do ecossistema:
- **`debugging-and-error-recovery`**: Metodologia Stop-the-Line e isolamento de causa-raiz (5 Porquês).
- **`loop-de-verificacao`**: Metodologia Boris Cherny (Claude Code) e Fabiano (Pedido com Prova, Sonda de Erro Plantado, Stop Hooks Exit 2 e Revisor Cego).
- **`ralph-loop` / `ralpho`**: Iteração autônoma contínua orientada a testes até obter saída 0 sem pausas desnecessárias.
- **`karpathy-skills` & `ponytail`**: Simplicidade radical, edições cirúrgicas mínimas e tolerância zero a dependências desnecessárias.
- **`gatekeeper`**: Blindagem de segurança (OWASP, RLAUR, integridade de contratos).
- **Motor `@eco` Nativo**: Orçamento rigoroso de tokens, leituras cirúrgicas por range, zero CoT desperdiçado e telemetria de consumo.

---

## ⚡ Motor `@eco` Integrado — Eficiência & Economia Radical

O `/healing` opera sob as regras inegociáveis de economia do **`@eco`**:

1. **Inspeção Cirúrgica Zero-Waste**:
   - Proibido carregar arquivos inteiros de 1.000 linhas no contexto. Usar `grep`, `search` ou `read_file` com `StartLine` e `EndLine` estritos em torno do ponto de falha indicado no stack trace.
   - Proibido ler logs de gigabytes ou dumps brutos no chat: filtrar no terminal (`Select-String`, `grep`, `tail -n 50`) antes da ingestão.
2. **Anti-Shotgun Debugging (Zero Chutes no Escuro)**:
   - Proibido editar 3 ou 4 arquivos ao mesmo tempo na esperança de que um resolva.
   - Cada ciclo altera **estritamente o arquivo e as linhas onde a causa-raiz reside**.
3. **Ponytail & Karpathy Minimal Diff**:
   - O conserto ideal tem entre 1 e 15 linhas. Proibido reescrever módulos inteiros, mudar a arquitetura ou adicionar novas bibliotecas npm/pip para contornar uma falha pontual.
4. **Telemetria de Tokens Obrigatória**:
   - Ao final de cada sessão `/healing`, emitir o relatório comparativo de economia de tokens do `@eco`.

---

## 🧬 O Pipeline de Autocura em 5 Fases

```
 ┌──────────────────────────────────────────────────────────────┐
 │  1. STOP-THE-LINE (Congelamento & Isolamento)                │
 │  - Congela edições aleatórias.                               │
 │  - Captura o stack trace real e isola as variáveis de entrada.│
 └──────────────────────────────┬───────────────────────────────┘
                                │
                                ▼
 ┌──────────────────────────────────────────────────────────────┐
 │  2. SONDA DETERMINÍSTICA (Reprodução Obrigatória)            │
 │  - Escreve um teste unitário mínimo reproduzindo o bug.      │
 │  - Princípio da Sonda: O teste TEM que falhar agora (red).   │
 └──────────────────────────────┬───────────────────────────────┘
                                │
                                ▼
 ┌──────────────────────────────────────────────────────────────┐
 │  3. CORREÇÃO CIRÚRGICA (Causa-Raiz, Não Sintoma)             │
 │  - 5 Porquês: Tratar a origem (ex: por que veio nulo?).      │
 │  - Proibido mascarar com try/catch vazio ou "any".           │
 │  - Menor diff de código possível (padrão Karpathy).          │
 └──────────────────────────────┬───────────────────────────────┘
                                │
                                ▼
 ┌──────────────────────────────────────────────────────────────┐
 │  4. RALPH-LOOP DE VERIFICAÇÃO FECHADA (Exit Code 0)          │
 │  - Executa o teste mínimo: deve dar PASS (green).            │
 │  - Executa a suíte de regressão do projeto: tudo 100% verde. │
 │  - Se falhar: Stop Hook aborta com Exit 2 e reinicia o loop. │
 └──────────────────────────────┬───────────────────────────────┘
                                │
                                ▼
 ┌──────────────────────────────────────────────────────────────┐
 │  5. IMUNIZAÇÃO PERMANENTE & AUDITORIA GATEKEEPER             │
 │  - O teste do bug vira teste permanente no repositório.      │
 │  - Regra registrada em "Como provar que ficou pronto".       │
 │  - Auditoria Gatekeeper: sem credenciais expostas nem OWASP. │
 └──────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Passo a Passo Operacional do `/healing`

### Passo 1: Stop-the-Line (Congelamento Imediato)
Quando um erro acontecer:
- **PARE**: Não saia alterando código sem entender a causa exata.
- Isole a mensagem exata de erro, arquivo e linha do stack trace.
- Verifique o estado git atual (`git status`, `git diff`) para garantir que você sabe exatamente o ponto de partida limpo.

### Passo 2: Sonda Determinística (O Teste da Prova)
- **Princípio da Sonda**: *"Conferência que nunca reprova não está conferindo nada."*
- Crie ou aponte um comando específico que reproduza a falha:
  ```bash
  # Exemplo: Rodar apenas o teste do caso que quebrou
  npm test -- -t "deve validar token expirado"
  # ou script python mínimo:
  python scripts/test_reproduce_bug.py
  ```
- **Condição obrigatória**: O teste DEVE falhar antes da correção ser aplicada. Se passar antes, o teste não reproduziu o bug real.

### Passo 3: Diagnóstico de Causa-Raiz (5 Porquês)
Aplique os 5 Porquês para encontrar a causa estrutural:
1. *Por que a requisição retornou 500?* -> Porque acessou `user.profile.id` e `profile` estava `undefined`.
2. *Por que `profile` estava `undefined`?* -> Porque o usuário foi criado via OAuth sem perfil inicial.
3. *Por que não havia perfil inicial?* -> Porque o webhook de registro não chamou a trigger de criação de profile.
4. *Causa-Raiz*: O fluxo de OAuth não instancia o registro default de perfil.
5. **Correção Cirúrgica**: Garantir que o fluxo de OAuth crie o perfil padrão no banco ou que a leitura use fallback defensivo tipado.

### Passo 4: Aplicação da Cirurgia Karpathy/Ponytail
- Abra somente o arquivo afetado.
- Aplique a alteração cirúrgica com o mínimo de caracteres necessários.
- Proibido introduzir novas dependências no `package.json` ou `requirements.txt` sem justificativa crítica.
- Proibido silenciar erros com blocos `try { ... } catch (e) {}` vazios.

### Passo 5: Ralph-Loop de Verificação Fechada
- Execute o comando de validação isolado.
- Execute a suíte completa de testes e o build do projeto:
  ```bash
  npm test && npm run build
  # ou pytest tests/ && mypy src/
  ```
- **Critério inegociável de conclusão**: O processo DEVE retornar código de saída `0`. Se retornar `1` ou `2`, o `/healing` continua iterando de forma autônoma sem pedir autorização para pequenos ajustes.

### Passo 6: Imunização Definitiva
Para o erro nunca mais voltar:
1. **Permanência do Teste**: O teste reproduzível criado no Passo 2 é incorporado oficialmente à pasta `tests/` do projeto.
2. **Atualização da Régua**: Se o projeto tiver `CLAUDE.md` ou documentação de verificação, adicione o novo caso na seção "Como provar que ficou pronto".
3. **Auditoria Gatekeeper**: Validar que nenhuma chave privada, token ou vulnerabilidade foi introduzida.

---

## 📋 Checklist Rápido de Conclusão do `/healing`

Antes de declarar o bug como resolvido, valide os 5 pontos:
- [ ] A causa-raiz foi identificada (e não apenas o sintoma mascarado)?
- [ ] Foi criado um teste/sonda que comprovadamente falhou antes da correção?
- [ ] A correção foi cirúrgica (diff mínimo, sem bibliotecas pesadas adicionadas)?
- [ ] A validação executou e retornou `exit code 0` com evidência (comando + output exibidos)?
- [ ] O teste virou parte permanente da suíte de regressão (imunização garantida)?

---

## 📊 Formato de Resposta com Telemetria @eco

Toda execução do `/healing` deve finalizar com a apresentação da prova e o resumo de telemetria:

```markdown
### 🩺 Diagnóstico & Resolução /healing:
- **Causa-Raiz**: <descrição em 1 linha da causa estrutural>
- **Arquivo Modificado**: [<caminho>](file:///<caminho>#L10-L25) (diff cirúrgico de X linhas)
- **Sonda de Reprodução**: <comando de teste que falhava> (Falhou com código X antes)
- **Prova de Resolução**: <comando executado> -> Código de saída 0 (PASS)
- **Imunização**: Teste persistido em tests/<nome_do_teste>

---
📊 **Telemetria de Tokens @eco**:
- **Gasto Real**: ~X tokens (leituras cirúrgicas por offset, diff mínimo)
- **Sem Automação**: ~Z tokens (leitura integral de arquivos e tentativas no escuro)
- **Economia Total**: ~K tokens poupados (~W%)
```
