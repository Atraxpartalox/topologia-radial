import cv2
import numpy as np
import matplotlib.pyplot as plt

def extraer_geometria_piedra_sol():
    size = 800
    center = (size // 2, size // 2)
    radios = [80, 150, 220, 290, 360]
    
    fig, ax = plt.subplots(figsize=(10, 10))
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')
    
    # Anillos Concéntricos
    for r in radios:
        circle = plt.Circle(center, r, color='#38BDF8', fill=False, linewidth=1.5, linestyle='--')
        ax.add_patch(circle)
        
    # Ejes Octagonales
    for i in range(8):
        angle = i * (2 * np.pi / 8)
        x2 = center[0] + 360 * np.cos(angle)
        y2 = center[1] + 360 * np.sin(angle)
        ax.plot([center[0], x2], [center[1], y2], color='#F59E0B', linewidth=1.2, alpha=0.8)

    # Divisiones Radiales
    for i in range(20):
        angle = i * (2 * np.pi / 20)
        x1 = center[0] + 220 * np.cos(angle)
        y1 = center[1] + 220 * np.sin(angle)
        x2 = center[0] + 290 * np.cos(angle)
        y2 = center[1] + 290 * np.sin(angle)
        ax.plot([x1, x2], [y1, y2], color='#00FFFF', linewidth=2.0)

    # Anotaciones
    ax.scatter([center[0]], [center[1]], color='#F43F5E', s=100, zorder=5)
    ax.text(center[0], center[1] - 375, "ANILLO EXTERIOR: XIUHCOATL (52 AÑOS)", color='#F8FAFC', fontsize=9, ha='center', fontweight='bold')
    ax.text(center[0], center[1] - 250, "ANILLO INTERMEDIO: TONALPOHUALLI (20 DÍAS)", color='#00FFFF', fontsize=9, ha='center', fontweight='bold')
    ax.text(center[0], center[1] - 100, "NÚCLEO: 4 OLLIN", color='#F59E0B', fontsize=9, ha='center', fontweight='bold')

    ax.set_xlim(0, size)
    ax.set_ylim(size, 0)
    plt.axis('off')
    
    plt.title("ALGORITMO DE DESCUBRIMIENTO GEOMÉTRICO v1.0\nEstructura Paramétrica Radial", 
              color='#F8FAFC', fontsize=12, pad=20, fontweight='bold')

    plt.tight_layout()
    plt.savefig("descubrimiento_piedra_sol.png", dpi=300, facecolor=fig.get_facecolor())
    print("Imagen 'descubrimiento_piedra_sol.png' generada.")

if __name__ == '__main__':
    extraer_geometria_piedra_sol()