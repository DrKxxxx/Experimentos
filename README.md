Este proyecto ha sido desarrollado exclusivamente con fines educativos y de investigación para mi Trabajo de Fin de Grado (TFG).

El autor no se hace responsable del uso indebido de este código ni de los daños que puedan derivarse de su ejecución en entornos no controlados. El objetivo es demostrar el funcionamiento técnico del cifrado de archivos en sistemas Linux para mejorar la seguridad defensiva.

¡No lo uses en máquinas que no sean tuyas!

## 🚀 Guía de Uso del Laboratorio

Para realizar la simulación completa, sigue estos pasos:

1. **Preparación**: Crear o tener un archivo que NO NOS IMPORTE PERDER (ej: `notas_secretas.txt`).
2. **Ataque**: Ejecutar `cifrador.py` para simular el secuestro de datos.
3. **Verificación**: Comprobar que los archivos son ahora ilegibles y que se ha generado una `clave.key`.
4. **Recuperación**: Usar la `clave.key` con `descifrador.py` para restaurar los datos originales.
---------------------------------------------------------------------------------------------------------------
This project has been developed exclusively for educational and research purposes for my Final Degree Project (TFG).

The author is not responsible for the misuse of this code or for any damage that may result from its execution in uncontrolled environments. The objective is to demonstrate the technical functioning of file encryption in Linux systems to improve defensive security.

Do not use it on machines that do not belong to you!

## 🚀 Laboratory User Guide

To perform the complete simulation, follow these steps:

1. **Preparation**: Create or have a file that you DO NOT MIND LOSING (e.g., `secret_notes.txt`).
2. **Attack**: Run `cipher.py` to simulate data hijacking.
3. **Verification**: Check that the files are now unreadable and that a `key.key` has been generated.
4. **Recovery**: Use the `key.key` with `decryptor.py` to restore the original data.

---------------------------------------------------------------------------
---------------------------------------------------------------------------

## 🛡️ Fase 2: Simulación de Intrusión y Persistencia

En esta etapa del experimento, se simula el compromiso de un servidor mediante técnicas de fuerza bruta y el establecimiento de una conexión persistente.

### Herramientas desarrolladas:
* **worn.py**: Script de automatización que realiza escaneo de puertos (22 SSH) y ataque de diccionario.
* **Persistencia Invisible**: Implementación de un backdoor mediante un script oculto en `.local/` vinculado al `.bashrc`.
* **Técnica de Desacople**: Uso de `setsid` y redirección de errores a `/dev/null` para garantizar que la terminal de la víctima no se bloquee ni se cierre al iniciar la conexión.

### Flujo del Experimento:
1. Escaneo de la red local en busca de objetivos.
2. Ataque de fuerza bruta hasta obtener las credenciales del usuario.
3. Despliegue del payload de persistencia.
4. Recepción de la Reverse Shell en Kali Linux mediante Netcat.
---------------------------------------------------------------------------
## 🛡️ Phase 2: Intrusion and Persistence Simulation

In this stage of the experiment, server compromise is simulated using brute force techniques and the establishment of a persistent connection.

### Tools developed:
* **worn.py**: Automation script that performs port scanning (22 SSH) and dictionary attacks.
* **Invisible Persistence**: Implementation of a backdoor using a hidden script in `.local/` linked to `.bashrc`.
* **Decoupling Technique**: Use of `setsid` and error redirection to `/dev/null` to ensure that the victim's terminal does not crash or close when the connection is initiated.

### Experiment Flow:
1. Scanning the local network for targets.
2. Brute force attack until user credentials are obtained.
3. Deployment of the persistence payload.
4. Receipt of the Reverse Shell in Kali Linux using Netcat.

Translated with DeepL.com (free version)
