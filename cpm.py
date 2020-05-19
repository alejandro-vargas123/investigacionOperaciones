from criticalpath import Node

if __name__=='__main__':
    cantidad=int(input("Ingrese la cantidad de nodos "))
    nodos=[]
    list=[]
    links=[]
    p=Node('project')
    for i in range(cantidad):
        #se capturan los nodos
        a=None
        b=str(i)
        duracion=int(input("Ingrese la duracion del nodo "+b+" :"))
        nodos.append(a)
        nodos[i]=p.add(Node(b, duration=duracion))

    print("ingrese las relacion por pares")
    print("Se termina con un espacio en blanco")
    while True:
        list=[]
        valor1=input()
        if valor1=="":
            break
        valor2=input()
        valor1=int(valor1)
        valor2=int(valor2)
        list.append(nodos[valor1])
        list.append(nodos[valor2])
        list=tuple(list)
        links.append(list)
        print()

    for link in links:
        p.link(*link)

    p.update_all()

    print(p.get_critical_path())
    print(p.duration)
