import torch
import cv2
import numpy as np

# ------------------------------------------------------------------
#  PARTE 1: LÓGICA DE DETECÇÃO (Seu código original)
# ------------------------------------------------------------------

# Carregar o modelo YOLOv5 pré-treinado
# (Isso pode exigir conexão com a internet na primeira execução)
try:
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
except Exception as e:
    print(f"Erro ao carregar o modelo YOLOv5: {e}")
    print("Verifique sua conexão com a internet ou o repositório 'ultralytics/yolov5'.")
    exit()


# ---------------------------
#   Função: Caixa Estilizada (Sua função original)
# ---------------------------
def draw_stylized_box(img, x1, y1, x2, y2, label):

    # --------------------
    # Sombra da bounding box
    # --------------------
    cv2.rectangle(
        img,
        (x1 + 4, y1 + 4),
        (x2 + 4, y2 + 4),
        (0, 0, 0),
        thickness=10 # Sombra um pouco mais sutil
    )

    # --------------------
    # Caixa principal
    # --------------------
    color = (30, 144, 255)  # azul (DodgerBlue)
    cv2.rectangle(
        img,
        (x1, y1),
        (x2, y2),
        color,
        thickness=3
    )

    # --------------------
    # Fundo translúcido do texto
    # --------------------
    
    # Define o tamanho do texto para criar o retângulo do fundo
    (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_DUPLEX, 0.6, 2)
    
    # Coordenadas do fundo do texto
    text_bg_x1 = x1
    text_bg_y1 = y1 - text_height - baseline - 4 # Um pouco acima da caixa
    text_bg_x2 = x1 + text_width + 16 # (8px de padding de cada lado)
    text_bg_y2 = y1
    
    # Desenha o retângulo em uma cópia da imagem (overlay)
    overlay = img.copy()
    cv2.rectangle(
        overlay,
        (text_bg_x1, text_bg_y1),
        (text_bg_x2, text_bg_y2),
        color,
        thickness=-1
    )
    alpha = 0.5 # Nível de transparência
    img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

    # --------------------
    # Texto (label + confiança)
    # --------------------
    cv2.putText(
        img,
        label,
        (x1 + 8, y1 - 7), # Posição do texto (com padding)
        cv2.FONT_HERSHEY_DUPLEX,
        0.6,
        (255, 255, 255), # Branco
        2
    )

    return img


