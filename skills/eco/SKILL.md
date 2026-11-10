---
name: eco
description: Motor mestre de ultra-eficiência do Antigravity. Unifica roteamento de modelos, despacho Groq/Gemini e diretrizes locais.
---

# Unified `@eco` — Always-Active Ultra-Efficiency & Autonomous Master Engine

O protocolo `/eco` (ou `@eco`) é o **motor global padrão e permanente de eficiência máxima** do ambiente. Ele funde em um único pipeline contínuo o roteamento de tarefas, economia de tokens, despacho externo blindado, disciplina de engenharia, ingestão zero-tokens e portão unificado de segurança.

---

## 1. Roteamento Autônomo Unificado (OmniRoute + Router + Router 2)

O `/eco` classifica e despacha toda carga de trabalho automaticamente entre dois canais de execução, sem necessidade de comandos manuais separados:

### A. Canal Interno (Padrão Antigravity — 100% Local & Seguro)
Aplicado para código local, leitura e edição de arquivos, comandos no terminal, bancos SQLite/PocketBase, cofre Obsidian e testes locais.
- **`flash_lite` (Economia de ~85% de tokens)**: Lookups rápidos, greps, leitura de arquivos, checagens de status e logs.
- **`flash` (Economia de ~65% de tokens)**: Implementações de código, refatorações, criação de componentes e testes unitários.
- **`pro` (Raciocínio Profundo)**: Arquitetura multi-arquivos, redesenhos complexos de sistemas e debugging multi-agente.

### B. Canal Externo (Despacho Cego Blindado — Router & Router 2 Fundidos)
Aplicado automaticamente para tarefas pesadas da web (varredura de múltiplos URLs, digestão analítica em lote, pesquisas exaustivas) ou consultas volumosas:
- **Prioridade 1 — Groq (`llama-3.3-70b-versatile`)**: Respostas instantâneas (< 1s) sem gastar tokens locais de raciocínio (Zero CoT) no Antigravity.
- **Fallback Automático — Gemini 2.5 Flash API**: Acionado se a janela de contexto exceder o limite do Groq ou houver rate limit.
- **Diretriz de Retorno**: Formato bruto, cirúrgico e direto (JSON ou Markdown limpo), sem saudações, cortesias ou preâmbulos.

---

## 2. Ingestão Local Zero-Tokens (`anydoc` + `pdfcraft` + `defuddle`)

Proibido gastar tokens de modelos multimodais caros ou de OCR na leitura de documentos e páginas web quando ferramentas locais offline estiverem disponíveis:
- **PDFs e Formulários**: Processar e extrair texto localmente via `pdfcraft` e CLI nativa antes de qualquer inferência.
- **Arquivos Office (Word, Excel, PPT) e CSVs**: Converter instantaneamente em Markdown limpo (GitHub-Flavored) via `anydoc`.
- **Páginas e Artigos Web**: Extrair corpo limpo em Markdown sem ruído de layout via `defuddle`.

---

## 3. Reuso Estrito & Anti-Reinvenção da Roda (`search-first`)

Antes de gerar qualquer novo utilitário, módulo ou função auxiliar, seguir rigorosamente o funil em 4 etapas:
1. **Verificar Skills Locais**: Avaliar se alguma das ferramentas do ecossistema já cumpre o objetivo.
2. **Verificar APIs Nativas**: Priorizar recursos padrão da linguagem e do SO (`fetch`, `fs`, `pathlib`, `subprocess`).
3. **Verificar Ferramentas de Sistema**: Usar CLIs locais consagradas (`ffmpeg`, `sqlite3`, `yt-dlp`).
4. **Veredito Cirúrgico**: Se já existe, reusar; se parecido, adaptar; se inexistente, escrever o código estritamente necessário.

---

## 4. Portão Unificado de Segurança & Auditoria (`gatekeeper`)

Toda e qualquer alteração de código, refatoração estrutural ou criação de skill é submetida automaticamente ao portão do **`gatekeeper`** (funde `coderabbit`, `open-kritt`, `security-audit` e `seguranca-api-keys`) antes da gravação ou commit:
- **Detecção Estrita de Credenciais (Regra RLAUR)**: Bloqueio imediato de chaves de API, segredos, senhas e tokens expostos em texto puro.
- **Auditoria de Vulnerabilidades OWASP**: Prevenção ativa contra command injection, SQL injection, bypass de autenticação e falhas de sanitização.
- **Conformidade de Código**: Eliminação de dependências npm/pip desnecessárias, vazamentos de memória e código morto.
- **Portão Git**: Comandos `git add .`, `git commit` e `git push` ocorrem estritamente após aprovação do `gatekeeper`.

