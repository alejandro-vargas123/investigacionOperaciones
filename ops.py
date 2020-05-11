class nodo:
    def __init__(self):
        self.ic=None
        self.il=None
        self.tc=None
        self.tl=None
        self.holgura=None
        self.duracion=None
        self.relaciones=[]
        self.nombre=None


if __name__=='__main__':
    cant_nodos=int(input("Ingrese la cantidad de nodos que hay en el sistema "))
    nodos=[]
    i=0
    while i < cant_nodos:
        k=nodo()
        nombre=input("Nombre del nodo "+str(i)+": ")
        duracion=int(input("Duracion de la actividad "+str(i)+": "))
        k.nombre=nombre
        k.duracion=duracion
        print("Relaciones")
        while True:
            valor=input()
            if valor=="":
                break
            k.relaciones.append(valor)
        nodos.append(k)
        print("")
        i+=1

    i=0
    while i < cant_nodos:
        print("Informacion nodo "+str(i))
        print(nodos[i].nombre)
        print(nodos[i].duracion)
        print(nodos[i].relaciones)
        print("")
        i+=1
