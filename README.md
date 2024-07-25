Este script se hizo con la idea de proveer accesibilidad extra para videojuegos no traducidos al español. Es algo rápido y para salir del paso que hice para uso personal con mucho lugar para mejorar el código.

# RESUMEN:
El script saca una captura de pantalla a la cual se puede elegir un recuadro. Automaticamente se recorta, se intenta extraer el texto para luego ser traducido.


# INSTALACION:
1.	Instalar Python 3.11  - https://www.python.org/downloads/
2.	Ejecutar el archivo installerpip.cmd
3.	Copiar Main.py  a la carpeta donde se lo quiera guardar.
4.	Crear un acceso directo para ejecutar Main.py (ej: c:\python\python.exe main.py) y asignarle “Tecla de método abreviado” (hotkey) en propiedades de Acceso Directo.


# USO:
Supongamos que queremos traducir las características de una armadura en cierto juego. Para ello vamos a ponerla en pantalla, presionar las teclas que configuramos en el punto 4 de INSTALACION lo que abrirá una ventana. Seleccionamos la parte de la imagen que se desea traducir y cerramos la ventana (es completamente antiintuitivo). Por último Alt+Tab hasta dejar la consola de python (una pantalla de CMD) que nos dará una traducción.

# A tener en cuenta:
Me encontré con varios errores a la hora de ejecutar este script. Los dos más importantes fueron:

“No se puede importar ABC”

El problema surgía en el entorno virtual de Pycharm. Desconozco lo suficiente como para solucionarlo así que simplemente volví al notepad++

“No da ningún resultado”

El microprocesador era demasiado antiguo. Lamentablemente no encontré ningún tipo de hotfix. 

“Process finished with exit code -1073741795 (0xC000001D)”

Nuevamente el error surgió dentro de Pycharm y tiene que ver con la incompatibilidad del microprocesador. El fallo me surgió con un Intel I3-3240. Es el mismo error que el anterior. Tuve que cambiar de equipo para que funcione.

# Dependencias:

matplotlib

selenium

Pillow

easyocr

numpy==1.26.4

python-bidi==0.4.2

torch torchvision torchaudio

opencv-python

keyboard

deep-translator

# Nota final: 
Si alguien mejora el código le agradecería que me avise.
