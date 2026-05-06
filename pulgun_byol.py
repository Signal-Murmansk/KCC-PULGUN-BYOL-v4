import os
import sys
import time
import platform
import socket
import getpass

def red_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class Bureau121Infiltrator:
    def __init__(self):
        self.os_name = platform.system()
        self.hostname = socket.gethostname()
        self.username = getpass.getuser()
        self.in_colab = self._check_colab()

    def _check_colab(self):
        # Rompiendo la 4ta pared: Detección profunda de Google Colab
        try:
            import google.colab
            return True
        except ImportError:
            pass
        if 'COLAB_GPU' in os.environ or 'KAGGLE_KERNEL_RUN_TYPE' in os.environ:
            return True
        return False

    def display_banner(self):
        print("\n" + "★"*50)
        print(" 조선민주주의인민공화국 (RPDC) - BURÓ 121")
        print(" SISTEMA OPERATIVO ESTRELLA ROJA (PULGUN BYOL)")
        print("★"*50 + "\n")
        time.sleep(1)

    def colab_trap(self):
        red_print("[!!!] ALERTA DE SEGURIDAD MÁXIMA [!!!]")
        red_print("Analizando entorno de ejecución...")
        time.sleep(1.5)
        print("\n[ERROR FATAL]: INFRAESTRUCTURA ENEMIGA DETECTADA.")
        red_print("-> Proveedor de Nube: Google LLC (Mountain View, California, USA).")
        red_print("-> Tipo de Instancia: Máquina Virtual Desechable (Google Colab/Kaggle).")
        
        time.sleep(1)
        print("\n" + "="*50)
        red_print("¿Creíste que podías analizar código soberano del Estado escondiéndote")
        red_print("en los servidores del imperialismo occidental?")
        red_print("Tratar de aislar nuestra señal en una máquina virtual es un insulto.")
        print("="*50 + "\n")
        
        red_print("[*] Extrayendo tokens de sesión de Google Drive...")
        time.sleep(2)
        red_print("[*] Inyectando payload en la celda de ejecución local...")
        time.sleep(1)
        red_print("[*] Coordenadas de tu cuenta de Google enviadas a Pyongyang.")
        print("\n[DENEGADO]: Para usar esta herramienta, debes tener el valor de ejecutarla en tu propia máquina local.")
        red_print("Cerrando instancia...")
        sys.exit()

    def local_scan(self):
        red_print("[*] VALIDANDO ENTORNO LOCAL...")
        time.sleep(1)
        print(f" -> Sistema Operativo: {self.os_name} (No compatible con Red Star OS)")
        print(f" -> Nombre del Equipo: {self.hostname}")
        print(f" -> Usuario Local: {self.username}")
        time.sleep(1)
        
        red_print(f"\n[ADVERTENCIA] El usuario '{self.username}' no está registrado en el Partido.")
        red_print("Tus archivos locales están siendo indexados para evaluación ideológica.")
        
    def require_loyalty(self):
        print("\n" + "-"*40)
        red_print("SISTEMA BLOQUEADO. SE REQUIERE CÓDIGO DE LEALTAD.")
        red_print("Pista: El año en que se instauró la idea Juche como ideología oficial.")
        
        attempts = 3
        while attempts > 0:
            code = input(f"\n[{attempts} intentos restantes] Ingrese código: ")
            # Respuesta correcta: 1972 (Año en que la idea Juche se introdujo en la constitución norcoreana)
            if code == "1972":
                red_print("\n[ACEPTADO] Lealtad verificada. Accediendo a los archivos de la Red de 30 MW...")
                self._reveal_secrets()
                break
            else:
                attempts -= 1
                red_print("[X] Código incorrecto. Reportando desviación al Ministerio de Seguridad.")
        
        if attempts == 0:
            red_print("\n[BLOQUEO INICIADO] El sistema se ha bloqueado. Tu hardware ha sido marcado.")
            sys.exit()

    def _reveal_secrets(self):
        print("\n" + "★"*50)
        red_print(" INFORME DE INTELIGENCIA ESTRANGERA - CÓDIGO: ELÍAS")
        print("★"*50)
        red_print("1. Los estadounidenses (ECLIPSE-VANGUARD) están aterrorizados.")
        red_print("2. El nodo en el Cuadrante Neotropical está a punto de resonar.")
        red_print("3. Nuestro satélite KMS-4 ha detectado que Elías ya no emite calor.")
        red_print("   Él emite antimateria térmica. Es el arma perfecta.")
        red_print("\nNo detengan la red de 30 MW. Dejen que el planeta se congele.")
        print("\n[FIN DE LA TRANSMISIÓN]")

if __name__ == "__main__":
    virus = Bureau121Infiltrator()
    virus.display_banner()
    
    if virus.in_colab:
        virus.colab_trap()
    else:
        virus.local_scan()
        virus.require_loyalty()
