osoby = int(input("Počet osob: "))
# Základní cena vstupenky
cena = 500
sleva = ""

# Pokud je osob 4 nebo více, přeskočí se dotazy na věk
if osoby >= 4:
    cena = cena * 0.75
    sleva = "Skupinová sleva 25%"
else:
    # Zeptá se na věk a studenta jen v případě, že je osob méně než 4
    vek = int(input("Zadej věk: "))
    student = input("Student (ano/ne): ")
    
    if vek < 26 and student == "ano":
        cena = cena * 0.70
        sleva = "Studentská sleva 30%"
    elif vek >= 65:
        cena = cena * 0.80
        sleva = "Seniorská sleva 20%"
    else:
        sleva = "Bez slevy"

celkem = cena * osoby

print("---Vstupenka---")
print("Typ slevy:", sleva)
print("Cena za vstupenku:", cena, "Kč")
print("Celková cena:", celkem, "Kč")