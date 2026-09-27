import matplotlib.pyplot as plt
import numpy as np

def generar_matriz_polar(categorias, radios):
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')

    num_cat = len(categorias)
    angulos = np.linspace(0, 2 * np.pi, num_cat, endpoint=False)

    for r in radios:
        ax.plot(angulos, [r]*num_cat, linestyle='--', color='#38BDF8', alpha=0.7)

    ax.set_xticks(angulos)
    ax.set_xticklabels(categorias, color='#F8FAFC', fontsize=9)
    ax.grid(True, color='#1E293B')
    
    plt.title("Visualizador Radial Paramétrico", color='#F8FAFC', pad=20)
    plt.savefig("matriz_polar.png", dpi=300, facecolor=fig.get_facecolor())
    plt.show()

# Ejecución
categorias = ["Fase A", "Fase B", "Fase C", "Fase D"]
radios = [1.0, 2.0, 3.0]
generar_matriz_polar(categorias, radios)nstructivos en planos arquitectónicos y estructuras arqueológicas.
