pets = {}
pets2 = {}

print("Введите кличку питомца:")
name = input()
        
print("Введите вид питомца: ")
type = input()
        
print("Введите возраст питомца: ")
years = int(input())
if (years == 1) or (years == 21):
    yearsUpd = str(years) + " год."
elif (5 > years > 1) or (25 > years > 21) or (35 > years > 31):
    yearsUpd = str(years) + " года."
elif (21 > years > 4) or (24 < years < 31):
    yearsUpd = str(years) + " лет."
        
print("Введите имя владельца: ")
petMastrName = input()

pets2 = {"Вид питомца":type,"Возраст питомца":yearsUpd,"Имя владельца":petMastrName}
pets[name] = pets2
        
print("Это", list(pets2.values())[0], "по кличке", list(pets.keys())[0], ".", "Возраст питомца:", list(pets2.values())[1], "Имя владельца:", list(pets2.values())[2])