# COMPREHENSION LIST

frutas = ["Manzana","Pera","Banana","Mandarina","Fresa"]
frutas_con_e = [fruta for fruta in frutas if "e" in fruta]
frutas_sin_banana = [fruta for fruta in frutas if fruta != "Banana"]
frutas2 = [fruta if fruta != "Pera" else "Aguacate" for fruta in frutas ]
# for fruta in frutas:
#     if "e" in fruta:
#         frutas_con_e.append(fruta)

print(frutas_con_e)
print(frutas_sin_banana)
print(frutas2)
# for fruta in frutas:
#     if fruta != "Banana":
#         frutas_sin_banana.append(fruta)
# print(frutas_sin_banana)