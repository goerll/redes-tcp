# Relatório

# Atividade 1
## Parte 1
Servidor executando e escutando a porta 65432
![Screenshot From 2025-04-15 22-34-29.png](https://raw.githubusercontent.com/goerll/redes-tcp/refs/heads/main/Screenshot%20From%202025-04-15%2022-34-29.png)

## Parte 2
Cliente conectando ao servidor e mandando algumas mensagens de teste
![[Screenshot From 2025-04-15 22-35-28 1.png]]
Servidor recebendo as mensagens
![[Screenshot From 2025-04-15 22-35-19.png]]

## Parte 3
Captura Wireshark do tráfego do servidor
![[Screenshot From 2025-04-15 22-42-36.png]]
Podemos observar o three-way handshake nos três primeiros pacotes. As duas mensagens recebidas correspondem aos pacotes 83-86 e 99-101, seguido pelo fechamento da conexão nos últimos dois pacotes.

### Desafio Extra
Servidor modificado para mostrar o timestamp das mensagens e a duração das conexões.
![[Screenshot From 2025-04-15 23-00-56.png]]

# Atividade 2
## Parte 1

![[Pasted image 20250416114716.png]]
## Parte 2
Servidor de chat funcionando com três clientes, visão do usuário 3 em relação ao chat.
![[Screenshot From 2025-04-15 22-47-18.png]]

# Atividade 3
## Parte 1
1. Tratamento inadequado de desconexões: quando um cliente se desconecta abruptamente a função broadcast captura exceções ao enviar mensagens mas não remove imediatamente o socket da lista clients, deixando referências a sockets fechados na lista até a remoção ser feita no próximo loop.
2. Falta de validação de entrada: não existem limites de tamanho para nicknames ou mensagens.
3. Vulnerabilidade a ataques de negação de serviço: o servidor aceita conexões indefinidamente e cria uma nova thread para cada cliente, clientes maliciosos podem manter conexões abertas sem enviar dados, esgotando os sockets disponíveis.

## Parte 2
Está no arquivo cliente_chat_melhorado.py

## Parte 3
![[Screenshot From 2025-04-16 13-40-04.png]]
