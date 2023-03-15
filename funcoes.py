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
         


def calc_imclist(peso_list, altura_list):
      list_imc = peso_list /(altura_list * altura_list)
      print('O list_imc é de:{:.1f}'.format(list_imc))
      
      if list_imc < 18.8:
            print('voce esta abaixo do peso')
      elif list_imc >= 18.8 < 25:
        print('voce esta no peso ideal')
      elif list_imc >= 25 < 45:
            print ('voce esta acima do peso')
      elif list_imc >= 45 < 65:
            print ('voce esta em obesidade')
      elif list_imc >= 65:
            print('voce esta super obeso cuidado')
      
      print()
      

      

print('''[1] Entrar com peso e altura 
      [2] processar lista de pessoas''')
print(input('digite a opção:'))
    
opcao1 = calc_imc
print(input('digite a opção'))

peso_str = input('qual é seu peso: ')
peso = float(peso_str)
altura_str = input('qual é a sua altura: ')
altura = float(altura_str)
calc_imc(peso, altura)

opcao2= calc_imclist
print(input('segunda opção'))


pessoas = [(1.85, 70), (1.50, 68), (1.76, 67)]
for pessoa in pessoas:
      peso_list = pessoa[1]
      altura_list = pessoa[0]
      calc_imclist(peso_list, altura_list)
 


      


# criar intreface com usuario e entrar com o peso e altura 
#1) Entrar com peso e altura
#2) Processar lista de pessoass
