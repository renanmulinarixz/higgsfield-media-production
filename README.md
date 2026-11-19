# Higgsfield Media Production e BeSafe Motion

Skill reutilizável para planejar e produzir mídia com Higgsfield: escolher modelos pela tarefa, verificar benefícios gratuitos/Unlimited, respeitar o orçamento do projeto e preparar assets ou referências para outras ferramentas.

O pacote 1.1.0 contém duas skills independentes. `higgsfield-media-production` identifica a plataforma e a função; não depende de marca, setor, roteiro, duração, estética ou modelo de assistente específico. `besafe-motion` concentra a direção educativa da BeSafe, templates editáveis, renderizadores locais e referências de animação de logos e elementos.

| Skill | Usar quando |
| --- | --- |
| [higgsfield-media-production](skills/higgsfield-media-production/SKILL.md) | Planejar ou produzir mídia com os modelos e benefícios reais do Higgsfield |
| [besafe-motion](skills/besafe-motion/SKILL.md) | Criar ou revisar aulas BeSafe, demonstrações de interfaces, aberturas e assinaturas de marca |

A skill de motion pode executar a rota local sem conta Higgsfield. Seus renderizadores exigem dependências locais e exportam vídeo sem áudio; aulas narradas precisam de síntese, sincronização e mixagem adicionais. O catálogo oferece um modelo próprio de 20 s/600 frames e oito referências de logos/elementos com 2.102 frames consultáveis.

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
  besafe-motion/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
    assets/
```

O pacote contém duas skills no formato [Agent Skills](https://agentskills.io/specification) e um `plugin.json` portátil para hosts compatíveis com [Agent Plugins](https://developers.openai.com/plugins/build/plugins). A distribuição pelo GitHub não equivale à aprovação ou publicação no diretório oficial de plugins.

Para instalar somente a skill no Codex, peça ao `$skill-installer` para instalar a pasta `skills/higgsfield-media-production` deste repositório, usando a URL correspondente após a publicação:

```text
Instale com $skill-installer:
https://github.com/renanmulinarixz/higgsfield-media-production/tree/main/skills/higgsfield-media-production
```

Para instalar a skill de motion, use o mesmo instalador com:

```text
https://github.com/renanmulinarixz/higgsfield-media-production/tree/main/skills/besafe-motion
```

Exemplo de uso:

```text
Use $besafe-motion para preparar uma aula sobre um falso alerta no Gmail.
Siga o roteiro aprovado, mantenha a mensagem entre os beats e use a voz Francisca Neural.
Para a abertura, escolha uma técnica de logo que ajude a conduzir o olhar até o remetente.
```

Na pasta `skills/besafe-motion`, execute `python scripts/prepare_reference_frames.py` para materializar os 2.102 frames do Pinterest e abra `assets/pinterest-logos/index.html`. Cada fonte tem folha de contato, PTS, fases editoriais e origem. Para o modelo próprio, use `python scripts/prepare_reference_frames.py --source model` com FFmpeg instalado e abra `assets/index.html`. Os JPEGs materializados ficam ignorados pelo Git; os oito ZIPs e o MP4 próprio fazem parte do pacote.

Leia [validação e limites](skills/besafe-motion/references/validation.md) para distinguir inspeção visual amostrada, integridade dos arquivos e testes de renderização em cada ambiente. Os quatro vídeos YouTube citados tiveram análise automática e não têm frames internos incluídos.

A pasta inteira também pode ser copiada para o diretório de skills reconhecido pelo agente. No Codex, o guia atual descreve `.agents/skills/` para escopo de projeto e `~/.agents/skills/` para o usuário; siga a [documentação da sua versão](https://learn.chatgpt.com/docs/build-skills) se o caminho for diferente. Publicar este pacote não instala a skill automaticamente na máquina.

A skill usa o conector Higgsfield disponível no ambiente ou um caminho de navegador suportado quando necessário. Ela não inclui credenciais, não configura uma conexão MCP e não garante acesso a modelos ou benefícios. A autenticação com Higgsfield é feita pela integração apropriada do seu agente.

## O que permanece atualizado

Modelos, preços, formatos, resolução e benefícios são descobertos no momento da tarefa. Este pacote não incorpora um catálogo congelado nem os dados de uma conta. Permissão de gasto e restrições são extraídas do pedido atual; não são concedidas pela instalação da skill.

Os detalhes são carregados conforme a necessidade: seleção de modelos, gastos/recuperação e handoff de motion ficam em referências separadas.

## Licença e relação com a plataforma

MIT para código e textos próprios. As referências externas e marcas mantêm os direitos dos respectivos titulares; consulte [o aviso do acervo](skills/besafe-motion/assets/pinterest-logos/NOTICE.md) e os registros de origem. Projeto independente, sem vínculo oficial com Higgsfield ou OpenAI. O uso dos serviços continua sujeito às condições dos respectivos provedores.
