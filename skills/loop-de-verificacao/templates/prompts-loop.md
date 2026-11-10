# Os 10 Prompts Prontos para Fechar o Loop de Verificação

Estes prompts implementam o padrão de fechamento de loop em 7 áreas de trabalho diferentes, garantindo que o agente só pare após verificar e provar a entrega.

---

### Prompt 1: O Pedido com Prova (Geral / Código)
```markdown
Objetivo: [o que tem que estar pronto, ex.: o formulário de cadastro valida o e-mail e mostra o erro em vermelho]

Como provar que está pronto:
1. [ex.: npm test sai com código 0 e o teste novo do formulário passa]
2. [ex.: você sobe o app localmente, preenche um e-mail inválido via script/navegador e me mostra o print da mensagem de erro]

Não termine antes de rodar a checagem. No fim da resposta, apresente o comando executado e a saída completa comprovando a aprovação.
```

---

### Prompt 2: Edição de Vídeo que se Autoconfere
```markdown
Edite [arquivo do bruto] seguindo o roteiro em roteiro.txt e renderize em render/final.mp4.

Depois de cada render:
1. Transcreva o render em ouvido.txt usando Whisper local ou ferramenta de transcrição.
2. Rode `python conferir_video.py render/final.mp4 --formato 1080x1920 --roteiro roteiro.txt --ouvido ouvido.txt --sonda`.
3. Abra cada folha de contato em `conferencia/folha_*.jpg` e os cortes em `conferencia/corte_*.jpg` e verifique:
   - Legendas cobrindo rosto ou olhos
   - Textos colados nas bordas de segurança (zonas mortas do Instagram/TikTok)
   - Cortes no meio de gestos bruscos ou boca aberta
4. Conserte todas as pendências apontadas pelo relatório e renderize novamente.
Só termine quando o RELATORIO.md terminar em APROVADO.
```

---

### Prompt 3: Meta de Edição com `/goal`
```markdown
/goal o RELATORIO.md do render mais novo em render/ termina em APROVADO e aparece colado no fim da resposta, com o comando que rodou e nenhuma diferença com o roteiro.txt, ou pare depois de 8 voltas
```

---

### Prompt 4: Auditoria Visual das Folhas de Quadros e Cortes
```markdown
Abra todas as imagens geradas na pasta `conferencia/`: as `folha_*.jpg` têm 12 quadros cada (1 a cada 2 segundos, da esquerda pra direita e de cima pra baixo) e as `corte_*.jpg` mostram 0,2 s antes e 0,2 s depois de cada corte.

Para cada imagem, analise:
1. Se a legenda ou algum texto cobre o rosto, a boca ou os olhos
2. Se algum texto está cortado na borda ou perto demais do topo e da base (área de botões/perfil das redes)
3. Se o corte caiu no meio de um gesto ou com a boca aberta no meio de uma palavra
4. Se alguma animação aparece por cima de outra ou prejudica a legibilidade
5. Se a cor ou o enquadramento muda de um quadro para o outro sem justificativa narrativa

Monte uma tabela com a imagem, o segundo aproximado, o problema detectado e o conserto aplicado. Se o quadro estiver perfeito, marque como "OK".
```

---

### Prompt 5: Criação da Skill de Conferência do Projeto
```markdown
Crie a skill `.claude/skills/conferir-entrega/SKILL.md` deste projeto, em português do Brasil, com no máximo 60 linhas:
1. No frontmatter, `name: conferir-entrega` e uma `description` que diga para usar antes de dizer que qualquer entrega terminou.
2. Os comandos exatos de conferência deste projeto, na ordem de execução, cada um com o que conta como aprovação (código de saída, texto esperado).
3. O que abrir e inspecionar além dos comandos: prints gerados, folhas de quadros, páginas no navegador, logs.
4. O formato exato da prova que você me apresenta no fim: comando rodado, saída e veredito final.
5. Uma seção de armadilhas conhecidas, com os erros que já passaram despercebidos anteriormente.
```

---

