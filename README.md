# Projeto de Detecção (YOLOv5) com Transformações Geométricas (OpenCV)

Este projeto demonstra a integração entre a detecção de objetos em tempo real com **YOLOv5** e as capacidades de manipulação de imagem do **OpenCV**.

O script `main.py` carrega uma imagem e apresenta um **menu interativo** no console. O usuário pode escolher aplicar diversas transformações geométricas (como translação, rotação, escalonamento e compostas) à imagem. Após a transformação, o script executa o modelo YOLOv5 na imagem *resultante*, permitindo analisar como essas transformações afetam o desempenho da detecção.

## ✨ Funcionalidades

* **Menu Interativo:** Um loop no console permite ao usuário escolher qual operação realizar.
* **Transformações Geométricas:** Funções para transladar, rotacionar e escalonar a imagem de entrada.
* **Transformações Compostas:** Aplica sequências de transformações (ex: Rotacionar + Transladar).
* **Detecção com YOLOv5:** Utiliza o modelo `yolov5s` para detectar objetos na imagem original ou na imagem já transformada.
* **Visualização Customizada:** Renderiza caixas delimitadoras (bounding boxes) estilizadas com sombra e fundo translúcido para melhor legibilidade.

## 🚀 Tecnologias Utilizadas

* **Python 3.10+** (Gerenciado via `.python-version`)
* **uv**: Gerenciador de projetos e pacotes Python extremamente rápido.
* **YOLOv5 (Ultralytics)**: O modelo de detecção de objetos.
* **PyTorch**: A biblioteca de deep learning usada para carregar e executar o modelo.
* **OpenCV (cv2)**: Utilizado para ler, processar, exibir as imagens e **realizar as transformações geométricas (warpAffine)**.
* **Pandas**: Usado para formatar e exibir os resultados da detecção de forma estruturada.
* **NumPy**: Dependência principal para manipulação de arrays.

## ⚙️ Instalação e Configuração

Este projeto utiliza o **uv** para gerenciamento de dependências e ambiente virtual, garantindo uma instalação rápida e reprodutível através dos arquivos `pyproject.toml` e `uv.lock`.

### Pré-requisitos
Certifique-se de ter o **uv** instalado. Se não tiver, instale-o com um comando (Linux/macOS) ou via PowerShell (Windows):
* **Documentação oficial do uv:** [docs.astral.sh/uv](https://docs.astral.sh/uv/)

### Passos

1.  **Clone o repositório** (ou baixe os arquivos):
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    cd SEU-REPOSITORIO
    ```

2.  **Sincronize o ambiente:**
    O comando abaixo lerá o arquivo `uv.lock`, criará o ambiente virtual (`.venv`) e instalará todas as dependências exatas necessárias.
    ```bash
    uv sync
    ```

## ▶️ Como Executar

Com o ambiente configurado pelo uv, você pode rodar o projeto de forma simplificada.

1.  **Prepare as Imagens:**
    Adicione as imagens que você deseja analisar dentro da pasta `imgs/`.

2.  **Configure o Caminho da Imagem:**
    Abra o arquivo `main.py` e, dentro da função `main()`, atualize a variável `image_path` para apontar para a imagem desejada:

    ```python
    # ---------------------------
    #     Execução principal
    # ---------------------------
    def main():
        image_path = "imgs/Img_Teste_1.jpg" # <-- ATUALIZE AQUI
        
        original_img = cv2.imread(image_path)
    # ...
    ```

3.  **Execute o Script:**
    Utilize o comando `uv run` para executar o script utilizando o ambiente virtual configurado automaticamente:
    ```bash
    uv run main.py
    ```

4.  **Interaja com o Menu:**
    * O terminal exibirá um menu de opções (Translação, Rotação, etc.).
    * Digite o número da operação desejada e pressione `Enter`.

5.  **Resultados:**
    * O console exibirá um DataFrame do Pandas com os objetos detectados *na imagem transformada*.
    * Uma nova janela (do OpenCV) será aberta, mostrando sua imagem **transformada** com as detecções desenhadas.
    * **Pressione qualquer tecla** (com a janela da imagem em foco) para fechá-la e retornar ao menu principal.
    * Escolha a opção `0` para sair do programa.

## ⚠️ Solução de Problemas (Troubleshooting)

### 1. `FileNotFoundError: ... hubconf.py` (Problemas de Cache do PyTorch)

* **Problema:** O cache do PyTorch Hub está corrompido ou incompleto.
* **Solução:** Force o PyTorch a baixar os arquivos do modelo novamente adicionando `force_reload=True` na linha de carregamento do modelo no código.

    ```python
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, force_reload=True)
    ```

### 2. `SyntaxError: (unicode error) 'unicodeescape'`

* **Problema:** Ao editar o caminho da imagem no Windows, o Python pode interpretar as barras invertidas (`\`) como escape.
* **Solução:** Use barras normais (`/`) ou raw strings (`r'...'`).

    ```python
    image_path = 'imgs/foto.jpg'      # Correto (Recomendado)
    image_path = r'imgs\foto.jpg'     # Correto (Raw String)
    ```
