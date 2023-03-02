# script calacular o imc de um individo 
# usar variaveis, guardar o resulatado e imprimir esse valor
# alem do valor informar a condição do individo


peso = float(input('qual e seu peso (Kg)'))

altura = float (input('qual e a sua altura (m)'))

imc = peso / (altura **2)
print('o imc e de {:.1f}'.format(imc))

if imc < 18.4:
    print('voce esta abaixo do peso') 
elif 18.4 <= imc < 23:
    print('voce esta no peso ideal')   
elif 23 <= imc < 30:
    print('voce esta acima do peso')
elif 30 <= imc < 40:
    print('voce esta em obesidade')
elif imc >= 40:
    print('voce esta super obeso cuidado!')