FACULTAD DE INGENIERÍA CIVIL
ING. TOPÓGRAFO GEOMÁTICO

3°B



“Creación de Código que proyecte las trayectorias de los huracanes con capas shp “



AUTORES DEL PROYECTO 
Brizuela Hernandez Rosa Maria 
Rosales Medina Héctor Daniel 


SEMESTRE/GRUPO:
“3°B”




PROFESOR:
Sebastián González Zepeda 


COQUIMATLÁN, COL. 20 DE OCTUBRE 2023


1.	RESUMEN EJECUTIVO
La creación de capas en archivos shapefile (shp) es un proceso esencial en el ámbito de los Sistemas de Información Geográfica (SIG) que permite representar información geoespacial de manera estructurada y manipulable. Estos archivos contienen datos geográficos como puntos, líneas o polígonos, y son utilizados en una amplia gama de aplicaciones, desde cartografía hasta análisis espaciales complejos.

El proceso de creación de capas en archivos shapefile implica varios pasos fundamentales:

1. Adquisición de datos: Se recopilan datos geoespaciales provenientes de diversas fuentes, como son GPS, imágenes satelitales, levantamientos terrestres, entre otros.

2. Preparación de datos: Los datos adquiridos son procesados y limpiados para garantizar su calidad y coherencia. Esto puede incluir la eliminación de errores, la corrección de inconsistencias y la estandarización de formatos.

3. Selección del tipo de geometría: Se determina si la capa contendrá puntos, líneas o polígonos, dependiendo de la naturaleza de los datos y el propósito del análisis.

4. Uso de software SIG: Se utiliza un software especializado en SIG, como ArcGIS, QGIS, u otros, para crear la capa shapefile. Se digitalizan los elementos geoespaciales sobre un lienzo cartográfico, asignándoles atributos descriptivos como nombres, categorías o valores.

5. Configuración de atributos: Se asignan metadatos y atributos a los elementos geográficos para proporcionar información adicional sobre ellos, como nombres, fechas, códigos, etc.

6. Validación y verificación: Se lleva a cabo una revisión exhaustiva para asegurar la precisión y coherencia de los datos. Esto implica verificar la topología, la consistencia espacial y la integridad de la capa.

Una vez completados estos pasos, se genera el archivo shapefile (.shp) que contiene la información geoespacial en un formato compatible con diversos programas SIG y herramientas de análisis espacial.

En resumen, la creación de capas en archivos shapefile es un proceso clave en la gestión de datos geoespaciales, permitiendo la representación y manipulación efectiva de información geográfica para su uso en aplicaciones cartográficas, análisis territoriales, planificación urbana, estudios medioambientales y diversos proyectos relacionados con la geolocalización.





2.	INTRODUCCIÓN
La creación de capas en archivos shapefile (shp) constituye un componente esencial en el ámbito de los Sistemas de Información Geográfica (SIG), proporcionando una estructura fundamental para representar y almacenar datos geoespaciales. Estos archivos shapefile contienen información geográfica como puntos, líneas o polígonos, y se utilizan ampliamente en numerosos campos, desde la cartografía hasta el análisis espacial y la toma de decisiones en entornos urbanos, ambientales, agrícolas y comerciales.

La creación de capas shp involucra la digitalización y organización de elementos geográficos dentro de un entorno de software SIG, lo que permite la representación visual y la manipulación de datos geoespaciales de manera eficiente. Este proceso implica la adquisición, preparación y procesamiento de datos provenientes de diversas fuentes, como mediciones GPS, imágenes satelitales, levantamientos terrestres o información recopilada mediante encuestas.

La correcta creación de capas shp no solo implica la representación visual de elementos geográficos, sino también la asignación de atributos descriptivos que enriquecen la información, como nombres, categorías, valores numéricos o datos temporales. Esto permite un análisis más profundo y preciso de los datos geoespaciales, facilitando la toma de decisiones fundamentadas en diferentes campos profesionales.

La introducción de capas en archivos shapefile es fundamental para comprender la geografía, la distribución espacial de elementos y fenómenos, así como para realizar análisis complejos que ayuden en la comprensión y solución de problemas en diversos contextos, desde la planificación urbana hasta la gestión de recursos naturales y la respuesta a emergencias. En conjunto, la creación de capas shp es un componente esencial en el vasto universo de la información geoespacial, desempeñando un papel crucial en la visualización, gestión y análisis de datos en entornos geográficos.






3.	PLANTEAMIENTO DEL PROBLEMA
Al generar capas en archivos shapefile (shp), pueden surgir una serie de problemas que podrían afectar la calidad y la utilidad de los datos geoespaciales. Algunos de estos problemas comunes son:

1. **Errores topológicos:** Durante el proceso de digitalización de elementos geográficos, pueden ocurrir errores topológicos como solapes, espacios vacíos no deseados o intersecciones incorrectas entre líneas y polígonos. Estos errores pueden comprometer la precisión de los datos y generar interpretaciones incorrectas.

