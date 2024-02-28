from interface import Persona

class Juan(Persona):

    def hablar(self):
        print("\tHola soy Juan")

    def comer(self):
        print("\tComer como Juan")

    def caminar(self):
        print("\tCaminar al paso de Juan")


class Pedro(Persona):
    
    def hablar(self):
        print("\tHola soy Pedro")

    def comer(self):
        print("\tComer como Pedro")

    def caminar(self):
        print("\tCaminar al paso de Pedro")


AmigoJuan = Juan()
AmigoPedro = Pedro()

print("Juan habla así:")
AmigoJuan.hablar()
print("Pedro habla así:")
AmigoPedro.hablar()
print("Juan come así:")
AmigoJuan.comer()
print("Pedro come así:")
AmigoPedro.comer()