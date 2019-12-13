"""
<>

>

<
"""
try:
    a = int(input("ingrese un valor minimo del rango"))
    b = int(input("ingrese un valor maximo del rango"))
    
    
    def rangoDeNum (mini, maxi, lis = []):
        assert mini<=maxi
        if mini == maxi:
            lis.append(mini)
            return lis
        else:
            lis.append(mini)
            return rangoDeNum(mini + 1, maxi, lis)
        
    print(rangoDeNum(a, b))
   
except AssertionError:
    print("el primer numero debe ser menor o igual que el segundo")


    
    

