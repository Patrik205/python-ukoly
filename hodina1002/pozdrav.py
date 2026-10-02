
x = int(input("Zadej hodinu (0-23): ")) # otázka na uživatele, aby zadal hodinu
if x<0:
    print("hodina nemůže být mimo rozsah 0-23") # vypise chybu, pokud je zadana hodina mimo rozsah
if x< 5:
    print("dobrou noc") # vypise dobrou noc
elif x<=9:
    print("dobré ráno")
elif x<12:
    print("dobré dopoledne")
elif x==12:
    print("dobré poledne")
elif x<16:
    print("dobré odpoledne")
elif x<22:
    print("dobrý večer")
else: x>=22
print("dobrou noc")
