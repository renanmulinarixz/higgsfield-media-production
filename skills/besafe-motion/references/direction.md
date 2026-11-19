## 1. Contrato de criação
Interpretar “sem ferramentas externas” como independência de provedores de geração: HTML, CSS, SVG, Canvas e JavaScript locais como base. Para MP4, usar navegador local e FFmpeg já disponíveis. Uma exportação MP4 ainda exige esses executáveis; não prometer renderização sem dependências. Não carregar bibliotecas, imagens ou fontes por CDN na versão offline.

Quando o usuário autorizar outra ferramenta, adaptar a execução e preservar o mesmo roteiro, entidades, textos, tempos e critérios de qualidade. Ferramenta disponível não é sinônimo de ferramenta conectada ou autorizada para uma geração paga.

Para cada produção, preencher:
- objetivo de aprendizagem em uma frase;
- ação que a pessoa deverá reconhecer ou executar;
- público, contexto e canal de exibição;
- duração, formato, fps, idioma, locução e legendas;
- roteiro aprovado e fatos que precisam de verificação;
- ativos autorizados, identidade visual e interfaces fictícias;
- rota de execução, capacidade confirmada e dependências;
- objeto que permanece ao longo da narrativa;
- quadros de referência com origem e motivo de seleção.

Padrão para testes: 20 s, 30 fps, 16:9. O modelo atual possui 1440 × 810 px e 600 quadros; resolução escolhida para esse teste, não regra de identidade. Reenquadrar para 9:16; não recortar automaticamente uma composição horizontal.

### Narração das aulas BeSafe

Voz aprovada pelo usuário em 18/11/2026: Microsoft Francisca Neural, `pt-BR-FranciscaNeural`, em português do Brasil. Nas versões aprovadas das aulas 1 e 2, a síntese usou `edge-tts`, `rate="+0%"`, tom e volume padrão. Preservar essa voz nas próximas aulas, salvo nova orientação. Confirmar a disponibilidade do sintetizador no ambiente antes de prometer locução.

Sincronizar legendas integrais à fala, em blocos legíveis de até duas linhas. Ajustar o roteiro e as pausas para a duração aprovada, sem acelerar artificialmente a voz. O modelo de 20 s é um teste sem áudio; os renderizadores incluídos exportam vídeo sem áudio e não fazem síntese nem mixagem. Uma aula narrada exige essas etapas adicionais e conferência do MP4 final.



## 2. Regras permanentes
1. Não inserir números de slides, nomes de cenas, contadores ou etiquetas de produção nos cantos do vídeo. Controles e códigos de frame pertencem ao catálogo de consulta.
2. Preservar entidades nas transições. Transformar o mesmo objeto antes de substituir a composição inteira.
3. Manter um foco principal por instante: título OU ação da interface OU consequência.
4. Usar tipografia grande para a ideia principal e reduzir o texto antes de reduzir a fonte.
5. Fazer o cursor apontar para a posição real do alvo depois das transformações da câmera.
6. Mostrar uma causa antes da reação: aproximação, breve estabilização, clique, resposta.
7. Usar luz, sombra, cor, máscara e desfoque para explicar hierarquia; não aplicá-los indiscriminadamente.
8. Conservar a legibilidade durante a pausa de leitura. Movimentos rápidos precisam terminar antes da leitura essencial.
9. Deixar a conclusão permanecer tempo suficiente para ser lida.
10. Não confundir retenção com agitação constante. Alternar surpresa, ação e repouso.
11. Priorizar aprendizagem sem culpabilização no BeSafe. Mostrar como verificar e agir.
12. Usar dados fictícios nos exemplos de mensagens, Gmail e aplicativos; não reproduzir conversas privadas.
13. Não inventar interfaces, recursos de ferramenta, resultados de renderização ou conteúdo de vídeos inacessíveis.
14. Não reaproveitar imagens de portfólios como ativos da aula. Usar o mecanismo visual como referência e produzir o conteúdo próprio.

O documento original BESAFE_REGRAS_MOTION_TRANSICOES.md permanece como histórico completo. Em conflito, prevalecer instruções explícitas recentes do usuário. Os valores numéricos abaixo são padrões editoriais propostos para BeSafe, não medições universais dos vídeos pesquisados.



## 4. Composição, ritmo e continuidade
### Escala gráfica sugerida
Em 1920 × 1080, começar com títulos de 110–180 px, destaques de 72–120 px e texto essencial de 40–64 px. Em outras resoluções, usar escala proporcional e conferir a leitura real. Texto secundário pode ser menor quando não participa da instrução. Evitar mais de duas famílias tipográficas.

Usar margens de composição de aproximadamente 6%; adaptar às áreas ocupadas pelos controles da plataforma. Não colocar conteúdo crítico encostado na borda. Paleta inicial do teste: fundo petróleo, superfície marfim, destaque menta e acento dourado; adaptar à identidade confirmada do projeto.

### Ritmo de 20 segundos
| Intervalo | Função | Operação |
| --- | --- | --- |
| 0–2,5 s | Gancho | Pergunta curta e objeto em destaque |
| 2,5–6,5 s | Contexto | Aproximar a interface e mostrar o problema |
| 6,5–11,5 s | Transformação | Cursor inicia a ação; objetos mantêm identidade |
| 11,5–15 s | Consequência | Dar espaço para perceber a diferença |
| 15–20 s | Aprendizagem | Concluir com uma ação clara e pausa |

A duração depende da carga de leitura. Planejar uma mudança significativa a cada 2–4 segundos como ponto de partida, sem inserir cortes só para atingir uma contagem.

### Continuidade técnica
- Guardar x, y, largura, altura, rotação, opacidade, escala, cor, raio e ordem de desenho por entidade.
- Calcular o estado em função de t. Não acumular deslocamento a cada requestAnimationFrame.
- Para 30 fps e 20 s, produzir índices 0…599, t = índice / 30.
- Fixar sementes de aleatoriedade; aguardar fontes e imagens antes de capturar.
- Interpolar câmera e objeto no mesmo sistema de coordenadas.
- Derivar posição do cursor do retângulo transformado do alvo; não usar coordenadas antigas.
- Compartilhar a transformação de máscara, highlight e alvo.
- Evitar desaparecimento de um objeto em um frame e reaparecimento em outro lugar sem transição.
- Considerar match cut quando objetos diferentes compartilham forma, direção e intenção; documentar a troca de identidade.

### Representação neutra
Usar um contrato JSON com: project, output, palette, typography, assets, entities, beats, camera, actions, holds, audio, invariants e evidence.
Cada beat deve informar start, end, objective, persistent_entities, entering_entities, focus_target, action, transition e reading_hold.
A mesma especificação orienta Canvas, AE ou prompts; a implementação precisa ser adaptada ao que cada ferramenta realmente suporta.
