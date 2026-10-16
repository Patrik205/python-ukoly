x = int(input("Zadej hodinu (0-23): "))

# 1. Kontroly na neplatné hodnoty
if x < 0:
    print("Hodina nemůže být záporná.")
elif x > 23:
    print("Zadávejte platné hodiny.")

# 2. Správné části dne
elif x < 5:
    print("Dobrou noc!")
elif 5 <= x < 9:
    print("Dobré ráno!")
elif 9 <= x < 11:
    print("Dobré dopoledne!")
elif x == 12:
    print("Dobré poledne!")
elif 12 < x < 16:
    print("Dobré odpoledne!")
elif 16 < x <= 22:
    print("Dobrý večer!")
else:
    print("Dobrou noc!")