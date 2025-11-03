Projeto de Detecção (YOLOv5) com Transformações Geométricas (OpenCV)
Este projeto demonstra a integração entre a detecção de objetos em tempo real com YOLOv5 e as capacidades de manipulação de imagem do OpenCV.

O script main.py carrega uma imagem e apresenta um menu interativo no console. O usuário pode escolher aplicar diversas transformações geométricas (como translação, rotação, escalonamento e compostas) à imagem. Após a transformação, o script executa o modelo YOLOv5 na imagem resultante, permitindo analisar como essas transformações afetam o desempenho da detecção.

✨ Funcionalidades
Menu Interativo: Um loop no console permite ao usuário escolher qual operação realizar.

Transformações Geométricas: Funções para transladar, rotacionar e escalonar a imagem de entrada.

Transformações Compostas: Aplica sequências de transformações (ex: Rotacionar + Transladar).

Detecção com YOLOv5: Utiliza o modelo yolov5s (via PyTorch Hub) para detectar objetos na imagem original ou na imagem já transformada.

Visualização Customizada: Renderiza caixas delimitadoras (bounding boxes) estilizadas com sombra e fundo translúcido para melhor legibilidade.

🚀 Tecnologias Utilizadas
Python 3.10+

YOLOv5 (Ultralytics): O modelo de detecção de objetos.

PyTorch: A biblioteca de deep learning usada para carregar e executar o modelo.

OpenCV (cv2): Utilizado para ler, processar, exibir as imagens e realizar as transformações geométricas (warpAffine).

Pandas: Usado para formatar e exibir os resultados da detecção de forma estruturada.

NumPy: Dependência principal para manipulação de arrays.

⚙️ Instalação
Siga estes passos para configurar e rodar o projeto localmente.

Clone o repositório (ou baixe os arquivos):

Bash

git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd SEU-REPOSITORIO
(Recomendado) Crie um Ambiente Virtual:

Bash

# No Windows
python -m venv venv
.\venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
Instale as dependências: A maneira mais fácil é instalar o pacote yolov5, que automaticamente cuidará de baixar o PyTorch, OpenCV, Pandas e outras bibliotecas necessárias.

Bash

pip install yolov5
▶️ Como Executar
Adicione as imagens que você deseja analisar dentro da pasta imgs/.

Abra o arquivo main.py e, dentro da função main(), atualize a variável image_path para apontar para a imagem desejada:

Python

# ---------------------------
#    Execução principal
# ---------------------------
def main():
    image_path = "imgs/Img_Teste_1.jpg" # <-- ATUALIZE AQUI

    original_img = cv2.imread(image_path)
# ...
Execute o script a partir do seu terminal:

Bash

python main.py
Interaja com o Menu:

O terminal exibirá um menu de opções (Translação, Rotação, etc.).

Digite o número da operação desejada e pressione Enter.

Resultados:

O console exibirá um DataFrame do Pandas com os objetos detectados na imagem transformada.

Uma nova janela (do OpenCV) será aberta, mostrando sua imagem transformada com as detecções desenhadas.

Pressione qualquer tecla (com a janela da imagem em foco) para fechá-la e retornar ao menu principal.

Escolha a opção 0 para sair do programa.

⚠️ Solução de Problemas (Troubleshooting)
Durante o desenvolvimento, alguns erros comuns podem aparecer:

1. FileNotFoundError: ... hubconf.py
Problema: O cache do PyTorch Hub está corrompido ou incompleto.

Solução: Force o PyTorch a baixar os arquivos do modelo novamente adicionando force_reload=True na linha de carregamento do modelo.

Python

# Linha original
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Linha corrigida (para rodar uma vez)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, force_reload=True)
Alternativamente, delete manualmente a pasta hub dentro de C:\Users\SEU-USUARIO\.cache\torch\.

2. SyntaxError: (unicode error) 'unicodeescape'
Problema: Você está usando um caminho absoluto no Windows e o Python está interpretando as barras invertidas (\) como caracteres de escape (ex: C:\Users\...).

Solução: Sempre use "raw strings" (adicionando um r antes das aspas) ou use barras normais (/).

Python

# Errado
image_path = 'C:\Users\...\imagem.jpg'

# Correto (Raw String)
image_path = r'C:\Users\...\imagem.jpg'

# Correto (Barras normais)
image_path = 'C:/Users/.../imagem.jpg'
