# Listas de campeões
list_tank = ["rammus", "galio", "malphite"]
list_assassin = ["rammus", "zed"]

# Builds
default = ("luden", "rabadon")
counter_assassin = ("seraph", "zhonyas")
counter_tank = ("liandry", "void")


while True:
    champions = input("Digite seu campeão: ").lower()

    # Verificar se o campeão está nas listas
    is_tank = champions in list_tank
    is_assassin = champions in list_assassin

    # Determinar a classificação
    if is_tank and is_assassin:
        classification = "tank-assassin"
    elif is_assassin:
        classification = "assassin"
    elif is_tank:
        classification = "tank"
    else:
        classification = "unknown"

    # Imprimir a build com base na classificação
    if classification == "tank":
        print("Build para tank:", counter_tank)
        break
    elif classification == "assassin":
        print("Build contra assassin:", counter_assassin)
        break
    elif classification == "tank-assassin":
        print("Build para tank:", counter_tank + counter_assassin)
        break
    else:
        print("Esse campeão não existe na lista, tente novamente.")