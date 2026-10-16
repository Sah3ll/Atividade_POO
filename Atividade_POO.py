# Questão 1 e 2
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.set_idade(idade)

    def set_idade(self):
        return self._idade

    def set_idade(self, nova_idade):
        if nova_idade>= 0:
            self._idade = nova_idade
        else:
            print(f"Erro: A idade para{self.nome}, idade: {self._idade} anos")
            self._idade = 0
    # 3)
    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade:  {self._idade} anos")

    def emitir_som(self):
        print("O animal está emitindo um som")


    # 4)
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
      def emitir_som(self):
        print("Miau")

class Passaro(Animal):
    def emitir_som(self):
        print("Piu piu")


class Animal:
    def _init_(self, nome, idade):
        self.nome = nome
        self.set_idade(idade) 

cachorro = Cachorro("Rex", 3)
gato = Gato("Miau", 2)
passaro = Passaro("Loro", 1)

animais = [cachorro, gato, passaro] 

for animal in animais:
        animal.exibir_dados()
        animal.emitir_som()
        print("-" * 25)


