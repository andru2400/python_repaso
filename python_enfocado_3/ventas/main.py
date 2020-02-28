import sys
clients = ['pablo','ricardo']

def create_client(cliente_name):
    global clients

    if cliente_name not in clients:
        clients.append(cliente_name)
        # clients += cliente_name
        # _add_comma()
    else:
        print('Client already is in the client\'s list')

def list_clients():
    global clients
    # print(clients)
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))

def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        # clients = clients.replace(client_name+',',update_client_name+',')
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print('Client is not in clients list')

# def _add_comma():
#     global clients
#     clients += ','

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('WHAT DO YOU LIKE TODO TODAY?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def delete_client(client_name):
    global clients

    if client_name in clients:
        # clients = clients.replace(client_name+',','')
        clients.remove(client_name)
    else:
        print('Client is not in clientss list')

    
def search_client(client_name):
    # clients_list = clients.split(',')

    for client in clients:
        if client != client_name:
            continue
        else:
            return True

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name ?')

        if client_name == 'exit':
            client_name = None
            break

        if not client_name:
            sys.exit()

    return client_name

if __name__ == '__main__': 
    _print_welcome()
    command = input()
    command = command.upper()

    if command  == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name')
        update_client(client_name, update_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        fount = search_client(client_name)

        if fount:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))

        list_clients()
    else:
        print('Invalid Command')
        