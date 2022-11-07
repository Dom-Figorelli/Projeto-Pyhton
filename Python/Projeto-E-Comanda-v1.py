# INICIO DO PROGRAMA

print("**")
print( "Seja Bem vindo")
print("*")

CPF = 123
mesa =3

CPFF=input("Digite seu CPF")
CPFF = int(CPFF)
comanda = 1
valor1= int(1) 
valor2 = int(2)
Total= valor1 + valor2

if (CPFF == CPF):

  print("Seja bem vindo ")
  if (mesa >2):
        print("vou te levar para mesa:" ,mesa ,'\n' )
        mesa = mesa - 1
 
  
  
else:
  print("Precisa efetuar seu cadastro")
  Nome = input("Digite seu Nome:")
  Email = input("Digite seu E-mail:")
  print(Nome, "cadastro efetuado com sucesso")
  
  
  class comanda:
    def _init_ (self,Nome,CPF):
      self.Nome = Nome
      self.CPF = CPF
      from comanda import comanda
      comanda = comanda("Wilson",32791  )
      comanda.Nome


# ************** E-comanda ************** - 3 Etapa 

pedido1=input("Qual sera seu pedido para comer? \n XSALADA \n XBURGUER \n XFRANGO \n")
pedido2=input("Qual sera sua bebida? \n COCA \n GUARANA \n SUCO \n")

def envia_cozinha():
    print("FUNCAO ENVIA PEDIDO PRA COZINHA")


print("Confirme seu pedido:", pedido1, pedido2)

ClienteConfirma = input("Seu pedido esta correto? 1 = Sim 2=Nao \n")

if ClienteConfirma == "1":
    envia_cozinha()
else: 
    print("FUNCAO VOLTA PARA ESCOLHA DE PEDIDOS")
    