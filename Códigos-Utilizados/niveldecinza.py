from PIL import Image
import os

def rgb_to_grayscale(image_path, save_path=None):
    """
    Converte uma imagem RGB para escala de cinza e salva no diretório especificado.
    
    :param image_path: Caminho da imagem original em RGB
    :param save_path: Caminho para salvar a nova imagem em escala de cinza (opcional)
    :return: Imagem convertida em escala de cinza
    """
    try:
        # Abrir a imagem
        img = Image.open(image_path)
        
        # Converter para escala de cinza
        grayscale_img = img.convert("L")
        
        # Definir o caminho de salvamento, se não for especificado
        if save_path is None:
            file_name, file_extension = os.path.splitext(image_path)
            save_path = f"{file_name}_grayscale{file_extension}"
        
        # Salvar a nova imagem em escala de cinza
        grayscale_img.save(save_path)
        
        print(f"Imagem convertida e salva em: {save_path}")
        return grayscale_img
    
    except Exception as e:
        print(f"Erro ao converter a imagem: {e}")

def convert_images_in_folder(folder_path):
    """
    Converte todas as imagens RGB de um diretório para escala de cinza.
    
    :param folder_path: Caminho do diretório com as imagens
    """
    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder_path, filename)
            rgb_to_grayscale(image_path)

# Exemplo de uso:
# Caminho da imagem ou pasta onde estão as imagens
#image_path = r'C:\Users\João Vitor\Pictures\foto perfil.jpg'  # Para uma imagem única
folder_path = r'C:\Users\João Vitor\Desktop\Original dataset'      # Para um diretório de imagens

# Converter uma única imagem
#rgb_to_grayscale(image_path)

# Converter todas as imagens de uma pasta
convert_images_in_folder(folder_path)
