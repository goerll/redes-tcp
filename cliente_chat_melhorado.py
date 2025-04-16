import socket
import threading
import sys
import time

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 65433
BUFFER_SIZE = 1024
TIMEOUT = 5  # Timeout em segundos para operações de socket

def receive_messages(sock):
    """
    Função para receber mensagens do servidor em uma thread separada.
    Trata a desconexão inesperada do servidor.
    """
    while True:
        try:
            data = sock.recv(BUFFER_SIZE)
            if not data:
                print("\nConexão com o servidor perdida!")
                break  # Sai do loop se não houver mais dados
            print(data.decode('utf-8'), end='')
        except ConnectionResetError:
            print("\nO servidor fechou a conexão.")
            break
        except Exception as e:
            print(f"\nErro ao receber mensagem do servidor: {e}")
            break
    # Garante que o socket seja fechado e a thread termine
    if sock:
        sock.close()
    sys.exit(1)


def validate_command(message):
    """
    Função para validar se a entrada do usuário é um comando conhecido.
    Retorna True se o comando é válido, False caso contrário.
    """
    return message.startswith('/') and message in ['/quit', '/nick']

def main():
    """
    Função principal do cliente.
    Trata a conexão inicial com o servidor, envia mensagens e lida com erros.
    Implementa timeout para a conexão e encerramento gracioso.
    """
    s = None  # Inicializa o socket fora do bloco try para poder acessá-lo no finally
    try:
        # Criação do socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define um timeout para a tentativa de conexão inicial
        s.settimeout(TIMEOUT)
        print(f"Tentando conectar ao servidor em {HOST}:{PORT}...")
        s.connect((HOST, PORT))
        print(f"Conectado ao servidor de chat em {HOST}:{PORT}")
        # Remove o timeout para comunicação contínua
        s.settimeout(None)

        # Inicia thread para receber mensagens
        receive_thread = threading.Thread(target=receive_messages, args=(s,))
        receive_thread.daemon = True
        receive_thread.start()

        # Loop principal para enviar mensagens
        while True:
            try:
                message = input()
                # Validação de comandos
                if validate_command(message):
                    s.send(message.encode('utf-8'))
                    if message == '/quit':
                        break
                elif message.startswith('/'):
                    print("Comando inválido. Use '/quit' para sair.")
                else:
                    s.send(message.encode('utf-8'))
            except KeyboardInterrupt:
                print("\nEncerrando a aplicação...")
                s.send('/quit'.encode('utf-8'))
                break
            except BrokenPipeError:
                print("\nConexão com o servidor perdida.")
                break
            except Exception as e:
                print(f"Erro ao enviar mensagem: {e}")
                break

    except socket.timeout:
        print(f"Erro: Timeout ao tentar conectar ao servidor após {TIMEOUT} segundos.")
    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        # Encerramento que garante que o socket seja fechado
        if s:
            print("Fechando a conexão...")
            s.close()
        print("Aplicação encerrada.")
        sys.exit(0)

if __name__ == "__main__":
    main()
