import socket
import time
from datetime import datetime

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço de loopback (localhost)
PORT = 65432  # Porta para escutar (não privilegiada)

try:
    # Criação do socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Associa o socket ao endereço e porta
        s.bind((HOST, PORT))
        # Habilita o socket para aceitar conexões, com fila de até 5 conexões
        s.listen(5)
        print(f"Servidor escutando em {HOST}:{PORT}")
        # Loop para aceitar conexões
        while True:
            # Espera por uma conexão
            conn, addr = s.accept()
            with conn:
                print(f"Conectado por {addr}")
                start_time = time.time()  # Registra o tempo de início da conexão
                # Loop para receber dados
                while True:
                    # Recebe os dados do cliente (máximo de 1024 bytes)
                    data = conn.recv(1024)
                    if not data:
                        # Se não receber dados, encerra a conexão
                        break
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtém o timestamp atual
                    print(f"[{timestamp}] Recebido: {data.decode('utf-8')}")
                    # Envia resposta ao cliente
                    conn.sendall(f"Eco: {data.decode('utf-8')}".encode('utf-8'))
                end_time = time.time()  # Registra o tempo de término da conexão
                duration = end_time - start_time  # Calcula a duração da conexão
                print(f"Conexão com {addr} encerrada. Duração: {duration:.2f} segundos.")
except KeyboardInterrupt:
    print("\nServidor encerrado pelo usuário")
except Exception as e:
    print(f"Erro: {e}")
