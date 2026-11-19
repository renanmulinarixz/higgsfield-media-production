## 10. Controle de qualidade
### Bloqueadores
- texto crítico errado, cortado ou ilegível;
- cursor e destaque desalinhados;
- gráfico que comunica informação falsa;
- objeto que salta de posição sem intenção;
- interface exibindo dados privados;
- frames vazios, dependências online na versão offline, duração incorreta;
- chamada de vídeo final sem arquivo renderizado;
- promessa de recurso ou ferramenta sem confirmação.

### Critérios de aceitação
1. Entender a ideia principal sem áudio.
2. Identificar o foco em miniatura.
3. Conferir abertura, fim, fronteiras de beat e clique quadro a quadro.
4. Validar contagem, resolução, fps e duração com ffprobe.
5. Decodificar o arquivo final inteiro para detectar erro de mídia.
6. Verificar fontes carregadas e nenhum recurso de rede na versão offline.
7. Conferir a conclusão e o tempo de leitura em tela reduzida.
8. Comparar edição solicitada antes/depois e confirmar o que deve persistir.

Não confundir testes estruturais com aprovação visual. O teste atual foi exportado e inspecionado na produção anterior; o acervo desta etapa foi extraído do MP4 final.

Comandos de referência para o ambiente local:
    ffprobe -v error -show_streams -show_format -of json video.mp4
    ffmpeg -v error -i video.mp4 -f null -
    ffmpeg -i video.mp4 -fps_mode passthrough -start_number 0 frames/frame-%06d.png

Para fontes VFR, registrar PTS por frame em vez de assumir índice/fps. Não interpolar para 30 fps ao catalogar um original variável sem registrar essa transformação.
