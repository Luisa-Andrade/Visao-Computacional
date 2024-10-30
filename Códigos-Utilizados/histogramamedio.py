import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from tkinter import filedialog
from tkinter import Tk

# Função para calcular o histograma de uma imagem em escala de cinza
def calculate_histogram(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    return histogram

# Função para selecionar a pasta com as imagens da classe
def select_folder():
    root = Tk()
    root.withdraw()  # Oculta a janela principal
    folder_path = filedialog.askdirectory(title="Selecione a pasta com as imagens da classe")
    return folder_path

# Função para calcular o histograma médio da classe de imagens
def average_histogram(folder_path):
    histograms = []
    image_count = 0

    # Percorre todas as imagens na pasta
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            img_path = os.path.join(folder_path, filename)
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Carrega a imagem em escala de cinza
            if image is not None:
                histogram = calculate_histogram(image)
                histograms.append(histogram)
                image_count += 1

    # Calcula o histograma médio
    if image_count > 0:
        avg_histogram = sum(histograms) / image_count
    else:
        print("Nenhuma imagem encontrada na pasta selecionada.")
        return None

    return avg_histogram

# Seleciona a pasta com as imagens e calcula o histograma médio
folder_path = select_folder()
avg_histogram = average_histogram(folder_path)

# Exibe o histograma médio
if avg_histogram is not None:
    plt.plot(avg_histogram, color='gray')
    plt.title('Histograma Médio da Classe Tênis')
    plt.xlabel('Intensidade de Pixel')
    plt.ylabel('Frequência Média')
    plt.show()
