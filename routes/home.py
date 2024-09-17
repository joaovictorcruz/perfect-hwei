from flask import Blueprint, render_template, request, jsonify

home_route = Blueprint('home', __name__)

# Listas de campeões
list_bruiser = ["sylas", "irelia", "yone", "yasuo"]
list_mage = ["orianna", "viktor", "aurelion sol", "vladmir", "veigar", "neeko", "syndra", "azir"]
list_tank = ["galio", "malphite", "sion"]
list_assassin = ["zed", "ahri", "akali", "annie", "diana", "fizz", "qyiana", "kassadin", "aurora"]
list_ranged = ["jayce", "tristana", "corki", "zeri", "lucian", "smolder", "akshan", "ezreal"]

builds = {
    "default": [("Companheiro de Luden", "static/images/items/luden.png"), ("Botas ionianas da lucidez", ""), ("Foco do Horizonte", ""), ("Capuz da Morte de Rabadon", "/static/images/items/rabadon.png"), ("Criptoflora", ""), ("Véu de Banshee", "")],
    "counter_assassin": [("Abraço de Seraph", "static/images/items/Cajado_do_Arcanjo_item.webp"), ("Botas ionianas de Lucidez", ""), ("Zhonias", "/static/images/items/zhonias.png "), ("Rabadon", ""), ("Criptoflora", ""), ("Chama Sombria", "")],
    "counter_tank": [("Abraço de Seraph", "static/images/items/Cajado_do_Arcanjo_item.webp"), ("Botas ionianas de Lucidez", ""), ("Angústia de Liandry", "static/images/items/liandry.png"), ("Cajado do Vazio", "/static/images/items/cajadoVazio.png"), ("Capuz da Morte de Rabadon", "/static/images/items/rabadon.png"), ("Ladrão de Almas Mejai", "")],
    "counter_bruiser": [("Abraço de Seraph", "static/images/items/Cajado_do_Arcanjo_item.webp"), ("Botas Galvanizadas de Aço", ""), ("Angústia de Liandry", "static/images/items/liandry.png"), ("Capuz da Morte de Rabadon", "/static/images/items/rabadon.png"),  ("Criptoflora", ""), ("Zhonias", "/static/images/items/zhonias.png ")]
}

runes = {
    "default": [("static/images/runes/runaimg-removebg-preview.png")],
    "counter_assassin": [("static/images/runes/counter_assassin.png")],
    "counter_tank": [("static/images/runes/counter_tank.png")]
}

@home_route.route('/')
def home():
    return render_template('index.html')

@home_route.route('/get_build', methods=['POST'])
def get_build():
    data = request.json
    champion = data.get('champion').lower()

    # Verificar a classificação do campeão
    is_tank = champion in list_tank
    is_assassin = champion in list_assassin
    is_bruiser = champion in list_bruiser

    if is_tank and is_assassin:
        build = builds["counter_tank"] + builds["counter_assassin"]
        rune = runes["default"]  # Escolha padrão se ambos se aplicam
    elif is_tank:
        build = builds["counter_tank"]
        rune = runes["counter_tank"]
    elif is_assassin:
        build = builds["counter_assassin"]
        rune = runes["counter_assassin"]
    elif is_bruiser:
        build = builds["counter_bruiser"]
        rune = runes["counter_assassin"]
    else:
        build = builds["default"]
        rune = runes["default"]

    # Retorna a build e runas como uma resposta JSON
    return jsonify({'build': build, 'rune': rune})