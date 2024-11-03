import math

def calculer_entropie(proba):
    """
    on a H(x) -= (p(x).log(p(x)))
    """
    entropie = 0
    for p in proba:
        if p > 0:
            entropie -= p * math.log2(p)
    return entropie

# Exemple d'utilisation
# Probabilités de chaque symbole (exemple avec une source à 4 symboles)
proba = [1/2, 1/8, 1/6, 1/2]  # Source uniforme
entropie = calculer_entropie(proba)
print("L'entropie de la source est:", entropie)
