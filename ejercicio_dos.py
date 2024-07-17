"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
impares=[4,8,2,5,7,10,6,5,3,20]
impares=list(filter(lambda n:n%2!=0,impares))  
print(impares)