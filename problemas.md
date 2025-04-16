# Problemas

1. Tratamento inadequado de desconexões: quando um cliente se desconecta abruptamente a função broadcast captura exceções ao enviar mensagens mas não remove imediatamente o socket da lista clients, deixando referências a sockets fechados na lista até a remoção ser feita no próximo loop.
2. Falta de validação de entrada: não existem limites de tamanho para nicknames ou mensagens.
3. Vulnerabilidade a ataques de negação de serviço: o servidor aceita conexões indefinidamente e cria uma nova thread para cada cliente, clientes maliciosos podem manter conexões abertas sem enviar dados, esgotando os sockets disponíveis.