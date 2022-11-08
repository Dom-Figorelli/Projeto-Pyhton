# INICIO DO PROGRAMA

from ast import While


print ( "**" )
print ( "Seja Bem vindo" )
print ( "*" )

CPF = 123
mesa = 3

CPFF = input ( "Digite seu CPF" )
CPFF = int ( CPFF )
comanda = 1


if (CPFF == CPF):

    print ( "Seja bem vindo " )
    if (mesa > 2):
        print ( "mesa:", mesa,"disponivel" '\n' )
        mesa = mesa - 1



else:
    print ( "Precisa efetuar seu cadastro" )
    Nome = input ( "Digite seu Nome:" )
    Email = input ( "Digite seu E-mail:" )
    print ( Nome, "cadastro efetuado com sucesso" )
    if (mesa > 2):
        print ( "mesa :", mesa,"disponivel" '\n' )
        mesa = mesa - 1


# ***** E-comanda ***** - 3 Etapa 

class faz_pedido:

    def _init_(self,comida, bebida):
        self.comida = comida
        self.bebida = bebida
        


    def pede_comida(self):
        pedido_comida_confirma = 2
        while pedido_comida_confirma == 2:
            faz_pedido.comida = input("Qual sera seu pedido para comer? \n XSALADA \n XBURGUER \n XFRANGO \n")
            print("Confirmar pedido?",faz_pedido.comida)
            pedido_comida_confirma = int(input("1 - Sim / 2 - Nao \n"))

    
    def pede_bebida(self):
        pedido_bebida_confirma = 2
        while pedido_bebida_confirma == 2:
            faz_pedido.bebida = input("Qual sera sua bebida? \n COCA \n GUARANA \n SUCO \n")
            print("Confirmar pedido?",faz_pedido.bebida)
            pedido_bebida_confirma = int(input("1 - Sim / 2 - Nao \n"))

    def envia_cozinha(resp_cozinha):
        print("Pedido na fila:",faz_pedido.comida,"prosseguir?")
        resp_cozinha = int(input("1 - Sim / 2 - Nao \n"))
        if resp_cozinha == 1:
            print("Pedido sendo feito")
        else:
            print("Refazer pedido")
        return resp_cozinha 

    def avisa_garcom(retirou):
        print("Pedido pronto!")
        retirou = int(input("Pedido retirado? 1 - Sim / 2 - Nao \n "))
        return retirou

comanda_aberta = 1
while comanda_aberta == 1:

    cozinha_confirma = 2
    while  cozinha_confirma == 2:  
        faz_pedido.pede_comida(0)
        faz_pedido.pede_bebida(0)
        cozinha_confirma = faz_pedido.envia_cozinha(0)


    pedido_retirado = 2
    while pedido_retirado == 2:
        pedido_retirado = faz_pedido.avisa_garcom(0)
    
    print("pedido a caminho")

    print("Gostaria de fazer outro pedido?")
    comanda_aberta = int(input("1 - Sim / 2 - Nao \n"))



# ***** E-comanda ***** - 4 Etapa     

print("Obrigado pela sua preferência ")
print("O valor da sua refeição foi R$50,00")
