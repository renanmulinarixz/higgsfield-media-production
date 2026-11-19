---
name: besafe-motion
description: Criar e revisar motion educativo BeSafe, aulas, vídeos de interfaces, intros e animações de logos e elementos. Usar tipografia grande, cursores, destaques e continuidade em demonstrações de Gmail, mensagens, aplicativos, segurança digital e investimentos. Adaptar HTML/Canvas/SVG local e ferramentas disponíveis, incluindo motion nativo do Higgsfield quando confirmado.
---

# BeSafe Motion

## Executar
1. Ler [direção e continuidade](references/direction.md). Identificar objetivo de aprendizagem, público, formato, duração e entidade que permanece entre beats.
2. Executar python3 scripts/capabilities.py. Escolher a rota local por padrão. Verificar capacidades reais em vez de assumir instalações.
3. Consultar [fontes e níveis de evidência](references/sources.md). Abrir assets/index.html, escolher poucos quadros relevantes e consultar as imagens individuais pelo índice. Não carregar 600 imagens no contexto de uma vez.
   Para intros, assinaturas de marca e animações de elementos, ler [logos e elementos](references/logo-elements.md) e abrir assets/pinterest-logos/index.html. Escolher estilo conforme público, finalidade e roteiro. Executar python scripts/prepare_reference_frames.py para materializar os 2.102 frames do Pinterest. Na distribuição compacta, materializar os 600 frames do modelo com python scripts/prepare_reference_frames.py --source model quando necessário.
4. Preparar um contrato de cenas a partir de assets/brief.example.json. Separar texto exato, entidades persistentes, alvo, ação, transição e pausa de leitura.
5. Copiar assets/template/motion.html para a pasta de saída do projeto. Adaptar o roteiro e os gráficos; não alterar a referência original. Expor window.motion.renderAt(t), window.motion.stateAt(t) e window.motion.duration, com t em segundos e um canvas #stage.
6. Aplicar somente [efeitos](references/effects.md) que esclarecem a ideia. Para Gmail, chat, apps e aulas de segurança, ler [interfaces BeSafe](references/interfaces.md).
7. Renderizar com node scripts/render.cjs caminho/motion.html caminho/video.mp4. O renderizador usa tempo absoluto, bloqueia rede, captura o canvas e exporta com FFmpeg. Exige Node, Playwright, Chromium e FFmpeg locais; não precisa de Higgsfield nem de APIs.
8. Se o navegador não iniciar e o projeto for Canvas autocontido confiável, usar explicitamente node scripts/render_canvas.cjs caminho/motion.html caminho/video.mp4. Exige @napi-rs/canvas local. Não renderiza DOM/SVG/CSS; métricas de fontes podem diferir. Validar pixels e leitura. Não executar HTML desconhecido nessa rota; VM não é fronteira de segurança. Verificar com python3 scripts/check_media.py caminho/video.mp4 --duration 20 --fps 30 --frames 600 (adaptar números à duração escolhida). Extrair quadros com python3 scripts/extract_frames.py caminho/video.mp4 caminho/frames.
9. Inspecionar vídeo inteiro e quadros das fronteiras, cliques e conclusão. Aplicar [qualidade](references/quality.md). Não confundir checks automáticos com inspeção visual.
10. Para aulas narradas, aplicar a voz aprovada e as legendas descritas em [direção](references/direction.md). Os renderizadores incluídos exportam vídeo sem áudio; sintetizar, sincronizar e mixar a locução em etapa adicional. Entregar o MP4 realmente produzido como arquivo/preview nativo quando disponível, fonte editável e limitações materiais. Confirmar instalação/execução de ferramenta somente mediante evidência.

Executar scripts a partir desta pasta ou resolver seus caminhos absolutos. Não escrever resultados futuros dentro da skill. Se faltar dependência, preservar fontes e dizer exatamente qual etapa não foi executada.

## Preservar
- Proibir números de slide, etiquetas de cena e informações de produção nos cantos do vídeo.
- Manter identidade e trajetória dos objetos; mover a câmera e ampliar a mesma janela.
- Exibir uma ação focal por instante. Priorizar título, interação ou consequência, com pausa para leitura.
- Derivar cursor, máscara e destaque da posição transformada do alvo.
- Preservar texto exato e sentido. Evitar efeitos que escondem o que a aula ensina.
- Usar dados fictícios e domínios reservados nos exemplos.
- Ensinar segurança sem culpabilizar; não tratar cadeados ou checks como prova absoluta.
- No teste de investimentos, preservar que diversificar não garante lucro nem elimina perdas.
- Não prometer retenção, precisão ou recursos de ferramenta apenas pela estética de uma referência.

## Adaptar ferramentas
Ler [adaptações](references/adapters.md) somente para a rota escolhida.
Para Higgsfield, ler [motion nativo](references/higgsfield-native.md) antes de escolher qualquer módulo. Diferenciar Vibe Motion/AI Motion Design no navegador, editorial motion, modelos generativos, Canvas e AI Motion Designer no Adobe. Não substituir motion editável silenciosamente por presets de câmera ou vídeo generativo. Descobrir ferramentas/esquemas atuais, preços e acesso antes de executar.

Astra/Codex planeja e escreve código; o renderizador produz pixels. After Effects/Premiere exigem acesso ao aplicativo correto. Não instalar integração desktop dentro de um sandbox remoto.

## Consultar o acervo
- assets/pinterest-logos/index.html: oito referências de logos e elementos, folhas de contato e navegação por frame após materialização.
- assets/pinterest-logos/manifest.json: PTS por frame, fases editoriais, origem, hash e limites da inspeção. Cada pin inclui frames.zip e contact.jpg.
- assets/index.html: catálogo offline com slider e navegação por quadro.
- assets/frames/manifest.json: 600 frames do modelo próprio, índice e timestamp.
- assets/frames/frame-000000.jpg até frame-000599.jpg: todos os frames a 30 fps, 1440×810, JPEG q=3.
- assets/model.mp4: original de 20 segundos; comparar fluidez no vídeo.
- assets/external-sources.json e assets/external/: 12 registros externos, 9 com imagem local; autoria, tempo e disponibilidade explícitos.
- [Fontes](references/sources.md): links dos quatro vídeos do usuário, analisados automaticamente; não há prints internos deles. Não inventar frames nem chamar análise automática de visualização direta.

Usar materiais externos para estudar mecanismos; produzir conteúdo próprio para as aulas. Avaliar referências por adequação pedagógica.

## Expandir
Adicionar um efeito com propósito, implementação por capacidade e critério observável de qualidade.
Adicionar referências com URL, autor, nicho, tipo de evidência, timestamp conhecido, mecanismo transferível e limite da análise.
Atualizar o adaptador quando a interface/documentação mudar. Manter a entrada curta e detalhes em referências.

Consultar [validação e limites desta versão](references/validation.md) quando precisar distinguir roteiro, renderização e inspeção de ferramenta. Para as novas referências, consultar também os limites registrados em references/logo-elements.md.