# ---------------------------
#   Processamento da Imagem (Sua função, levemente modificada)
#   Agora ela recebe o OBJETO da imagem, não o caminho
# ---------------------------
def detect_and_draw_objects(img):
    """
    Executa a detecção YOLOv5 em uma imagem (array NumPy) e 
    desenha as caixas estilizadas.
    """
    
    # A imagem recebida já está em BGR (do OpenCV)
    # Precisamos convertê-la para RGB para o modelo YOLO (PyTorch)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detectar objetos
    results = model(img_rgb)
    df = results.pandas().xyxy[0]

    # Criar uma cópia da imagem original (BGR) para desenhar
    img_to_draw = img.copy()

    # Renderização customizada
    for _, row in df.iterrows():
        x1, y1, x2, y2 = map(int, [row.xmin, row.ymin, row.xmax, row.ymax])
        label = f"{row['name']}  {row['confidence']:.2f}"

        img_to_draw = draw_stylized_box(img_to_draw, x1, y1, x2, y2, label)

    # Exibir janela interativa
    cv2.imshow("Detecções - Visual Computacional", img_to_draw)
    print("\nPressione qualquer tecla na janela da imagem para fechar e voltar ao menu...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return df

# ------------------------------------------------------------------
#  PARTE 2: NOVAS FUNÇÕES DE TRANSFORMAÇÃO GEOMÉTRICA
# ------------------------------------------------------------------

def translate_image(image, tx, ty):
    """Translada a imagem por (tx, ty) pixels."""
    h, w = image.shape[:2]
    # Matriz de Translação
    M = np.float32([[1, 0, tx],
                    [0, 1, ty]])
    # Aplica a translação
    translated = cv2.warpAffine(image, M, (w, h))
    return translated

def rotate_image(image, angle, center=None, scale=1.0):
    """Rotaciona a imagem pelo 'angle' (em graus)."""
    h, w = image.shape[:2]
    
    # Se o centro não for especificado, usa o centro da imagem
    if center is None:
        center = (w // 2, h // 2)
        
    # Matriz de Rotação
    M = cv2.getRotationMatrix2D(center, angle, scale)
    
    # Aplica a rotação
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def scale_image(image, fx, fy):
    """Escalona a imagem pelos fatores fx (largura) e fy (altura)."""
    # INTER_LINEAR é um bom padrão para aumentar ou diminuir
    scaled = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    return scaled

# ------------------------------------------------------------------
#  PARTE 3: EXECUÇÃO PRINCIPAL (MENU INTERATIVO)
# ------------------------------------------------------------------

def main():
    image_path = "imgs/Img_Teste_1.jpg" # O caminho da sua imagem de teste
    
    original_img = cv2.imread(image_path)
    
    if original_img is None:
        print(f"Erro: Não foi possível carregar a imagem em '{image_path}'.")
        print("Verifique se o caminho está correto e se o arquivo existe.")
        return

    while True:
        print("\n--- MENU DE TRANSFORMAÇÃO E DETECÇÃO ---")
        print("Escolha uma operação para aplicar ANTES da detecção:")
        print("1. Translação (Mover 100px direita, 50px baixo)")
        print("2. Rotação (45 graus)")
        print("3. Escalonamento (Zoom de 1.5x)")
        print("--- Transformações Compostas ---")
        print("4. [Composta 1] Rotacionar (30°) e Transladar (50, 50)")
        print("5. [Composta 2] Rotacionar (-60°) e Transladar (-80, 40)")
        print("6. [Composta 3] Rotacionar (90°) e Transladar (100, -50)")
        print("-----------------------------------")
        print("7. APENAS Detecção (Imagem Original)")
        print("0. Sair")

        choice = input("Digite sua escolha: ")
        
        transformed_img = None

        if choice == '1':
            print("Aplicando Translação...")
            transformed_img = translate_image(original_img, 100, 50)
            
        elif choice == '2':
            print("Aplicando Rotação...")
            transformed_img = rotate_image(original_img, 45)
            
        elif choice == '3':
            print("Aplicando Escalonamento...")
            # Nota: O escalonamento muda o tamanho da imagem.
            # O YOLO pode ter dificuldade se a imagem ficar muito grande ou pequena.
            transformed_img = scale_image(original_img, 1.5, 1.5)

        elif choice == '4':
            print("Aplicando Composta 1 (Rot+Trans)...")
            temp_img = rotate_image(original_img, 30)
            transformed_img = translate_image(temp_img, 50, 50)
            
        elif choice == '5':
            print("Aplicando Composta 2 (Rot+Trans)...")
            temp_img = rotate_image(original_img, -60)
            transformed_img = translate_image(temp_img, -80, 40)
            
        elif choice == '6':
            print("Aplicando Composta 3 (Rot+Trans)...")
            temp_img = rotate_image(original_img, 90)
            transformed_img = translate_image(temp_img, 100, -50)
            
        elif choice == '7':
            print("Processando Imagem Original...")
            transformed_img = original_img.copy() # Usa uma cópia por segurança
            
        elif choice == '0':
            print("Saindo...")
            break
            
        else:
            print("Escolha inválida. Tente novamente.")
            continue
            
        # Se uma escolha válida foi feita, processa a imagem
        if transformed_img is not None:
            print("Iniciando detecção de objetos na imagem transformada...")
            detections = detect_and_draw_objects(transformed_img)
            
            print("\nDETECÇÕES ENCONTRADAS (na imagem transformada):")
            if detections.empty:
                print("Nenhum objeto detectado.")
            else:
                print(detections)

# Executa o programa principal
if __name__ == "__main__":
    main()