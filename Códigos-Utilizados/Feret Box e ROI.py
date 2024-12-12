!pip install PyDrive

import os
import numpy as np
import cv2
from zipfile import ZipFile
from google.colab import files
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Autenticação do PyDrive
from google.colab import auth
auth.authenticate_user()

from oauth2client.client import GoogleCredentials
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# ID da pasta do Google Drive
folder_id = "1W6Mo35WBthJ2d64l79Fo7h06e0vDfub9"

# Pasta para salvar as imagens baixadas e processadas
input_folder = "drive_images"
feret_folder = "feret_results6"
cropped_folder = "cropped_results6"
os.makedirs(input_folder, exist_ok=True)
os.makedirs(feret_folder, exist_ok=True)
os.makedirs(cropped_folder, exist_ok=True)

# Função para baixar imagens do Google Drive
def download_images_from_drive():
    print("Listando arquivos na pasta do Google Drive...")
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

    image_paths = []
    for file in file_list:
        if file['mimeType'].startswith('image/'):
            print(f"Baixando {file['title']}...")
            file_path = os.path.join(input_folder, file['title'])
            file.GetContentFile(file_path)
            image_paths.append(file_path)

    return image_paths

# Função para aplicar o Feret Box e cortar a imagem
def apply_feret_box_and_cut(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return

    y_indices, x_indices = np.where(image > 0)  # Pega os pixels do objeto
    if not len(x_indices):
        print(f"Nenhum objeto encontrado na imagem: {image_path}")
        return

    x_min, x_max = np.min(x_indices), np.max(x_indices)
    y_min, y_max = np.min(y_indices), np.max(y_indices)

    # Criar a imagem com o Feret Box
    output_image_feret = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.rectangle(output_image_feret, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
    
    # Salvar a imagem com o Feret Box
    feret_result_path = os.path.join(feret_folder, "feret_" + os.path.basename(image_path))
    cv2.imwrite(feret_result_path, output_image_feret)

    # Cortar a região da imagem dentro do Feret Box
    cropped_image = image[y_min:y_max, x_min:x_max]

    # Converter a imagem cortada para colorido para visualização
    output_image_cropped = cv2.cvtColor(cropped_image, cv2.COLOR_GRAY2BGR)
    
    # Salvar a imagem cortada
    cropped_result_path = os.path.join(cropped_folder, "cropped_" + os.path.basename(image_path))
    cv2.imwrite(cropped_result_path, output_image_cropped)

# Função para compactar os resultados
def zip_results(folder, zip_name):
    zip_path = f"{folder}.zip"
    with ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder))
    return zip_path

# Fluxo principal
if __name__ == "__main__":
    print("Baixando imagens do Google Drive...")
    image_paths = download_images_from_drive()

    if not image_paths:
        print("Nenhuma imagem encontrada.")
    else:
        print("Aplicando Feret Box e cortando as imagens...")
        for image_path in image_paths:
            apply_feret_box_and_cut(image_path)

        print("Compactando resultados com Feret Box...")
        feret_zip_path = zip_results(feret_folder, "feret_results")

        print("Compactando resultados cortados...")
        cropped_zip_path = zip_results(cropped_folder, "cropped_results")

        print("Baixando arquivo ZIP com as imagens do Feret Box...")
        files.download(feret_zip_path)

        print("Baixando arquivo ZIP com as imagens cortadas...")
        files.download(cropped_zip_path)

    print("Processo concluído.")
