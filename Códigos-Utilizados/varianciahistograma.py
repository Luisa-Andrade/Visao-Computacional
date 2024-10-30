from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def calcular_variancia_histograma(imagem):
    # Converter a imagem para escala de cinza
    imagem_cinza = imagem.convert('L')
    
    # Calcular o histograma
    histograma = imagem_cinza.histogram()
    
    # Normalizar o histograma
    histograma = np.array(histograma)
    histograma_normalizado = histograma / histograma.sum()
    
    # Calcular a média do histograma
    media = np.sum(np.arange(len(histograma_normalizado)) * histograma_normalizado)
    
    # Calcular a variância
    variancia = np.sum((np.arange(len(histograma_normalizado)) - media) ** 2 * histograma_normalizado)
    
    return variancia

def calcular_variancia_para_varias_imagens():
    # Configurar a janela de seleção de arquivos
    root = tk.Tk()
    root.withdraw()
    
    # Permitir a seleção de múltiplos arquivos de imagem
    caminhos_imagens = filedialog.askopenfilenames(title="Selecione as Imagens",
                                                   filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp")])
    
    # Verificar se alguma imagem foi selecionada
    if not caminhos_imagens:
        print("Nenhuma imagem selecionada.")
        return
    
    # Calcular a variância para cada imagem e armazenar os resultados
    variancias = []
    nomes_imagens = []
    
    for caminho in caminhos_imagens:
        imagem = Image.open(caminho)
        variancia = calcular_variancia_histograma(imagem)
        variancias.append(variancia)
        nomes_imagens.append(caminho.split('/')[-1])  # Usar o nome do arquivo como rótulo
    
    # Plotar as variâncias
    plt.figure(figsize=(10, 6))
    plt.bar(nomes_imagens, variancias, color='purple')
    plt.xlabel('Imagens')
    plt.ylabel('Variância do Histograma')
    plt.title('Variância do Histograma para Cada Imagem da Classe Tênis')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Executar a função
calcular_variancia_para_varias_imagens()
