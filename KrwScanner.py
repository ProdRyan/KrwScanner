################################################################
#                                                              #
#                        [ Creditos ]                          #
#                                                              #
################################################################
#                                                              #
#                 Codigo hecho por xNetting                    #
#                                                              #
#                Dev: xNetting / Grupo: Krw Squad              #
#                                                              #
################################################################

# Coded By xNetting
# KrwSquad

import dns.resolver
import sys
import requests
import random
import os

os.system('color ' +random.choice(['4', 'a', '9', 'd']))
print('''

    ███████████████████████████████████████████████████████████████████████
    █▄─█─▄█▄─▄▄▀█▄─█▀▀▀█─▄███─▄▄▄▄█─▄▄▄─██▀▄─██▄─▀█▄─▄█▄─▀█▄─▄█▄─▄▄─█▄─▄▄▀█
    ██─▄▀███─▄─▄██─█─█─█─████▄▄▄▄─█─███▀██─▀─███─█▄▀─███─█▄▀─███─▄█▀██─▄─▄█
    ▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀

                    Dev: xNetting // Grupo: #KrwSquad
                                                                                                                                                
    ''')

def scan5():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │         Ingrese la url que quiere escanear          │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    target_5 = str(input('''
    
    root@xnetting: ~# '''))

    try:
        obj = requests.get(url=target_5)
        ca = dict(obj.headers)
        for x in ca:
            print(f'''
            
    root@xnetting: ~# {x} {ca[x]}''')
    
    except:
        print('''
        
    root@xnetting: ~# No se encontro informacion ''')

def dnsscan4():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │       Ingrese el dominio que quiere escanear        │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    target_4 = str(input('''
    
    root@xnetting: ~# '''))

    try:
        scan = dns.resolver.resolve(target_4, 'MX')
        for a in scan:
            print(f'''
            
    root@xnetting: ~# {a}''')

    except:
        print('''
        
    root@xnetting: ~# No se encontro informacion ''')

def dnsscan3():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │       Ingrese el dominio que quiere escanear        │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    target_3 = str(input('''
    
    root@xnetting: ~# '''))

    try:
        scan = dns.resolver.resolve(target_3, 'SOA')
        for a in scan:
            print(f'''
            
    root@xnetting: ~# {a}''')

    except:
        print('''
        
    root@xnetting: ~# No se encontro informacion ''')

def dnsscan2():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │       Ingrese el dominio que quiere escanear        │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    target_2 = str(input('''
    
    root@xnetting: ~# '''))

    try:
        scan = dns.resolver.resolve(target_2, 'NS')
        for a in scan:
            print(f'''
            
    root@xnetting: ~# {a}''')
    
    except:
        print('''
        
    root@xnetting: ~# No se encontro informacion ''')

def dnsscan1():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │       Ingrese el dominio que quiere escanear        │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    target_1 = str(input('''
    
    root@xnetting: ~# '''))

    try:
        scan = dns.resolver.resolve(target_1, 'A')
        for a in scan:
            print(f'''
            
    root@xnetting: ~# {a}''')

    except:
        print('''
        
    root@xnetting: ~# No se encontro informacion ''')

def main():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Eliga su tipo de scan DNS                         │                      
    │                                                     │
    │        1 - Direccion Host                           │
    │                                                     │
    │        2 - Obtener DNS                              │
    │                                                     │
    │        3 - Informacion DNS de la zona               │   
    │                                                     │
    │        4 - Informacion de Intercambio               │   
    │                                                     │
    │        5 - All Info                                 │                     
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    opcion = input('''
    
    root@xnetting: ~# ''')

    if opcion == '1':
        dnsscan1()
    elif opcion == '2':
        dnsscan2()
    elif opcion == '3':
        dnsscan3()
    elif opcion == '4':
        dnsscan4()
    elif opcion == '5':
        scan5()
    else:
        sys.exit()

main()