2. **Problemas de precisión:** La precisión de los datos geoespaciales es fundamental. Los errores de precisión pueden surgir debido a la calidad de los datos originales, la resolución de los dispositivos de captura (como GPS), errores humanos durante la digitalización o la manipulación incorrecta de coordenadas.

3. **Atributos incorrectos o faltantes:** Asignar atributos a los elementos geográficos de manera incorrecta o incompleta puede afectar la calidad y la interpretación de los datos. Datos faltantes o mal etiquetados pueden limitar la utilidad de la capa shapefile para análisis posteriores.

4. **Inconsistencias en la proyección:** Utilizar diferentes proyecciones cartográficas en distintos conjuntos de datos puede ocasionar problemas al superponer capas, lo que resulta en discrepancias espaciales que afectan la precisión y la interpretación correcta de los datos.

5. **Tamaño excesivo del archivo:** Si no se optimizan adecuadamente los datos, el tamaño del archivo shapefile puede crecer significativamente, lo que dificulta su manejo, almacenamiento y transferencia.

6. **Corrupción del archivo:** Los archivos shapefile pueden corromperse debido a errores en la manipulación de datos, interrupciones durante la escritura o lectura del archivo, lo que puede resultar en la pérdida parcial o total de la información.

7. **Incompatibilidad entre software:** Algunas veces, los archivos shapefile creados pueden no ser completamente compatibles con diferentes software SIG, lo que puede generar dificultades al compartir o utilizar estos archivos en distintas plataformas.

Es fundamental realizar pruebas exhaustivas, validar y verificar los datos geoespaciales durante y después del proceso de creación de capas shp para detectar y corregir estos problemas. El aseguramiento de la calidad de los datos es esencial para garantizar que las capas shapefile generadas sean precisas, confiables y útiles para su aplicación en análisis espaciales y toma de decisiones


Estado del arte
4.	MARCO HISTORICO
La creación de archivos shapefile (shp) tiene su origen en la década de 1990 y está estrechamente asociada al desarrollo de sistemas de información geográfica (SIG) y herramientas de cartografía digital. Este formato fue desarrollado por la compañía ESRI (Environmental Systems Research Institute) como parte de su software ArcView GIS en ese período.

El concepto de capas geoespaciales y la necesidad de almacenar datos geográficos de manera digital y estructurada se remonta a los inicios de la informática y la cartografía computarizada a fines de la década de 1960 y principios de la década de 1970. En esos momentos, se comenzaron a explorar y desarrollar métodos para almacenar datos geográficos de manera digital, lo que permitió la creación de mapas y la realización de análisis espaciales mediante el uso de computadoras.

Sin embargo, fue a principios de la década de 1990 cuando ESRI introdujo el formato shapefile como un estándar para almacenar datos geoespaciales en su software SIG, permitiendo la representación de puntos, líneas y polígonos con sus atributos asociados en un único conjunto de archivos. El formato shapefile se convirtió rápidamente en uno de los más utilizados y aceptados en la industria SIG debido a su flexibilidad, capacidad para manejar diferentes tipos de geometría y su compatibilidad con una amplia gama de software de cartografía y análisis espacial.

A lo largo de los años, ESRI y otros desarrolladores de software SIG han continuado mejorando y ampliando las capacidades del formato shapefile, agregando soporte para datos tridimensionales, topología avanzada, y enriqueciendo la capacidad de almacenar información geoespacial más compleja y detallada.

A pesar de que el formato shapefile ha sido un estándar ampliamente adoptado durante décadas, con el avance tecnológico y la aparición de estándares más modernos y flexibles como GeoPackage, GeoJSON y otros, se ha comenzado a considerar su eventual reemplazo por formatos más avanzados y compatibles con las demandas actuales de la ciencia y tecnología geoespacial. Sin embargo, debido a su amplia compatibilidad y su arraigo en la comunidad SIG, los archivos shapefile siguen siendo ampliamente utilizados en la actualidad, aunque su uso puede ir disminuyendo gradualmente a medida que se adopten nuevos estándares más eficientes y versátiles.
5.	MARCO CONCEPTUAL
La creación de capas en archivos shapefile (shp) está fundamentada en un conjunto de conceptos clave que abarcan desde los datos geoespaciales hasta su representación digital. Aquí se presenta un marco conceptual que subyace a este proceso:

1. **Datos geoespaciales:** Son información vinculada a ubicaciones en la Tierra. Pueden ser puntos, líneas o polígonos que representan objetos físicos o fenómenos geográficos. Estos datos se capturan a través de diversas fuentes como GPS, imágenes satelitales, encuestas terrestres y otros métodos de recolección.

