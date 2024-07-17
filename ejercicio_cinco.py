"""
Crear una funcion que me me retorne un diccionario con los datos personales de un alumno
ejm:
entrada: ("jose","alvarez","30","APSTI","III")
salida: {nombre:"jose",apellido:"alvarez",edad:"30",programa_estudio:"APSTI",semestre:"III"}
"""


nombre="jose"
apellido="alvarez"
programa_estudio="APSTI"
semestre="III"
def alumno(nombre,apellido,programa_estudio,semestre):
    return{
        "nombre":"jose",
        "apellido":"alvarez",
        "programa_estudio":"APSTI",
        "semestre":"III"

    }
print(alumno(nombre,apellido,programa_estudio,semestre))
