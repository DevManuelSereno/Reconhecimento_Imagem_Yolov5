# Projeto de Detecção de Objetos com YOLOv5

Este é um projeto simples em Python que utiliza o modelo **YOLOv5s** para realizar a detecção de objetos em tempo real em imagens estáticas.

O script `main.py` carrega uma imagem de uma pasta local, a processa usando o modelo YOLOv5 (carregado via PyTorch Hub), imprime as detecções encontradas no console e, por fim, exibe a imagem com as caixas delimitadoras (bounding boxes) e os rótulos dos objetos detectados.

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **YOLOv5 (Ultralytics)**: O modelo de detecção de objetos.
* **PyTorch**: A biblioteca de deep learning usada para carregar e executar o modelo.
* **OpenCV (cv2)**: Utilizado para ler, processar e exibir as imagens.
* **Pandas**: Usado para formatar e exibir os resultados da detecção de forma estruturada.
* **NumPy**: Dependência principal para manipulação de arrays.

## ⚙️ Instalação

Siga estes passos para configurar e rodar o projeto localmente.

1.  **Clone o repositório** (ou baixe os arquivos):
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    cd SEU-REPOSITORIO
    ```

2.  **(Recomendado) Crie um Ambiente Virtual:**
    ```bash
    # No Windows
    python -m venv venv
    .\venv\Scripts\activate

    # No macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    A maneira mais fácil é instalar o pacote `yolov5`, que automaticamente cuidará de baixar o `PyTorch`, `OpenCV`, `Pandas` e outras bibliotecas necessárias.

    ```bash
    pip install yolov5
    ```

## ▶️ Como Executar

1.  Adicione as imagens que você deseja analisar dentro da pasta `imgs/`.

2.  Abra o arquivo `main.py` e atualize a variável `image_path` para apontar para a imagem desejada. (Lembre-se de usar um **caminho relativo**):

    ```python
    # Caminho da imagem que deseja processar
    image_path = 'imgs/Img_Teste_1.jpg'
    ```

3.  Execute o script a partir do seu terminal:
    ```bash
    python main.py
    ```

4.  **Resultados:**
    * O console exibirá um DataFrame do Pandas com as coordenadas e a confiança de cada objeto detectado.
    * Uma nova janela (do OpenCV) será aberta, mostrando sua imagem com as detecções desenhadas.

## ⚠️ Solução de Problemas (Troubleshooting)

Durante o desenvolvimento, alguns erros comuns podem aparecer:

### 1. `FileNotFoundError: ... hubconf.py`

* **Problema:** O cache do PyTorch Hub está corrompido ou incompleto.
* **Solução:** Force o PyTorch a baixar os arquivos do modelo novamente adicionando `force_reload=True` na linha de carregamento do modelo.

    ```python
    # Linha original
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    
    # Linha corrigida (para rodar uma vez)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, force_reload=True)
    ```
    Alternativamente, delete manualmente a pasta `hub` dentro de `C:\Users\SEU-USUARIO\.cache\torch\`.

### 2. `SyntaxError: (unicode error) 'unicodeescape'`

* **Problema:** Você está usando um caminho absoluto no Windows e o Python está interpretando as barras invertidas (`\`) como caracteres de escape (ex: `C:\Users\...`).
* **Solução:** Sempre use "raw strings" (adicionando um `r` antes das aspas) ou use barras normais (`/`).

    ```python
    # Errado
    image_path = 'C:\Users\...\imagem.jpg'
    
    # Correto (Raw String)
    image_path = r'C:\Users\...\imagem.jpg'
    
    # Correto (Barras normais)
    image_path = 'C:/Users/.../imagem.jpg'
    ```

