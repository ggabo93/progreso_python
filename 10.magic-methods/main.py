from clases.mago import Mago

mago1 = Mago("Merlin", ["Bola de fuego", "Volar"])
mago2 = Mago("Dark Magician", ["Bola de aire", "Volar"])
mago3 = Mago("Merlin", ["Bola de fuego", "Volar"])

print(mago1.__str__())
print(mago2.__str__())

print(mago1.__eq__(mago2))
print(mago1.__eq__(mago3))
