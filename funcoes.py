def calc_imc(peso, altura):      
  imc = peso / (altura * altura)
  print('O imc é de: {:.1f}'.format(imc))
   
  if imc < 18.8:
        print('você esta abaixo do peso')
  elif imc >= 18.8 < 25:
        print('você esta no peso ideal')
  elif imc >= 25 < 45:
        print ('você esta acima do peso')
  elif imc >= 45 < 65:
        print ('você esta em obesidade')
  elif imc >= 65:
        print ('você esta super obeso cuidado')
        
  print()
         
          

def opcao1( ):
      peso_str = input('qual é seu peso: ')
      peso = float(peso_str)
      altura_str = input('qual é a sua altura: ')
      altura = float(altura_str)
      calc_imc(peso, altura)
            
      print()


def opcao2():
      pessoas = [(1.85, 70), (1.50, 68), (1.76, 67)]
      for pessoa in pessoas:
            peso = pessoa[1]
            altura = pessoa[0]
            calc_imc(peso, altura)
      
def opcao3():
      pass

        
      
print('''[1] Entrar com peso e altura 
      [2] processar lista de pessoas
      [3] batata''')

x = input ('digite uma opção')

if x == '1':
      opcao1()
      
if x == '2':
      opcao2()

if x == '3':
      opcao3()

 
#1) Entrar com peso e altura
#2) Processar lista de pessoass