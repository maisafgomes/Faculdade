from easysnmp import Session

import PySimpleGUI as sg

print = sg.Print

def printConexoesUDP(ipL,ipE):
    print('udpLocalAddress     ' + ipL + '     ' + ipE)



def buscaConexoesUDP(ip):
    session = Session(hostname=str(ip), community='public', version=2)
    system_items = session.walk('1.3.6.1.2.1.7.5.1.1')
    a = [] 
    print("PROTOCOLO             CONEXAO LOCAL             CONEXAO EXTERNA")
    for item in system_items:
        printConexoesUDP(item.oid_index,item.value)
        