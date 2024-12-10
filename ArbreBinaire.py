from File import *

class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfantGauche = None
        self.enfantDroit = None
    
    def setGauche(self, valeur):
        if self.enfantGauche == None:
            self.enfantGauche = Noeud(valeur)
        else :
            newNode = Noeud(valeur)
            newNode.enfantGauche = self.enfantGauche
            self.enfantGauche = newNode
    
    def setDroit(self, valeur):
        if self.enfantDroit == None:
            self.enfantDroit = Noeud(valeur)
        else :
            newNode = Noeud(valeur)
            newNode.enfantDroit = self.enfantDroit
            self.enfantDroit = newNode
    
    def getValeur(self):
        return self.valeur
    
    def getGauche(self):
        return self.enfantGauche
    
    def getDroit(self):
        return self.enfantDroit
    


    
def affiche(arbre: Noeud):
    if arbre != None:
        return (arbre.getValeur(), affiche(arbre.getGauche(), affiche(arbre.getDroit())))
    
def hauteur(arbre: Noeud):
    if arbre == None:
        return 0
    else :
        return 1 + max(hauteur(arbre.getGauche(), hauteur(arbre.getDroit())))
    
def taille(arbre: Noeud):
    if arbre == None:
        return 0
    else :
        return 1 + taille(arbre.getGauche()) + taille(arbre.getDroit())
    
def parcoursInfixe(arbre: Noeud):
    if arbre != None:
        parcoursInfixe(arbre.getGauche())
        print(' -', arbre.getValeur, end = '')
        parcoursInfixe(arbre.getDroit())

def parcoursSuffixe(arbre: Noeud):
    if arbre != None:
        parcoursSuffixe(arbre.getGauche())
        parcoursSuffixe(arbre.getDroit())
        print(' -', arbre.getValeur(), end = '')

def parcoursPrefixe(arbre: Noeud):
    if arbre != None:
        print(' -', arbre.getValeur(), end = '')
        parcoursPrefixe(arbre.getGauche())
        parcoursPrefixe(arbre.getDroit())

def parcoursLargeur(arbre: Noeud):
    if arbre != None:
        file = File()
        file.enfiler(arbre)
        while not file.est_vide():
            noeud = file.defiler()
            print(' -', noeud.getValeur(), end = '')
            if noeud.getGauche() != None:
                file.enfiler(noeud.getGauche())
            if noeud.getDroit() != None:
                file.enfiler(noeud.getDroit())

def afficheNiveau(arbre: Noeud, niveau):
    if arbre != None:
        if niveau == 1:
            print(' -', arbre.getValeur(), end = '')
        else:
            afficheNiveau(arbre.getGauche(), niveau - 1)
            afficheNiveau(arbre.getDroit(), niveau - 1)

def parcoursLargeur2(arbre: Noeud):
    h = hauteur(arbre)
    for i in range(1, h + 1):
        afficheNiveau(arbre, i)

def rechercheBST(arbre: Noeud, k):
    if arbre == None:
        return False
    if arbre.getValeur() == k:
        return True
    elif k < arbre.getValeur():
        return rechercheBST(arbre.getGauche(), k)
    else :
        return rechercheBST(arbre.getDroit(), k)
    
def insererBTS(arbre: Noeud, k):
    while arbre != None:
        arbre2 = arbre
        if arbre.getValeur() > k:
            arbre = arbre.getGauche()
        else:
            arbre = arbre.getDroit()
    if arbre2.getValeur() > k:
        arbre2.setGauche(k)
    else:
        arbre2.setDroit(k)

def minimum(arbre: Noeud):
    current = arbre
    while current.getGauche() is not None:
        current = current.getGauche()
    return current.getValeur()

def supprimeBTS(arbre: Noeud, k):
    if arbre == None:
        return arbre
    if k < arbre.getValeur():
        arbre.enfantGauche = supprimeBTS(arbre.getGauche(), k)
    elif k > arbre.getValeur():
        arbre.enfantDroit = supprimeBTS(arbre.getDroit(), k)
    else:
        if arbre.getGauche() == None:
            return arbre.getDroit()
        elif arbre.getDroit() == None:
            return arbre.getGauche()
        arbre.valeur = minimum(arbre.getDroit())
        arbre.enfantDroit = supprimeBTS(arbre.getDroit(), arbre.getValeur())
    return arbre