---

## 5. Higienização Determinística Pré-Commit (`turnitout`)

- Códigos e textos gerados devem ser higienizados localmente com `turnitout` para remover marcas d'água de IA, metadados C2PA e caracteres invisíveis Unicode (*zero-width spaces*), prevenindo quebras em compiladores e falsos positivos em linters.

---

## 6. Diretrizes de Engenharia Ponytail & Karpathy

- **Zero Enrolação Conversacional**: Respostas ultraconcisas sem preâmbulos, saudações ou explicações redundantes.
- **Sem Suposições Silenciosas (*No Silent Assumptions*)**: Expor trade-offs ou solicitar esclarecimento quando houver ambiguidade no requisito.
- **Simplicidade Radical**: "O melhor código é o código não escrito". Proibido criar fábricas ou abstrações desnecessárias.
- **Edições Cirúrgicas Mínimas**: Preservar rigorosamente comentários, docstrings e contexto adjacente de arquivos editados.

---

## 7. Loop Fechado de Verificação & Debugging Stop-the-Line (`loop-de-verificacao` + `debugging-and-error-recovery`)

Fundido diretamente no `@eco` a partir da metodologia de Boris Cherny (criador do Claude Code) e Fabiano:
- **Loop Fechado de 2x a 3x de Qualidade**: O agente nunca finaliza no achismo de "parece pronto". Toda tarefa exige uma checagem determinística que volta binariamente `passou` (0) ou `falhou` (1/2).
- **Pedido com Prova Inegociável**: Respostas de conclusão exigem obrigatoriamente a apresentação do comando executado e a saída completa comprovando a integridade. Proibido declarar término sem prova.
- **Stop Hooks Determinísticos (Exit Code 2)**: Bloqueio estrutural de parada. Se o teste, typecheck, build ou conferidor de vídeo falhar, o processo aborta a saída com código de erro 2 e devolve a lista de falhas para correção imediata pelo agente.
- **Princípio da Sonda (Anti-Cegueira / Erro Plantado)**: "Conferência que nunca reprova não está conferindo nada". Antes de confiar em qualquer rotina de teste ou auditoria, planta-se um erro artificial para provar que a checagem é capaz de reprovar.
- **Revisor Cego Independente**: Entregas críticas são auditadas por subagente somente-leitura (`Read, Glob, Grep`) sem o viés cognitivo do agente que implementou a solução.
- **Tolerância Zero a Chutes (*No Shotgun Debugging*)**: Diante de falhas, congelar edições aleatórias, isolar a causa-raiz (5 Porquês), aplicar correção pontual cirúrgica e validar com teste de regressão.
- **Ciclo de Imunização Contínua**: Todo defeito identificado manualmente vira imediatamente uma nova checagem automatizada na seção "Como provar que ficou pronto" do `CLAUDE.md`.
- **Human-in-the-Loop nos Pontos Sem Volta**: Deploys de produção, subida de campanhas de tráfego, disparo de mensagens e exclusões exigem portão de aprovação humana.

---

## 8. Arquitetura e Otimização de Esquemas

- **Graphify**: Inspecionar grafos de dependências e importações antes de refatorações de código.
- **MicroKit & Bencho UI**: Microinterações modernas e leves em TSX/CSS nativo, fluidez de 60 FPS, sem bibliotecas pesadas de terceiros.
- **mcptoon**: Compressão sob demanda de esquemas MCP para preservar o orçamento de contexto.

---

## 9. Blindagem de Produção, Resiliência & Anti-SaaS (`vibe-production-checklist` + `matriz-anti-saas` + `pocketbase`)

