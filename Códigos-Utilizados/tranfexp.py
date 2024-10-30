import cv2
import numpy as np
import os

def apply_exponential_transform(image_path, gamma=1.0, save_path=None):
    """
    Aplica a transformação exponencial (correção gama) a uma imagem.
    
    :param image_path: Caminho da imagem original
    :param gamma: Valor de gama para a transformação exponencial. O valor padrão é 1.0.
    :param save_path: Caminho para salvar a nova imagem com transformação exponencial (opcional)
    :return: Imagem transformada
    """
    try:
        # Ler a imagem
        img = cv2.imread(image_path)
        
        # Verificar se a imagem foi lida corretamente
        if img is None:
            print(f"Erro ao ler a imagem: {image_path}")
            return
        
        # Converter para float32 para evitar overflow durante a transformação
        img_float = np.float32(img) / 255.0
        
        # Aplicar a transformação exponencial (correção gama)
        exponential_image = np.power(img_float, gamma)
        
        # Normalizar os valores para a faixa [0, 255] e converter de volta para uint8
        exponential_image = np.uint8(exponential_image * 255)
        
        # Definir o caminho de salvamento, se não for especificado
        if save_path is None:
            file_name, file_extension = os.path.splitext(image_path)
            save_path = f"{file_name}_exponential_transform{file_extension}"
        
        # Salvar a imagem com a transformação exponencial aplicada
        cv2.imwrite(save_path, exponential_image)
        
        print(f"Transformação exponencial aplicada e salva em: {save_path}")
        return exponential_image
    
    except Exception as e:
        print(f"Erro ao aplicar a transformação exponencial: {e}")

def apply_exponential_transform_to_folder(folder_path, gamma=1.0):
    """
    Aplica a transformação exponencial a todas as imagens de um diretório.
    
    :param folder_path: Caminho do diretório com as imagens
    :param gamma: Valor de gama para a transformação exponencial
    """
    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder_path, filename)
            apply_exponential_transform(image_path, gamma)

# Exemplo de uso:
# Caminho da imagem ou pasta onde estão as imagens
#image_path = "caminho/para/sua/imagem.jpg"  # Para uma imagem única
folder_path = r'C:\originalGrayDataset'      # Para um diretório de imagens

# Aplicar a função exponencial a uma única imagem
#apply_exponential_transform(image_path, gamma=1.5)

# Aplicar a função exponencial a todas as imagens de uma pasta
apply_exponential_transform_to_folder(folder_path, gamma=1.5)
