<br>FACULTAD DE INGENIERÍA CIVIL
<br> ING. TOPÓGRAFO GEOMÁTICO
<br> 3°B
<br> **Creación de Código que proyecte las trayectorias de los huracanes con capas shp **
<br> AUTORES DEL PROYECTO 
<br> Brizuela Hernandez Rosa Maria 
<br> Rosales Medina Héctor Daniel 
<br>Asesor: Sebastián González Zepeda 
<br> COQUIMATLÁN, COL. 20 DE OCTUBRE 2023
<br>
<br>
2.	INTRODUCCIÓN
La creación de capas en archivos shapefile (shp) constituye un componente esencial en el ámbito de los Sistemas de Información Geográfica (SIG), proporcionando una estructura fundamental para representar y almacenar datos geoespaciales. Estos archivos shapefile contienen información geográfica como puntos, líneas o polígonos, y se utilizan ampliamente en numerosos campos, desde la cartografía hasta el análisis espacial y la toma de decisiones en entornos urbanos, ambientales, agrícolas y comerciales.
La creación de capas shp involucra la digitalización y organización de elementos geográficos dentro de un entorno de software SIG, lo que permite la representación visual y la manipulación de datos geoespaciales de manera eficiente. Este proceso implica la adquisición, preparación y procesamiento de datos provenientes de diversas fuentes, como mediciones GPS, imágenes satelitales, levantamientos terrestres o información recopilada mediante encuestas.
3.	PLANTEAMIENTO DEL PROBLEMA
Al generar capas en archivos shapefile (shp), pueden surgir una serie de problemas que podrían afectar la calidad y la utilidad de los datos geoespaciales. Algunos de estos problemas comunes son:
1. **Errores topológicos:** 
2. **Problemas de precisión:** 
3. **Atributos incorrectos o faltantes:** 
4. **Inconsistencias en la proyección:** 
6.	METODOLOGIA
Utilizar capas en archivos shapefile (shp) implica una metodología que abarca desde la adquisición de datos hasta su análisis y visualización. Aquí te presento una metodología básica para utilizar capas shp:
1. **Adquisición de datos:** Obtén los archivos shapefile o crea tus propias capas utilizando software SIG. Los datos pueden provenir de fuentes diversas como GPS, imágenes satelitales, levantamientos terrestres u otras fuentes geoespaciales.
2. **Exploración y carga de capas:** Utiliza software SIG como ArcGIS, QGIS o programas similares para cargar las capas shp en tu entorno de trabajo. Explora y familiarízate con los datos disponibles en las capas, visualizando los elementos geográficos y sus atributos.
3. **Análisis espacial:** Realiza análisis espaciales sobre las capas shp para obtener información relevante. Esto puede incluir operaciones como superposición de capas, cálculo de áreas, distancias, uniones espaciales, consultas espaciales, entre otros.
4. **Edición y manipulación:** Si es necesario, edita las capas shp para corregir errores topológicos, agregar atributos, dividir o fusionar elementos geográficos, o realizar otras modificaciones que mejoren la calidad de los datos.
5. **Proyección y transformación:** Asegúrate de utilizar la proyección cartográfica adecuada para tus análisis. Puedes necesitar transformar las capas shp a diferentes sistemas de coordenadas para su correcta superposición y análisis.
7.	BIBLIOGRAFIAS
Carta Inegi. (s/f). Slideshare.net. Recuperado el 28 de octubre de 2023, de https://es.slideshare.net/belkisrangelconsuegra/levantamiento-con-cinta
Capa estilo . (s/f). Slideshare.net. Recuperado el 28 de octubre de 2023, de https://es.slideshare.net/marcojuniorcallecamacho/levantamiento-con-wincha


CODIGO GENERADO 
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.basemap import Basemap
os.chdir('C:\programacion3\huracanes')
 Establecer archivos de cada una de las trayectorias
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
 
Cargar cartografía ráster base
tierra = m.shadedrelief()
 
Mostrar paralelos y meridianos
import numpy as np
paralelos = m.drawparallels(np.linspace(-90,90,13), color='grey')
meridianos = m.drawmeridians(np.linspace(-180,180,13), color='grey')
 
 
Cargar y mostrar las trayectorias diferenciadas por color
map_tray1 = m.readshapefile(h1, 'Huracan 1', color='#ff5d17', linewidth=2)
map_tray2 = m.readshapefile(h2, 'Huracan 2', color='#ffe312', linewidth=2)
map_tray3 = m.readshapefile(h3, 'Huracan 3', color='#30a64d', linewidth=2)
map_tray4 = m.readshapefile(h4, 'Huracan 4', color='#e02d5a', linewidth=2)
map_tray5 = m.readshapefile(h5, 'Huracan 5', color='#8d20d6', linewidth=2)
 
plt.title('Huracanes en Mexico', fontdict={'fontsize':22}, pad=20)
 
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
  

