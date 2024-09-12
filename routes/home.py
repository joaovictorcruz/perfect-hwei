from flask import Blueprint, render_template, request, jsonify

home_route = Blueprint('home', __name__)

# Listas de campeões
list_tank = ["rammus", "galio", "malphite"]
list_assassin = ["rammus", "zed"]

builds = {
    "default": [("luden", "/static/images/items/luden.png"), ("rabadon", "/static/images/items/rabadon.png")],
    "counter_assassin": [("seraph", "/static/images/items/Cajado_do_Arcanjo_item.webp"), ("zhonyas", "/static/images/items/zhonias.png")],
    "counter_tank": [("liandry", "/static/images/items/liandry.png"), ("void", "/static/images/items/cajadoVazio.png")]
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
    elif is_tank:
        build = builds["counter_tank"]
    elif is_assassin:
        build = builds["counter_assassin"]
    else:
        build = builds["default"]  # Default build

    # Retorna a build como uma resposta JSON
    return jsonify({'build': build})