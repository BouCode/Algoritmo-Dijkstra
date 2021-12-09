grafo = { "A" : { "B" : 1},
          "B" : { "C" : 5, "F" : 1},
          "C" : { "D" : 3, "G" : 3},
          "D" : {"E": 2, "H":3},
          "E" : {"I": 4},
          "F" : {"G": 2},
          "G" : {"H": 2}, 
          "H" : {"I": 1},
          "I" : {"J": 2},
          "J" : {},
          }

def dijkstra(grafo, origen): 

    control = { }
    distanciaActual = { }
    noActual = { }
    noVisitados = []
    actual = origen
    noActual[actual] = 0

    
    for vertice in grafo.keys():
        noVisitados.append(vertice)  
        distanciaActual[vertice] = float('inf')

    distanciaActual[actual] =0

    noVisitados.remove(actual)

    while noVisitados:
        for vecino, peso in grafo[actual].items():
             pesoCalc = peso + noActual[actual]
             if distanciaActual[vecino] == float("inf") or distanciaActual[vecino] > pesoCalc:
                 distanciaActual[vecino] = pesoCalc
                 control[vecino] = distanciaActual[vecino]

        if control == {} : break    
        minVecino = min(control.items(), key=lambda x: x[1])
        actual=minVecino[0]
        noActual[actual] = minVecino[1]
        noVisitados.remove(actual)
        del control[actual]

    print(distanciaActual)


def dijkstra_path(grafo, origen, fin): 

    control = { }
    distanciaActual = { }
    noActual = { }
    noVisitados = []
    actual = origen
    noActual[actual] = 0

    
    for vertice in grafo.keys():
        noVisitados.append(vertice)   
        distanciaActual[vertice] = float('inf') 

    distanciaActual[actual] = [0,origen] 

    noVisitados.remove(actual)

    while noVisitados:
        for vecino, peso in grafo[actual].items():
             pesoCalc = peso + noActual[actual]
             if distanciaActual[vecino] == float("inf") or distanciaActual[vecino][0] > pesoCalc:
                 distanciaActual[vecino] = [pesoCalc,actual]
                 control[vecino] = pesoCalc
                 print(control)
                 
        if control == {} : break    
        minVecino = min(control.items(), key=lambda x: x[1])
        actual=minVecino[0]
        noActual[actual] = minVecino[1]
        noVisitados.remove(actual)
        del control[actual]

    print("La menor distancia de %s hasta %s es: %s" % (origen, fin, distanciaActual[fin][0]))
    print("El mejor camino es: %s" % printPath(distanciaActual,origen, fin))          
    
def printPath(distancias,inicio, fin):
        if  fin != inicio:
            return "%s -- > %s" % (printPath(distancias,inicio, distancias[fin][1]),fin)
        else:
            return inicio

dijkstra_path(grafo,"A","J")

