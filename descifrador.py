from cryptography.fernet import Fernet

# 1. Cargamos la llave del archivo que generó el atacante
with open("clave.key", "rb") as key_file:
    key = key_file.read()

f = Fernet(key)

# 2. Leemos el archivo cifrado (el que tiene símbolos raros)
with open("notas_secretas.txt", "rb") as file:
    encrypted_data = file.read()

# 3. Desciframos los datos
decrypted_data = f.decrypt(encrypted_data)

# 4. Sobrescribimos el archivo con el texto original
with open("notas_secretas.txt", "wb") as file:
    file.write(decrypted_data)

print("✅ ¡RESCATE COMPLETADO! Los archivos han sido restaurados.")
