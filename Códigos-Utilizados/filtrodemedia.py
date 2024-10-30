import cv2
import numpy as np
import os

def apply_mean_filter(image_path, kernel_size=5, save_path=None):
    """
    Aplica o filtro da média a uma imagem usando convolução com uma máscara de tamanho especificado.
    
    :param image_path: Caminho da imagem original
    :param kernel_size: Tamanho do kernel (máscara) usado no filtro. Padrão é 5x5.
    :param save_path: Caminho para salvar a nova imagem com o filtro aplicado (opcional)
    :return: Imagem filtrada
    """
    try:
        # Ler a imagem
        img = cv2.imread(image_path)
        
        # Verificar se a imagem foi lida corretamente
        if img is None:
            print(f"Erro ao ler a imagem: {image_path}")
            return
        
        # Criar uma máscara (kernel) de média com o tamanho especificado (5x5, por padrão)
        kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
        
        # Aplicar o filtro da média usando convolução
        filtered_image = cv2.filter2D(img, -1, kernel)
        
        # Definir o caminho de salvamento, se não for especificado
        if save_path is None:
            file_name, file_extension = os.path.splitext(image_path)
            save_path = f"{file_name}_mean_filter{file_extension}"
        
        # Salvar a imagem filtrada
        cv2.imwrite(save_path, filtered_image)
        
        print(f"Filtro da média aplicado e imagem salva em: {save_path}")
        return filtered_image
    
    except Exception as e:
        print(f"Erro ao aplicar o filtro da média: {e}")

def apply_mean_filter_to_folder(folder_path, kernel_size=5):
    """
    Aplica o filtro da média a todas as imagens de um diretório usando convolução com uma máscara de tamanho especificado.
    
    :param folder_path: Caminho do diretório com as imagens
    :param kernel_size: Tamanho do kernel (máscara) usado no filtro. Padrão é 5x5.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder_path, filename)
            apply_mean_filter(image_path, kernel_size)

# Exemplo de uso:
# Caminho da imagem ou pasta onde estão as imagens
#image_path = "caminho/para/sua/imagem.jpg"  # Para uma imagem única
folder_path = r'C:\originalGrayDataset'      # Para um diretório de imagens

# Aplicar o filtro da média a uma única imagem
#apply_mean_filter(image_path)

# Aplicar o filtro da média a todas as imagens de uma pasta
apply_mean_filter_to_folder(folder_path)
