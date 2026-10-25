---
name: obsidian-flow
description: Hub unificado de ingestão, manipulação e visualização no Obsidian. Funde obsidian-cli, obsidian-markdown, obsidian-bases, anydoc e json-canvas.
---

# 🧠 /obsidian-flow — Hub Unificado de Conhecimento Obsidian

O `/obsidian-flow` integra em um único comando atômico todas as operações sobre o cofre [Obsidian-Cofre-Montanha](file:///c:/Users/Administrator/Documents/Projetos/Obsidian-Cofre-Montanha):

## 1. Módulos Integrados
- **`anydoc`**: Conversão direta e local de PDF, DOCX, XLSX e CSV para Markdown limpo (GitHub-Flavored / Obsidian) sem custos de OCR.
- **`obsidian-markdown`**: Formatação nativa com wikilinks `[[Nota]]`, tags `#tag`, callouts (`> [!NOTE]`) e frontmatter YAML padronizado.
- **`obsidian-cli`**: Leitura, busca, criação e sincronização direta de notas no cofre via terminal.
- **`obsidian-bases`**: Estruturação de dados relacionais em visualizações de tabela, cartões, filtros e resumos.
- **`json-canvas`**: Criação e atualização de mapas visuais `.canvas` conectando nós e cartões conceituais.

## 2. Diretrizes de Execução
1. Sempre priorizar wikilinks explícitos (`[[Alunos/Nome]]`, `[[Skills/...]]`) para manter a densidade do gráfico do cofre.
2. Usar renderização limpa sem poluição de metadados desnecessários.
3. Se envolver tabelas de dados, estruturar com propriedades no frontmatter para integração com o Obsidian Dataview / Bases.

## 3. Exemplos Práticos
- Ingestão de documento:
  > `/obsidian-flow converta o PDF anamnese-carlos.pdf em nota estruturada dentro de [[Alunos/Carlos]], gere as tags de saúde e crie um nó no mapa mental [[Dashboard-Alunos.canvas]].`
- Criação e linkagem rápida:
  > `/obsidian-flow crie a ficha técnica do treino de força máxima com wikilinks para [[Periodizacao]] e [[Metodologia-Montanha]].`
