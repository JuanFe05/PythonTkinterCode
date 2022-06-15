def generarSerie(n):
    c = 0
    serie = ""
    t = 1
    
    while c < n:
        serie = serie + str(t) + " "
        t = (t * t) + 1
        c = c + 1
        
    return serie
    
def principal():
    n = int(input("Ingrese un número: "))
    
    while n <= 0:
        n = int(input("Ingrese un número: "))
    
    serie = generarSerie(n)
    
    print(serie)
    
principal()