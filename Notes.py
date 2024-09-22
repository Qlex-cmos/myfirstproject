def main ():
    # récolter une premiere note
    note1 = int(input("Entrez la première note"))
    # récolter une seconde note
    note2 = int(input("Entrez la seconde note"))
    # récolter une troisieme note
    note3 = int(input("Entrez la troisieme note"))
    # calculer la moyenne
    result = (note1 + note2 + note3) / 3
    # afficher le resultat
    print("la moyenne de l'élève est  " + str(result))




if __name__ == '__main__':
    main()