import cv2
import numpy as np
import os
from tkinter import Tk, filedialog

def select_folder():
    # Cria uma interface para escolher a pasta
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title="Selecione a pasta com as imagens")
    return folder_selected

def apply_gradient(image):
    # Obtenha as dimensões da imagem
    height, width = image.shape
    
    # Crie um gradiente horizontal (ajuste conforme necessário)
    gradient = np.tile(np.linspace(0, 155, width, dtype=np.uint8), (height, 1))

    # Realize a soma com o gradiente (certifique-se de usar uma cópia para não alterar a imagem original)
    result = cv2.add(image, gradient)
    return result

def process_images_in_folder(folder_path):
    # Crie uma pasta para salvar os resultados
    output_folder = os.path.join(folder_path, "imagens_com_gradiente")
    os.makedirs(output_folder, exist_ok=True)

    # Itera sobre cada arquivo na pasta
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            # Carrega a imagem em escala de cinza
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Aplica o gradiente e salva o resultado
            result_image = apply_gradient(image)
            output_path = os.path.join(output_folder, f"gradiente_{filename}")
            cv2.imwrite(output_path, result_image)
            print(f"Imagem processada e salva: {output_path}")

# Fluxo principal
folder_path = select_folder()
if folder_path:
    process_images_in_folder(folder_path)
    print("Processamento concluído!")
else:
    print("Nenhuma pasta selecionada.")
