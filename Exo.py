def main ():
    # récolter une valeur porte-monnaie
    wallet = int(input("Entrez la valeur de votre porte-monnaie"))
    # créer un produit qui aura une valeur 50
    item = 50
    # afficher la nouvelle valeur du porte-monnaie après son achat
    print(wallet - item)

if __name__ == '__main__':
    main()