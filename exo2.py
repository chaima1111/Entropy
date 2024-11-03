import math

def calculer_entropie(probabilites):
    entropie = 0
    for p in probabilites:
        if p > 0:
            entropie -= p * math.log2(p)
    return entropie


def entropieConjointe(distribution_conjointe):
    """
    Calcule l'entropie conjointe H(X, Y) pour une distribution de probabilité conjointe donnée.
        """
    entropie = 0.0
    for (x, y), p_xy in distribution_conjointe.items():
        if p_xy > 0:  # On ignore les probabilités nulles car log(0) est indéfini
            entropie -= p_xy * math.log2(p_xy)
    return entropie


def calculer_entropie_conditionnelle(entropie_conjointe, entropie_Y):
    """
    Calcule l'entropie conditionnelle H(X|Y).
    """
    return entropie_conjointe - entropie_Y


def calculer_information_mutuelle(entropie_X, entropie_conditionnelle):
    """
    Calcule l'information mutuelle entre deux sources.
    """
    return entropie_X  - entropie_conditionnelle


# Exemple d'utilisation
# Probabilités marginales de X et Y
probabilites_X = [0.5, 0.5]
probabilites_Y = [0.6, 0.4]

# Probabilités conjointes P(X/ Y)
# p(x1/y1) p(x1/y2) p(x2/y1) p(x2/y2)
probabilites_conjointes = [3/5,1/5,1/3,2/3 ]

distribution_conjointe = {
    (0, 0): 0.25,
    (0, 1): 0.45,
    (1, 0): 0.15,
    (1, 1): 0.25
}

# Calcul des entropies
entropie_X = calculer_entropie(probabilites_X)
entropie_Y = calculer_entropie(probabilites_Y)
# on appelle la fonction ou on fait cette formule
h_xy = entropieConjointe(distribution_conjointe)#H(X,Y)
entropie_conditionnelle = calculer_entropie_conditionnelle(h_xy,entropie_X)
# Calcul de l'information mutuelle et de l'entropie conditionnelle
information_mutuelle = calculer_information_mutuelle(entropie_X,entropie_conditionnelle);

# Affichage
print("Entropie de X:", entropie_X)
print("Entropie de Y:", entropie_Y)
print(f"L'entropie conjointe H(X, Y) est : {h_xy:.4f} bits")
print("Information mutuelle I(X; Y):", information_mutuelle)