### Prompt 6: Revisão Cega contra a Especificação
```markdown
Use o subagente revisor para conferir o que foi feito contra o `SPEC.md`.

Diretrizes:
- Confira se cada requisito foi atendido no código implementado.
- Teste cada fluxo descrito na especificação.
- Aponte apenas problemas funcionais reais e ignore preferências cosméticas de estilo.
- Apresente a lista do que passou, o que falhou e o veredito final: APROVADO ou CONSERTAR.
```

---

### Prompt 7: Régua Rígida de Copywriting
```markdown
Antes de me entregar o texto, confira cada regra abaixo e monte uma tabela com a regra, passou ou falhou e o trecho que comprova:
1. A primeira linha é uma promessa forte, contradição visceral ou número específico.
2. Tem no máximo [N] caracteres.
3. Nenhuma destas palavras proibidas da marca aparece: [lista de palavras proibidas].
4. O CTA final pede explicitamente [a ação combinada, ex.: comentar a palavra X].
5. Todo número ou dado citado tem fonte rastreável em [pasta/arquivo de fontes].
6. A leitura mantém ritmo fluido sem jargões corporativos vazios.

Se alguma regra falhar, reescreva o trecho e confira novamente. Só me entregue quando todos os itens estiverem aprovados.
```

---

### Prompt 8: Tráfego Pago Conferido antes do Upload
```markdown
Abaixo está a tabela exportada da planilha de campanha antes do upload no gerenciador de anúncios. Antes de eu autorizar a subida, confira:
1. A soma do orçamento diário de todos os conjuntos bate exatamente com R$ [valor total acordado].
2. Nenhum conjunto isolado ultrapassa o teto de R$ [limite individual].
3. Todos os links de destino possuem obrigatoriamente os parâmetros `utm_source`, `utm_medium` e `utm_campaign`.
4. O padrão de nomenclatura segue estritamente a convenção `[CAMPANHA]_[OBJETIVO]_[PUBLICO]_[CRIATIVO]`.
5. O público, idade e posicionamento correspondem exatamente ao briefing.

Monte uma tabela com cada checagem, veredito (Passou/Falhou) e o número da linha correspondente.
Importante: A publicação final e ativação dependem exclusivamente de aprovação humana.
```

---

### Prompt 9: Landing Page Testada no Navegador Real
```markdown
Abra a página local [ex.: http://localhost:3000] no navegador no Microsoft Edge em duas resoluções: 390px (Mobile) e 1440px (Desktop).

Checagens obrigatórias:
1. Tire print das duas larguras e compare visualmente com o layout de referência em [mockup].
2. Verifique se o console JavaScript possui zero erros e se nenhuma requisição de rede retornou status 4xx ou 5xx.
3. Clique no botão de CTA principal e preencha o formulário de cadastro/compra com dados válidos até a confirmação na tela de agradecimento.
4. Teste um preenchimento com dados inválidos e garanta que as mensagens de validação estão legíveis.
5. Liste cada divergência, aplique a correção pontual no código e confira novamente.

Só termine quando ambas as larguras estiverem perfeitamente alinhadas ao design e o fluxo completo for aprovado com prints comprobatórios.
```

---

### Prompt 10: Novo Erro Humano Vira Checagem Automatizada
```markdown
Eu identifiquei este erro na entrega e a conferência anterior deixou passar: [descreva o erro, ex.: a legenda cobriu o rosto da pessoa entre 12 s e 14 s].

Execute o ciclo de imunização do sistema:
1. Explique em uma frase objetiva por que a checagem anterior não detectou esse erro.
2. Implemente uma checagem nova que capture especificamente esse padrão de falha (no script ou na skill de verificação).
3. Plante esse mesmo erro propositalmente em uma cópia de teste e mostre que agora a conferência REPROVA com status CONSERTAR.
4. Execute novamente na versão corrigida e comprove que ela recebe o status APROVADO.
5. Registre a nova regra na seção "Como provar que ficou pronto" do CLAUDE.md do projeto.
```
