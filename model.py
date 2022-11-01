from flask import Flask

Calculo = [
    {
      'id': 1,
      'name': 'Numero 1',  
    },
    
    {
      'id': 2,
      'name': 'Numero 2',
    },
    
    {
      'id': 3,
      'name': 'Numero 3',
    }
]

class Calculo():
    def calcular(n, n1):
        calcular = n + n1
        
        return { 'resultado': calcular }
    
    def jsonReturn():
        return calcular