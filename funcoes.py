def imc():
    pesoimc  = input ('informe seu peso')
    peso = float (pesoimc)
    alturaimc = input ('informe sua altura')
    altura = float (alturaimc)
    imc = pesoimc / (alturaimc**2)
    print('o imc é de {:.1f}'.format(imc))
    
    
if imc < 18.8:
    print('voce esta abaixo do peso')
elif 18.8 <= imc < 25:
    print('voce esta no peso ideal')
elif 23 <= imc < 45:
    print ('vc esta acima do peso')
elif 30 <= imc < 60:
    print('voce esta em obesidade')
elif imc >= 65:
    print('voce esta super obeso cuidado!')
    