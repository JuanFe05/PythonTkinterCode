def principal():
    valores = [60, 2.5, 3.0, 1.0, 4.0]
    
    ans = generar(valores)
    
    print(ans)
    
def generar(vector):
    counter = 0
    
    while counter < len(vector):
        vector[counter] = vector[counter] * (counter + 1)
        counter = counter + 1
        
        reporte = "Valores "
        counter = 0
        
        while counter < len(vector):
            reporte = reporte + str(vector[counter]) + " "
            counter = counter + 1
            
            return reporte
        
principal()
        
        