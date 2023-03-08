def imc():
      
  peso = input('qual é seu peso:' )
  peso_srt= float(peso)
  altura = input('qual é a sua altura')
  altura_srt= float(altura)
  
  
  imc = peso_srt / (altura_srt** 2)
  print('O imc é de:{:.1f}'.format(imc))
   
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
         


imc()
  
  


