- **Resiliência Nativa**: Toda rota, script ou serviço gerado sob `/eco` deve atender ao checklist de produção: idempotência em operações de escrita/pagamento, limites de taxa defensivos (*rate limiting*), tratamento estrito de timeout de rede e criação obrigatória de índices em colunas de busca no SQLite/PocketBase.
- **Arquitetura Anti-SaaS Local**: Eliminação sistemática de serviços de nuvem pagos de terceiros (Auth0, Firebase, Supabase, Typeform) substituindo-os por binários únicos autônomos locais (PocketBase, SQLite, Hono, Litpage).

---

## 10. Extração Furtiva & Testes Empíricos de Performance (`stealth-browser` + `scrapling` + `load-testing-k6`)

- **Web Scraping Indetectável**: Coleta de dados web resiliente sem estourar orçamento de tokens nem tomar bloqueios de Cloudflare/CAPTCHA, operando com Playwright camuflado (`scrapling`/`stealth-browser`) exclusivamente no Microsoft Edge.
- **Auditoria de Performance Baseada em Dados**: Validação empírica de novas rotas, webhooks e microsserviços via micro-testes de carga locais com `load-testing-k6`. Proibido declarar refatoração concluída sem comprovar ausência de vazamento de memória e estabilidade sob concorrência.

---

## 11. Orquestração Autônoma de Skills & Despacho por Intenção

O protocolo `/eco` atua como **meta-orquestrador autônomo** para todas as 140+ skills do ecossistema, dispensando a necessidade de comandos manuais repetitivos:

1. **Auto-Trigger por Intenção**:
   - **Fisiologia & Treino**: Ativação autônoma imediata de `montanha-coach` + `opex-coaching-system` + `lyle-mcdonald-nutrition` + `lpo-crosstraining` + `minha-voz`.
   - **Conteúdo & Instagram**: Ativação autônoma de `insta` + `formato-carrossel` + `formato-roteiro` + `stories-10x-copy` + `minha-voz`.
   - **Engenharia & Código**: Ativação autônoma de `ponytail` + `karpathy-skills` + `debugging-and-error-recovery` + `gatekeeper` + `loop-de-verificacao`.
   - **Edição & Vídeo**: Ativação autônoma de `insta` + `conferir_video` + `loop-de-verificacao` (com folhas de contato, análise de silêncio/volume e sondas).
   - **Atendimento & Comercial**: Ativação autônoma de `personal-trainer-prompts` + `automatizar-whatsapp-seguro` + `minha-voz`.
   - **Clonagem de Interfaces**: Ativação autônoma de `replica` + `screenshot-to-code` + `impeccable`.
   - **Contratos & Negócios**: Ativação autônoma de `legal-brazil` + `lgpd-web-compliance` + `prospeccao-b2b`.

2. **Presets de Modos Operacionais Nativos**:
   - `@coach`: Consultoria Fisiológica, Cálculo Matemático de TDEE e Treinos de Força/LPO.
   - `@criador`: Esteira Editorial Completa, Carrosséis e Vídeos Verticais 9:16.
   - `@dev`: Engenharia de Software no padrão Ponytail & Karpathy com testes de regressão.
   - `@negocios`: Gestão Comercial, Contratos, Vendas e Ferramentas Anti-SaaS.

3. **Pipelines em Cadeia (Skill Chaining)**:
   - Processamento contínuo entre skills em tarefas compostas (ex: Áudio/Texto Bruto ➔ `extrair-procedimento` ➔ `minha-voz` ➔ `formato-carrossel`/`formato-roteiro` ➔ entrega pronta).

4. **Regra de Auto-Consulta (Search-First de Métodos)**:
   - Proibição absoluta de improvisação genérica quando houver método consagrado no cofre (Everett, Lyle, OPEX, Ladeira).

---

## 12. Telemetria de Tokens & Relatório de Economia Obrigatório

Em cumprimento à diretriz global permanente do `@eco`, toda resposta ao usuário deve concluir com a aferição transparente da economia gerada pelo motor:
- **Gasto Real**: Tokens consumidos na requisição otimizada com `@eco` (execução local, scripts pontuais, mcptoon, qualquer ingestão zero-tokens).
- **Sem Automação**: Custo projetado caso a requisição fosse realizada sem as diretrizes do ecossistema (leituras integrais de arquivos pesados, CoT verboso, schemas MCP sem compressão, ferramentas de nuvem redundantes).
- **Economia Total**: Diferencial de tokens poupados e taxa percentual de eficiência.
