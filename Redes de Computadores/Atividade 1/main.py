from socket import *

def monstro(nportas):
  print('Você encontrou um monstro!! \n')
  a = True
  while(a):
    escolha = int(input('Escolha uma porta de 0 a %s \n' %nportas))
    if escolha > nportas:
      print('Você escolheu um numero errado \n')
      a = True  
    else:
      mensagem = bytes(str(escolha), encoding='utf8') 
      connection.sendto(mensagem,(host,port))
      data = connection.recv(1024)
      resposta = str(data, 'utf-8')
      resposta = resposta.split(';')
      if resposta[0] == 'MONSTER_ATTACKED':
        print("Você foi atacado pelo monstro \n")
      else:
        print("Você matou o monstro \n")
      print("------------------------------")
      print("Vida: %s \n" %resposta[1])
      print("Pontos: %s" %resposta[2])
      print("------------------------------\n")
      a = False

def bau():
  print('Você encontrou um bau!! \n')
  a = True
  while(a):
    escolha = int(input('Escolha: \n 0 - para ignorar o bau \n 1 - para abrir o bau \n'))
    if escolha > 1:
      print('Você escolheu uma opção errada \n')
      a = True  
    else:
      if escolha == 1:
        mensagem = bytes('YES', encoding='utf8') 
        connection.sendto(mensagem,(host,port))
        data = connection.recv(1024)
        resposta = str(data, 'utf-8')
        resposta = resposta.split(';')
        print("O bau foi aberto e você recebeu %s pontos \n" %resposta[1])
        print("------------------------------")
        print("Vida: %s \n" %resposta[2])
        print("Pontos: %s" %resposta[3])
        print("------------------------------\n")

      else:
        mensagem = bytes('NO', encoding='utf8') 
        connection.sendto(mensagem,(host,port))
        data = connection.recv(1024)
        resposta = str(data, 'utf-8')
        resposta = resposta.split(';')
        print("O Bau foi ignorado")
        print("------------------------------")
        print("Vida: %s \n" %resposta[1])
        print("Pontos: %s" %resposta[2])
        print("------------------------------\n")
      a = False

def chefao():
  print('Você encontrou o chefão \n')
  a = True
  while(a):
    escolha = int(input('Escolha: \n 0 - para fugir do chefão \n 1 - para lutar com o chefão \n'))
    if escolha > 1:
      print('Você escolheu uma opção errada \n')
      a = True  
    else:
      if escolha == 1:
        mensagem = bytes('FIGHT', encoding='utf8') 
        connection.sendto(mensagem,(host,port))
        data = connection.recv(1024)
        resposta = str(data, 'utf-8')
        resposta = resposta.split(';')
        if resposta[0] == 'BOSS_DEFEATED':
          print("Você matou o chefão \n")
        else:
          print("Você perdeu a luta como chefão \n")  
        print("------------------------------")  
        print("Vida: %s \n" %resposta[1])
        print("Pontos: %s" %resposta[2])
        print("------------------------------\n")
      else:
        mensagem = bytes('RUN', encoding='utf8') 
        connection.sendto(mensagem,(host,port))
        data = connection.recv(1024)
        resposta = str(data, 'utf-8')
        resposta = resposta.split(';')
        print("Você fugiu!")
        print("------------------------------")
        print("Vida: %s \n" %resposta[1])
        print("Pontos: %s" %resposta[2])
        print("------------------------------\n")
      a = False

def nada(resposta):
  print("Nada Aconteceu")
  print("------------------------------")
  print("Vida: %s \n" %resposta[1])
  print("Pontos: %s" %resposta[2])
  print("------------------------------\n")
 
if __name__ == '__main__':
  print("Bem Vindo ao Jogo \n")
  print("------------------------------")
  print("Vida: 100 \n")
  print("Pontos: 0")
  print("------------------------------\n")
  host = 'localhost'
  port = 12000
  connection = socket(AF_INET, SOCK_STREAM)
  connection.connect((host,port))
  inicio = bytes('START', encoding='utf8') 
  connection.sendto(inicio,(host,port))  
  a = True
  while a:
    data = connection.recv(1024)
    resposta = str(data, 'utf-8')
    resposta = resposta.split(';')
    if resposta[0] == 'MONSTER_ATTACK':
      aux = int(resposta[1])
      print("------------------------------ MONSTRO ------------------------------\n")
      monstro(aux)
      a = bytes('WALK', encoding='utf8') 
      connection.sendto(a,(host,port))  
    elif resposta[0] == 'TAKE_CHEST':
      print("------------------------------ BAU ------------------------------\n")
      bau()
      a = bytes('WALK', encoding='utf8') 
      connection.sendto(a,(host,port))  
    elif resposta[0] == 'BOSS_EVENT':
      print("------------------------------ CHEFAO ------------------------------\n")
      chefao()
      a = bytes('WALK', encoding='utf8') 
      connection.sendto(a,(host,port))  
    elif resposta[0] == 'NOTHING_HAPPENED':
      print("------------------------------ Nada Aconteceu ------------------------------\n")
      nada(resposta)
      a = bytes('WALK', encoding='utf8') 
      connection.sendto(a,(host,port)) 
    elif resposta[0] == 'WIN':
      print("------------------------------ VITORIA ------------------------------\n")
      print("VOCÊ VENCEU!! \n")
      print("Salas Visitadas: %s \n" %resposta[1])
      print("Vida: %s \n" %resposta[2])
      print("Pontos: %s" %resposta[3])
      print("------------------------------")
      connection.close()
      a = False
    else:
      print("------------------------------ DERROTA ------------------------------\n")
      print("VOCÊ PERDEU!! \n")
      print("Salas Visitadas: %s \n" %resposta[1])
      print("Vida: %s \n" %resposta[2])
      print("Pontos: %s" %resposta[3])
      connection.close()
      print("------------------------------")
      a = False






