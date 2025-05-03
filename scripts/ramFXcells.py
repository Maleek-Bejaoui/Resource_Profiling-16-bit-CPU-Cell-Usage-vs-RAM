# Estimation de la Consommation Logique d’un CPU 16 bits en ASIC (TinyTapeout)
import os
import shutil
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Données
x = np.array([16, 32, 64, 128])
y = np.array([2040, 2595, 3719, 5898])

# Régression et graphique
p = Polynomial.fit(x, y, deg=1)
coefs = p.convert().coef

# Recréation du graphique
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'o', label='Données réelles', color='orange')
plt.plot(x, p(x), '-', label=f"Régression linéaire: y = {coefs[1]:.2f}x + {coefs[0]:.2f}", color='brown')
plt.title("Taille de RAM vs Cellules utilisées (avec régression)")
plt.xlabel("Taille de RAM (octets)")
plt.ylabel("Cellules logiques utilisées")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# # Sauvegarde du graphique
# img_path = "/mnt/data/asic_ram_estimation/docs/ram_vs_cells_regression.png"
# os.makedirs(os.path.dirname(img_path), exist_ok=True)
# plt.savefig(img_path)


