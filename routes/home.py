from flask import Blueprint, render_template, request, jsonify

home_route = Blueprint('home', __name__)

# Listas de campeões
list_tank = ["rammus", "galio", "malphite"]
list_assassin = ["rammus", "zed"]

# Builds
default = [("luden", "/static/images/luden.png"), ("rabadon", "/static/images/rabadon.png")]
counter_assassin = [("seraph", "/static/images/Cajado_do_Arcanjo_item.webp"), ("zhonyas", "/static/images/zhonias.png")]
counter_tank = [("liandry", "/static/images/liandry.png"), ("void", "/static/images/cajadoVazio.png")]

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
        build = counter_tank + counter_assassin
    elif is_tank:
        build = counter_tank
    elif is_assassin:
        build = counter_assassin
    else:
        build = ["luden", "rabadon"]  # Default build

    # Retorna a build como uma resposta JSON
    return jsonify({'build': build})