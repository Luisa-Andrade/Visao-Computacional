import numpy as np
from skimage import exposure, io, img_as_ubyte
import os
import tkinter as tk
from tkinter import filedialog

# Função para selecionar imagens
def select_images():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    file_paths = filedialog.askopenfilenames(
        title="Selecione as imagens",
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.tif")],
        initialdir=os.getcwd()
    )
    return file_paths

# Função para equalizar histograma e salvar imagem
def equalize_and_save_images(image_paths, output_dir="equalized_images"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Cria a pasta de saída, se não existir

    for img_path in image_paths:
        # Carrega a imagem na sua forma original (colorida, se for o caso)
        img = io.imread(img_path)
        
        # Aplica a equalização de histograma
        img_eq = exposure.equalize_hist(img)
        
        # Converte a imagem equalizada para uint8
        img_eq_uint8 = img_as_ubyte(img_eq)
        
        # Salva a imagem equalizada na pasta de saída
        file_name = os.path.basename(img_path)
        save_path = os.path.join(output_dir, f"equalized_{file_name}")
        io.imsave(save_path, img_eq_uint8)
        print(f"Imagem equalizada salva em: {save_path}")

# Selecionar as imagens
img_paths = select_images()

# Processar e salvar imagens equalizadas
if img_paths:
    equalize_and_save_images(img_paths)
else:
    print("Nenhuma imagem selecionada.")
