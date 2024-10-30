import cv2
import numpy as np
import os

def apply_log_transform(image_path, save_path=None):
    """
    Aplica a transformação logarítmica a uma imagem.
    
    :param image_path: Caminho da imagem original
    :param save_path: Caminho para salvar a nova imagem com transformação logarítmica (opcional)
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
        img_float = np.float32(img)
        
        # Normalizar os valores da imagem para o intervalo [0, 1]
        img_normalized = img_float / 255.0
        
        # Aplicar a transformação logarítmica
        c = 255 / np.log(1 + np.max(img_normalized))  # Constante de normalização
        log_image = c * np.log(1 + img_normalized)
        
        # Converter de volta para uint8
        log_image = np.uint8(log_image)
        
        # Definir o caminho de salvamento, se não for especificado
        if save_path is None:
            file_name, file_extension = os.path.splitext(image_path)
            save_path = f"{file_name}_log_transform{file_extension}"
        
        # Salvar a imagem com a transformação logarítmica aplicada
        cv2.imwrite(save_path, log_image)
        
        print(f"Transformação logarítmica aplicada e salva em: {save_path}")
        return log_image
    
    except Exception as e:
        print(f"Erro ao aplicar a transformação logarítmica: {e}")

def apply_log_transform_to_folder(folder_path):
    """
    Aplica a transformação logarítmica a todas as imagens de um diretório.
    
    :param folder_path: Caminho do diretório com as imagens
    """
    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder_path, filename)
            apply_log_transform(image_path)

# Exemplo de uso:
# Caminho da imagem ou pasta onde estão as imagens
#image_path = "C:/Users/João Vitor/Desktop/originalGrayDataset/Caneca1-dia-in-fundo7_grayscale.jpg"  # Para uma imagem única
folder_path = r'C:\originalGrayDataset'      # Para um diretório de imagens

# Aplicar a função logarítmica a uma única imagem
#apply_log_transform(image_path)

# Aplicar a função logarítmica a todas as imagens de uma pasta
apply_log_transform_to_folder(folder_path)
