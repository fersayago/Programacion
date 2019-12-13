"""
<>

>

<
"""

def dividirMail (mail):
    user, resto = mail.split("@")
    lisResto = resto.split(".")
    resLista = [user] + lisResto
    final = tuple(resLista)
    return final
 
inp = input("ingrese su e-mail")
    
print(dividirMail(inp))