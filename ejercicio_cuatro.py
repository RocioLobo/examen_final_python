"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""
lista_alumnos=[
   

{
        "nombre":"abel",
        "edad":36,
        "semestre":2,
        "ciclo":"III",
        "programa_estudio":"mecanica"
        
        
   
    },
    {
        "nombre":"edith",
        "edad":50,
        "semestre":2,
        "ciclo":"II",
        "programa_estudio":"enfermeria"
        
        

    }
]

#1. crear un funcion que me imprima los registro,

print(f"lista_alumnos")

#2. crear una funcion que me ´permita editar uno de los campos del registro
lista_alumnos[1]["edad"]=12
print(lista_alumnos)
