# fonction pour calculer le pgcd
def calcul_pgcd(a,b):
    while b !=0:
        r = a % b
        a = b
        b = r

        return a
    

try:
    while True:
        # Entrer des nombres
        a = int(input("Entrez le premier nombre (entier positif) :"))
        b = int(input("Entrez le deuxième nombre (entier positif) :"))

        if a <= 0 or b <=0:
            raise ValueError("Les nombres doivent être des entiers positifs non nuls. Fin du programme.")
        
        # calcul et affichage du résultat
        result = calcul_pgcd(a,b)
        print(f'Le PGCD de {a} et {b} = {result}')

except ValueError as e:
    print(f"Erreur : {e}")         

