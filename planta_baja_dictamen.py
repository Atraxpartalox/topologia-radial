import matplotlib.pyplot as plt
import numpy as np

def generar_planta_baja_dictamen():
    fig, ax = plt.subplots(figsize=(10, 10))
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')

    ancho, largo = 8.0, 15.0
    
    # Red de Ejes
    ejes_x = [0.0, 3.5, 8.0]
    ejes_y = [0.0, 4.0, 9.5, 15.0]

    for ex in ejes_x:
        ax.axvline(ex, color='#38BDF8', linestyle='--', linewidth=1.2, alpha=0.7)
    for ey in ejes_y:
        ax.axhline(ey, color='#38BDF8', linestyle='--', linewidth=1.2, alpha=0.7)

    grosor_muro = 0.15

    # Delimitación de Muros (15 cm)
    muros = [
        (0.0, 0.0, ancho, grosor_muro),
        (0.0, largo - grosor_muro, ancho, grosor_muro),
        (0.0, 0.0, grosor_muro, largo),
        (ancho - grosor_muro, 0.0, grosor_muro, largo),
        (grosor_muro, 4.0 - grosor_muro/2, 5.0, grosor_muro),
        (3.5 - grosor_muro/2, 4.0, grosor_muro, 5.5),
        (grosor_muro, 9.5 - grosor_muro/2, 8.0 - 2*grosor_muro, grosor_muro)
    ]

    for m in muros:
        rect = plt.Rectangle((m[0], m[1]), m[2], m[3], facecolor='#F59E0B', edgecolor='#F8FAFC', linewidth=1, alpha=0.9)
        ax.add_patch(rect)

    ax.text(ancho/2.0, largo + 1.2, "ANÁLISIS PARAMÉTRICO - PLANTA BAJA", color='#F8FAFC', fontsize=11, ha='center', fontweight='bold')
    ax.text(ancho/2.0, -1.2, "MUROS DE 15 CM Y EJES PARA DICTAMEN TÉCNICO", color='#94A3B8', fontsize=9, ha='center')

    for idx, ex in enumerate(ejes_x):
        ax.text(ex, -0.5, f"EJE {chr(65+idx)}", color='#38BDF8', fontsize=9, ha='center', fontweight='bold')
    for idx, ey in enumerate(ejes_y):
        ax.text(-0.6, ey, f"EJE {idx+1}", color='#38BDF8', fontsize=9, va='center', fontweight='bold')

    ax.set_xlim(-1.5, ancho + 1.5)
    ax.set_ylim(-2.0, largo + 2.0)
    ax.set_aspect('equal')
    plt.axis('off')

    plt.tight_layout()
    plt.savefig("analisis_planta_baja.png", dpi=300, facecolor=fig.get_facecolor())
    print("Imagen 'analisis_planta_baja.png' generada.")

if __name__ == '__main__':
    generar_planta_baja_dictamen()