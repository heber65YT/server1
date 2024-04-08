import os
import subprocess

# Comprobamos si Java está instalado
java_installed = subprocess.run(['java', '-version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

if not java_installed:
    print("Java no está instalado. Descargando...")
    # Aquí colocarías el código para descargar e instalar Java, dependiendo del sistema operativo

# Preguntamos por el nombre de la carpeta
nombre_carpeta = "server"

# Comprobamos si la carpeta existe
if not os.path.exists(nombre_carpeta):
    print("La carpeta no existe. Creando carpeta...")
    os.mkdir(nombre_carpeta)

# Cambiamos el directorio de trabajo a la carpeta especificada
os.chdir(nombre_carpeta)

# Comprobamos si el archivo server.jar está presente en la carpeta
if not os.path.exists("server.jar"):
    print("El archivo server.jar no existe. Insertando archivo...")
    # Aquí colocarías el código para copiar o descargar el archivo server.jar en la carpeta

else:
    # Define la cantidad máxima de memoria RAM en megabytes (por ejemplo, 2 GB)
    max_ram_mb = 10240

    # Ejecutamos el archivo server.jar con la configuración de memoria RAM

    print("El archivo server.jar existe. Ejecutando...")

    # Ejecutamos el archivo server.jar
    process = subprocess.Popen(['java', '-Xmx{}m'.format(max_ram_mb), '-jar', 'server.jar'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Leemos la salida estándar y de error en tiempo real
    for linea in iter(process.stdout.readline, b''):
        print("Mensaje del servidor:", linea.decode('utf-8').strip())

    for linea in iter(process.stderr.readline, b''):
        print("Error del servidor:", linea.decode('utf-8').strip())

    # Esperamos a que el proceso termine
    process.wait()

    # Capturamos la salida estándar y de error después de que el proceso haya terminado
    stdout, stderr = process.communicate()

    # Imprimimos la salida
    if stdout:
        print("Salida estándar después de la ejecución:")
        print(stdout.decode('utf-8'))

    if stderr:
        print("Salida de error después de la ejecución:")
        print(stderr.decode('utf-8'))