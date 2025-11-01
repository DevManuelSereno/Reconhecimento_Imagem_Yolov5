import torch
import cv2
import numpy as np

# Carregar o modelo YOLOv5 pré-treinado (caminho pode variar)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Função para processar a imagem
def process_image(image_path):
    # Ler a imagem
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Realizar a detecção
    results = model(img)

    # Mostrar resultados
    results.print()  # Imprime resultados no console
    results.show()   # Mostra a imagem com as detecções

    # Obter as detecções como um DataFrame
    df = results.pandas().xyxy[0]  # xyxy format (xmin, ymin, xmax, ymax)

    return df

# Caminho da imagem que deseja processar
image_path = 'imgs/Img_Teste_1.jpg'

# Processar a imagem e obter resultados
detections = process_image(image_path)

# Exibir as detecções
print(detections)
