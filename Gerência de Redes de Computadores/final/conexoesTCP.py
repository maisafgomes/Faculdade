from easysnmp import Session
import PySimpleGUI as sg

print = sg.Print

def printConexoesTCP(ipL,pL,ipE,pE):
    print("PROTOCOLO         CONEXAO LOCAL             CONEXAO EXTERNA")
    for i in range(len(ipL)):
        print('TCPipv4        '+'.'.join(ipL[i])+'  '+''.join(pL[i])+'        '+'.'.join(ipE[i])+'  '+''.join(pE[i]))

def printConexoesTCP2(ipL,pL,ipE,pE):
    print("PROTOCOLO       CONEXAO LOCAL                                                    CONEXAO EXTERNA")
    for i in range(len(ipL)):
        print('TCPipv6        '+'.'.join(ipL[i])+'  '+''.join(pL[i])+'        '+'.'.join(ipE[i])+'  '+''.join(pE[i]))


def arruma(listadeTCP):
    ipLocal = []
    portaLocal = []
    ipExterno  = []
    portaExterno = []
    for item in listadeTCP:
        aux1 = []
        aux2 = []
        string = str(item.encode('utf-8'))
        arrumado = string.split(".")
        for i in range (2,6):
             aux1.append(arrumado[i])
        for i in range (9,13):
             aux2.append(arrumado[i])
        ipLocal.append(aux1)
        ipExterno.append(aux2)
        portaLocal.append(arrumado[6])
        portaExterno.append(arrumado[13])
    printConexoesTCP(ipLocal,portaLocal,ipExterno,portaExterno)

def arruma2(listadeTCP2):
    ipLocal = []
    portaLocal = []
    ipExterno  = []
    portaExterno = []
    for item in listadeTCP2:
        aux1 = []
        aux2 = []
        string = str(item.encode('utf-8'))
        arrumado = string.split(".")
        for i in range (2,18):
             aux1.append(arrumado[i])
        for i in range (21,37):
             aux2.append(arrumado[i])
        ipLocal.append(aux1)
        ipExterno.append(aux2)
        portaLocal.append(arrumado[18])
        portaExterno.append(arrumado[37])
    printConexoesTCP2(ipLocal,portaLocal,ipExterno,portaExterno)



def buscaConexoesTCP(ip):
    session = Session(hostname=str(ip), community='public', version=2)
    system_items = session.walk('tcpConnectionState.1')
    a = []
    for item in system_items:
        if item.value == '5':
            a.append(item.oid_index)

    arruma(a)

    
def buscaConexoesTCP2(ip):
    session = Session(hostname=str(ip), community='public', version=2)
    system_items = session.walk('tcpConnectionState.2')
    b = []
    for item in system_items:
        if item.value == '5':
            b.append(item.oid_index)
        
    arruma2(b)
