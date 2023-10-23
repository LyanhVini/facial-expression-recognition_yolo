# facial-expression-recognition_yolo
Este repositório contém um modelo de reconhecimento de expressões faciais baseado na poderosa arquitetura YOLOv8 (You Only Look Once version 8). O modelo é treinado para detectar e classificar expressões faciais em tempo real, tornando-o ideal para aplicações de análise de emoções, segurança e interação humano-computador.

## Topologia

- [Reconhecimento de expressão facial](https://github.com/LyanhVini/facial-expression-recognition_yolo/) - `Modelo de Inteligência Artificial parra reconhecimento de expressões faciais`
- [data](https://github.com/LyanhVini/facial-expression-recognition_yolo/tree/main/data) - `Contém a base de dados`
    - CK+48 + Fear2013v4.zip - `base de dados utilizada -> Mesclagem da CK+ e Fear2013`
    - data.txt - `Comentário sobre a base de dados`
- [results](https://github.com/LyanhVini/facial-expression-recognition_yolo/tree/main/results) - `Contém os resultados do treinamento do modelo`
    - confusion_matrix_normalized.png - `Matrix de confusão`
    - results.png - `Métricas de avaliação de treinamento (loss, val, acc_top1 e acc_top5)`
    - results.txt  - `Comentários adicionais dos resultados`
- [models](https://github.com/LyanhVini/facial-expression-recognition_yolo/tree/main/models) - `Contém os modelos treinados`
- [README.md](https://github.com/LyanhVini/facial-expression-recognition_yolo/blob/main/README.md) - `Documentação`
- [inferenciaYOLO.py](https://github.com/LyanhVini/facial-expression-recognition_yolo/blob/main/inferenciaYOLO.py) - `Script que executa o modelo via webcam`
- [main.py](https://github.com/LyanhVini/facial-expression-recognition_yolo/blob/main/main.ipynb) - `Arquivo COLAB que realiza todo o pré-processamento, processamento, treinamento e avaliação do modelo`
