import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Adicione outros formatos se necessário
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path).convert("RGB")
            images.append(img)
    return images

def resize_images(images, size=(100, 100)):
    return [img.resize(size) for img in images]

def compute_average_image(images):
    # Converter imagens para arrays NumPy
    np_images = [np.array(img) for img in images]
    
    # Calcular a média pixel a pixel
    avg_image_array = np.mean(np_images, axis=0).astype(np.uint8)
    
    # Converter de volta para imagem PIL
    avg_image = Image.fromarray(avg_image_array)
    return avg_image

# Caminho para a pasta onde estão suas imagens
folder_path = r'C:\normalizedDataSet\Normalizada - Tenis'

# Carregar e redimensionar as imagens para o mesmo tamanho
images = load_images_from_folder(folder_path)
if images:
    resized_images = resize_images(images)

    # Calcular o protótipo médio
    avg_image = compute_average_image(resized_images)

    # Exibir a imagem protótipo médio
    plt.imshow(avg_image)
    plt.axis('off')
    plt.show()
else:
    print("Nenhuma imagem encontrada na pasta especificada.")
