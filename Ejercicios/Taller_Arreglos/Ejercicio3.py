def principal():
    letras = ['P', 'Z', 'B', 'E', 'C']
    valores = [3.1, 2.2, 4.1, 3.8, 1.7]
    
    quien = unMetodo(valores, letras)
    
    print(quien)
    
def unMetodo(nums, alfas):
    yo = alfas[0]
    mia = nums[0]
    i = 1
    
    while i < len(alfas):
        if nums[i] < mia:
            yo = alfas[i]
            mia = nums[i]
            
        i += 1
    
    return yo

principal()