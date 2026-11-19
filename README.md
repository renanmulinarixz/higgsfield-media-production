# Higgsfield Media Production

Skill reutilizável para planejar e produzir mídia com Higgsfield: escolher modelos pela tarefa, verificar benefícios gratuitos/Unlimited, respeitar o orçamento do projeto e preparar assets ou referências para outras ferramentas.

O nome `higgsfield-media-production` identifica a plataforma e a função. A skill não depende de marca, setor, roteiro, duração, estética ou modelo de assistente específico.

## Uso

Com a skill disponível no seu agente, invoque:

```text
Use $higgsfield-media-production para planejar imagens e vídeos para este projeto.
Priorize os benefícios gratuitos e Unlimited realmente disponíveis.
Créditos podem ser usados somente para imagens, até o limite que informei neste projeto.
Não inicie gerações enquanto estivermos apenas planejando.
```

Outros exemplos:

```text
Use $higgsfield-media-production para criar uma imagem de produto conforme estas referências.
Use apenas uma rota gratuita ou Unlimited que cubra a configuração escolhida.
```

```text
Use $higgsfield-media-production para preparar um estudo de transição para meu editor.
Preserve o objeto entre os dois quadros e entregue uma descrição do movimento para implementação.
```

Também atende a imagens finais, cenas cinematográficas, edição, vetores e áudio, desde que o pedido e a autorização daquele projeto incluam esses resultados. Não impõe que toda animação seja feita em código.

## Estrutura e instalação

```text
plugin.json
skills/
  higgsfield-media-production/
    SKILL.md
    agents/openai.yaml
    references/
      model-selection.md
      spending-and-recovery.md
      motion-handoff.md
```

O pacote contém uma skill no formato [Agent Skills](https://agentskills.io/specification) e um `plugin.json` portátil para hosts compatíveis com [Agent Plugins](https://developers.openai.com/plugins/build/plugins). A distribuição pelo GitHub não equivale à aprovação ou publicação no diretório oficial de plugins.

Para instalar somente a skill no Codex, peça ao `$skill-installer` para instalar a pasta `skills/higgsfield-media-production` deste repositório, usando a URL correspondente após a publicação:

```text
Instale com $skill-installer:
https://github.com/renanmulinarixz/higgsfield-media-production/tree/main/skills/higgsfield-media-production
```

A pasta inteira também pode ser copiada para o diretório de skills reconhecido pelo agente. No Codex, o guia atual descreve `.agents/skills/` para escopo de projeto e `~/.agents/skills/` para o usuário; siga a [documentação da sua versão](https://learn.chatgpt.com/docs/build-skills) se o caminho for diferente. Publicar este pacote não instala a skill automaticamente na máquina.

A skill usa o conector Higgsfield disponível no ambiente ou um caminho de navegador suportado quando necessário. Ela não inclui credenciais, não configura uma conexão MCP e não garante acesso a modelos ou benefícios. A autenticação com Higgsfield é feita pela integração apropriada do seu agente.

## O que permanece atualizado

Modelos, preços, formatos, resolução e benefícios são descobertos no momento da tarefa. Este pacote não incorpora um catálogo congelado nem os dados de uma conta. Permissão de gasto e restrições são extraídas do pedido atual; não são concedidas pela instalação da skill.

Os detalhes são carregados conforme a necessidade: seleção de modelos, gastos/recuperação e handoff de motion ficam em referências separadas.

## Licença e relação com a plataforma

MIT. Projeto independente, sem vínculo oficial com Higgsfield ou OpenAI. O uso dos serviços continua sujeito às condições dos respectivos provedores.
