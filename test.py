def main():
    # création d'une variable usermane ayant pour valeur la chaîne de caractères Alex
    username = "Alex"
    # création de la variable age
    age = 42
    # porte-monnaie d'une personne
    wallet = 125.7
    # varianle bouléen
    is_happy = True
    #print("Hello world")
    #print("Salut Alex")

    # changer valeur variable à la volée
    age = 52

    print(username, age)
    age = age + 1
    print(username, age)

    print("Salut " + username + " vous avez " + str(age) + " ans")

if __name__ == '__main__':
    main()