2. **Geometría espacial:** Refiere a la forma y ubicación de los objetos geográficos en un espacio bidimensional o tridimensional. La creación de capas shp implica definir la geometría de los elementos, como puntos (coordinadas XY), líneas (secuencias de puntos) y polígonos (secuencias cerradas de líneas).

3. **Atributos:** Son características descriptivas asociadas a los elementos geográficos. Estos pueden incluir nombres, códigos, categorías, valores numéricos, fechas u otros datos relevantes que enriquecen la información sobre los elementos representados en la capa shp.

4. **Digitalización:** Es el proceso de convertir datos geográficos analógicos o físicos en información digital. En el contexto de la creación de capas shp, implica el uso de software SIG para capturar y representar visualmente objetos geográficos mediante la digitalización de sus características y atributos.

5. **Topología:** Se refiere a las relaciones espaciales entre los elementos geográficos. La creación de capas shp requiere mantener una topología precisa para evitar errores como solapes, intersecciones no válidas o discontinuidades en los elementos.

6. **Proyección cartográfica:** Es la transformación de coordenadas geográficas tridimensionales en un plano bidimensional. Las capas shp suelen tener una proyección específica que define cómo se representan los datos en el espacio cartográfico.

7. **Formato Shapefile:** Es un formato estándar de archivo para datos geoespaciales desarrollado por ESRI. Consiste en varios archivos que almacenan información geométrica, atributos y metadatos, permitiendo la representación y el intercambio de datos espaciales entre diferentes plataformas SIG.

8. **Software SIG:** Son aplicaciones especializadas que permiten la manipulación, análisis y visualización de datos geográficos. Programas como ArcGIS, QGIS o GRASS GIS son utilizados para crear, editar y trabajar con capas shp.

El marco conceptual de la creación de capas shp se basa en comprender estos conceptos fundamentales para capturar, representar y trabajar con datos geoespaciales de manera precisa y significativa en entornos digitales, facilitando el análisis espacial y la toma de decisiones en una amplia gama de campos.

6.	METODOLOGIA
Utilizar capas en archivos shapefile (shp) implica una metodología que abarca desde la adquisición de datos hasta su análisis y visualización. Aquí te presento una metodología básica para utilizar capas shp:

1. **Adquisición de datos:** Obtén los archivos shapefile o crea tus propias capas utilizando software SIG. Los datos pueden provenir de fuentes diversas como GPS, imágenes satelitales, levantamientos terrestres u otras fuentes geoespaciales.

2. **Exploración y carga de capas:** Utiliza software SIG como ArcGIS, QGIS o programas similares para cargar las capas shp en tu entorno de trabajo. Explora y familiarízate con los datos disponibles en las capas, visualizando los elementos geográficos y sus atributos.

3. **Análisis espacial:** Realiza análisis espaciales sobre las capas shp para obtener información relevante. Esto puede incluir operaciones como superposición de capas, cálculo de áreas, distancias, uniones espaciales, consultas espaciales, entre otros.

4. **Edición y manipulación:** Si es necesario, edita las capas shp para corregir errores topológicos, agregar atributos, dividir o fusionar elementos geográficos, o realizar otras modificaciones que mejoren la calidad de los datos.

5. **Proyección y transformación:** Asegúrate de utilizar la proyección cartográfica adecuada para tus análisis. Puedes necesitar transformar las capas shp a diferentes sistemas de coordenadas para su correcta superposición y análisis.

6. **Visualización y representación:** Crea mapas temáticos o representaciones visuales de los datos utilizando las capas shp. Esto puede ayudar a comprender patrones espaciales, distribuciones geográficas o tendencias en los datos.

7. **Interpretación y toma de decisiones:** Analiza los resultados obtenidos a partir de las capas shp para tomar decisiones informadas en tu campo de estudio o proyecto. La interpretación de los datos espaciales puede conducir a conclusiones importantes y acciones estratégicas.

8. **Documentación y almacenamiento:** Documenta todos los pasos realizados en el uso de las capas shp, incluyendo las transformaciones, análisis realizados, decisiones tomadas y los resultados obtenidos. Almacena los datos y los resultados de manera organizada y segura para futuros usos.

Esta metodología proporciona una guía general para trabajar con capas shp, desde su adquisición y análisis hasta la interpretación de los datos geoespaciales y la toma de decisiones. Es importante adaptar estos pasos según las necesidades específicas de tu proyecto o análisis, así como considerar buenas prácticas en el manejo de datos geográficos para garantizar la precisión y fiabilidad de los resultados

7.	BIBLIOGRAFIAS
Carta Inegi. (s/f). Slideshare.net. Recuperado el 28 de octubre de 2023, de https://es.slideshare.net/belkisrangelconsuegra/levantamiento-con-cinta

Capa estilo . (s/f). Slideshare.net. Recuperado el 28 de octubre de 2023, de https://es.slideshare.net/marcojuniorcallecamacho/levantamiento-con-wincha

