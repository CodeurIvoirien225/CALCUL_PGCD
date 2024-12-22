def pgcd_euclide(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


a = int(input("Entrez le premier nombre 'a' :"))
b = int(input("Entrez le deuxième nombre 'b' :"))

result = pgcd_euclide(a,b) 

print(f"Le PGCD est : {result}") 

