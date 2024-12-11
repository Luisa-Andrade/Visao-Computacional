from PIL import Image
import os

def process_images(input_folder, output_folder):
    # Certifique-se de que a pasta de saída existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Itera por todos os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        # Garante que o arquivo seja uma imagem
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            # Caminho completo da imagem
            file_path = os.path.join(input_folder, filename)
            
            # Abre a imagem e converte para escala de cinza
            with Image.open(file_path) as img:
                gray_image = img.convert('L')  # Converte para escala de cinza
                
                # Aplica o limiar binário
                binary_image = gray_image.point(lambda x: 255 if x > 127 else 0, '1')
                
                # Caminho para salvar a imagem processada
                output_path = os.path.join(output_folder, filename)
                
                # Salva a imagem binária
                binary_image.save(output_path)
                print(f"Processado: {filename}")
    
    print("Todas as imagens foram processadas!")

# Define as pastas de entrada e saída
input_folder = r'C:\Aumentada-Tenis'
output_folder =r'C:\Users\João Vitor\Desktop\VISAO COMPUTACIONAL\SEGMENTACAO\TENIS\NO CODIGO'

# Chama a função
process_images(input_folder, output_folder)
