import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.basemap import Basemap
os.chdir('C:\programacion3\huracanes')
# Establecer archivos de cada una de las trayectorias
h1 = "huracan 1"
h2 = "huracan 2"
h3 = "huracan 3"
h4 = "huracan 4"
h5 = "huracan 5"

fig, ax = plt.subplots(figsize=(10, 10))
 
m = Basemap(
    ax = ax,
    resolution = 'l',
    projection = 'ortho',
    lon_0 = -110, lat_0 = 30
    # llcrnrlon = -12, llcrnrlat = 28,
    # urcrnrlon = 45, urcrnrlat = 50    
)
 
# Cargar cartografía ráster base
tierra = m.shadedrelief()
 
# Mostrar paralelos y meridianos
import numpy as np
paralelos = m.drawparallels(np.linspace(-90,90,13), color='grey')
meridianos = m.drawmeridians(np.linspace(-180,180,13), color='grey')
 
 
# Cargar y mostrar las trayectorias diferenciadas por color
map_tray1 = m.readshapefile(h1, 'Huracan 1', color='#ff5d17', linewidth=2)
map_tray2 = m.readshapefile(h2, 'Huracan 2', color='#ffe312', linewidth=2)
map_tray3 = m.readshapefile(h3, 'Huracan 3', color='#30a64d', linewidth=2)
map_tray4 = m.readshapefile(h4, 'Huracan 4', color='#e02d5a', linewidth=2)
map_tray5 = m.readshapefile(h5, 'Huracan 5', color='#8d20d6', linewidth=2)
 
# Añadir un título
plt.title('Huracanes en Mexico', fontdict={'fontsize':22}, pad=20)
 
# Añadir una leyenda
elem_leyenda = [
    Line2D([0], [0], label='Huracan 1', color='#ff5d17', linewidth=2),
    Line2D([0], [0], label='Huracan 2', color='#ffe312', linewidth=2),
    Line2D([0], [0], label='Huracan 3', color='#30a64d', linewidth=2),
    Line2D([0], [0], label='Huracan 4', color='#e02d5a', linewidth=2),
    Line2D([0], [0], label='Huracan 5', color='#8d20d6', linewidth=2)
]
 
ax.legend(handles=elem_leyenda, title='Trayectorias', title_fontsize=15, 
          fontsize=12, loc='upper right', facecolor='white', shadow=True, 
          borderpad=2, columnspacing=2, labelspacing=1)
 
plt.xlabel("Proyecto Programacion", 
           fontsize=12, labelpad=30)
 
plt.show()