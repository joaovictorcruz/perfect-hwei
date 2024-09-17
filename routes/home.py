from flask import Blueprint, render_template, request, jsonify

home_route = Blueprint('home', __name__)

# Listas de campeões
list_bruiser = ["sylas", "irelia", "yone", "yasuo"]
list_mage = ["orianna", "viktor", "aurelion sol", "vladmir", "veigar", "neeko", "syndra", "azir"]
list_tank = ["galio", "malphite", "sion"]
list_assassin = ["zed", "ahri", "akali", "annie", "diana", "fizz", "qyiana", "kassadin", "aurora"]
list_ranged = ["jayce", "tristana", "corki", "zeri", "lucian", "smolder", "akshan", "ezreal"]

builds = {
    "default": [("luden", "static/images/items/luden.png"), ("rabadon", "/static/images/items/rabadon.png")],
    "counter_assassin": [("seraph", "static/images/items/Cajado_do_Arcanjo_item.webp"), ("zhonyas", "/static/images/items/zhonias.png")],
    "counter_tank": [("liandry", "static/images/items/liandry.png"), ("void", "/static/images/items/cajadoVazio.png")]
}

runes = {
    "default": [("static/images/runes/runaimg-removebg-preview.png")],
    "counter_assassin": [("static/images/runes/counter_assassin.png")]
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

    if is_tank and is_assassin:
        build = builds["counter_tank"] + builds["counter_assassin"]
        rune = runes["default"]  # Escolha padrão se ambos se aplicam
    elif is_tank:
        build = builds["counter_tank"]
        rune = runes["default"]
    elif is_assassin:
        build = builds["counter_assassin"]
        rune = runes["counter_assassin"]
    else:
        build = builds["default"]
        rune = runes["default"]

    # Retorna a build e runas como uma resposta JSON
    return jsonify({'build': build, 'rune': rune})