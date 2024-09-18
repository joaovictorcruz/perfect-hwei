from flask import Blueprint, render_template, request, jsonify

home_route = Blueprint('home', __name__)

# Listas de campeões
list_bruiser = ["sylas", "irelia", "yone", "yasuo"]
list_mage = ["orianna", "viktor", "aurelion sol", "vladmir", "veigar", "neeko", "syndra", "azir"]
list_tank = ["galio", "malphite", "sion"]
list_assassin = ["zed", "ahri", "akali", "annie", "diana", "fizz", "qyiana", "kassadin", "aurora"]
list_ranged = ["jayce", "tristana", "corki", "zeri", "lucian", "smolder", "akshan", "ezreal"]
list_default = [
    "aatrox", "ahri", "akali", "alistar", "amumu", "anivia", "aphelios", "ashe", "bard", "blitzcrank", 
    "brand", "braum", "caitlyn", "camille", "cassiopeia", "cho'gath", "dr. mundo", "draven", 
    "ekko", "elise", "evelynn", "fiora", "gangplank", "gnar", "gragas", "graves", "hecarim", "illaoi", 
    "ivern", "janna", "jax", "jhin", "jhinx", "kalista", "karma", "karthus", "katarina", "kayle", 
    "kayne", "kennen", "kog'maw", "leblanc", "leesin", "leona", "lissandra", "lulu", "lux", 
    "maestro yi", "maokai", "miss fortune", "mordekaiser", "morgana", "nami", "nasus", "nautilus", 
    "nidalee", "nocturne", "nunu", "olaf", "ornn", "pantheon", "poppy", "pyke", "quinn", "rammus", 
    "rek'sai", "renekton", "rengar", "riven", "ryze", "sejuani", "seraphine", "sett", "shaco", 
    "shen", "shyvana", "singed", "skarner", "sona", "soraka", "swain", "tahm kench", "taliyah", 
    "talon", "taric", "teemo", "thresh", "trundle", "tryndamere", "twisted fate", "twitch", 
    "urgot", "varus", "vayne", "vex", "vi", "viego", "volibear", "warwick", "wukong", "xayah", 
    "xerath", "yasuo", "yorick", "yuumi", "zac", "zilean", "zoe", "zyra"
]

builds = {
    "default": [("Companheiro de Luden", "static/images/items/luden.png"), ("Botas Ionianas da Lucidez", "static/images/items/ionianas.png"), ("Foco do Horizonte", "static/images/items/focoHorizonte.png"), ("Capuz da Morte de Rabadon", "/static/images/items/rabadon.png"), ("Criptoflora", "static/images/items/criptoflora.png"), ("Véu de Banshee", "static/images/items/banshee.png")],
    "counter_assassin": [("Abraço de Seraph", "static/images/items/Cajado_do_Arcanjo_item.webp"), ("Botas Ionianas de Lucidez", "static/images/items/ionianas.png"), ("Zhonias", "/static/images/items/zhonias.png "), ("Capuz da Morte de Rabadon", "/static/images/items/rabadon.png"), ("Criptoflora", "static/images/items/criptoflora.png"), ("Chama Sombria", "static/images/items/chama_sombria.png")],
    "counter_tank": [("Abraço de Seraph", "static/images/items/Cajado_do_Arcanjo_item.webp"), ("Botas Ionianas de Lucidez", "static/images/items/ionianas.png"), ("Angústia de Liandry", "static/images/items/liandry.png"), ("Cajado do Vazio", "/static/images/items/cajadoVazio.png"), ("Capuz da Morte de Rabadon", "/static/images/items/rabadon.png"), ("Ladrão de Almas Mejai", "static/images/items/mejai.png")],
    "counter_bruiser": [("Abraço de Seraph", "static/images/items/Cajado_do_Arcanjo_item.webp"), ("Botas Galvanizadas de Aço", "static/images/items/galvanizadas.png"), ("Angústia de Liandry", "static/images/items/liandry.png"), ("Capuz da Morte de Rabadon", "/static/images/items/rabadon.png"),  ("Criptoflora", "static/images/items/criptoflora.png"), ("Zhonias", "/static/images/items/zhonias.png ")],
    "counter_mage": [("Companheiro de Luden", "static/images/items/luden.png"), ("Sapatos do Feiticeiro", "static/images/items/sapato_feiticeiro.png"), ("Ladrão de Almas Mejai", "static/images/items/mejai.png"), ("Chama Sombria", "static/images/items/chama_sombria.png"), ("Capuz da Morte de Rabadon", "/static/images/items/rabadon.png"), ("Cajado do Vazio", "/static/images/items/cajadoVazio.png")], 
    "counter_ranged": [("Tocha Sombria", "static/images/items/tochaSombria.png"), ("Botas Galvanizadas de Aço", "static/images/items/galvanizadas.png"), ("Angústia de Liandry", "static/images/items/liandry.png"), ("Foco do Horizonte", "static/images/items/focoHorizonte.png"), ("Capuz da Morte de Rabadon", "/static/images/items/rabadon.png"), ("Criptoflora", "static/images/items/criptoflora.png")]
}

runes = {
    "default": [("static/images/runes/runaimg-removebg-preview.png")],
    "counter_assassin": [("static/images/runes/counter_assassin.png")],
    "counter_tank": [("static/images/runes/counter_tank.png")],
    "counter_bruiser": [("static/images/runes/counter_bruiser.png")],
    "counter_mage": [("static/images/runes/counter_mage.png")],
    "counter_ranged": [("static/images/runes/counter_ranged.png")],

}

@home_route.route('/')
def home():
    return render_template('index.html')

@home_route.route('/get_build', methods=['POST'])
def get_build():
    data = request.json
    champion = data.get('champion').lower()

    # Verificar se o campeão existe em alguma das listas
    all_champions = list_bruiser + list_mage + list_tank + list_assassin + list_ranged + list_default
    if champion not in all_champions:
        return jsonify({'error': 'Esse campeão não existe, tente novamente'})

    # Verificar a classificação do campeão
    is_tank = champion in list_tank
    is_assassin = champion in list_assassin
    is_bruiser = champion in list_bruiser
    is_mage = champion in list_mage
    is_ranged = champion in list_ranged

    if is_tank and is_assassin:
        build = builds["counter_tank"] + builds["counter_assassin"]
        rune = runes["default"]
    elif is_tank:
        build = builds["counter_tank"]
        rune = runes["counter_tank"]
    elif is_assassin:
        build = builds["counter_assassin"]
        rune = runes["counter_assassin"]
    elif is_bruiser:
        build = builds["counter_bruiser"]
        rune = runes["counter_bruiser"]
    elif is_mage:
        build = builds["counter_mage"]
        rune = runes["counter_mage"]
    elif is_ranged:
        build = builds["counter_ranged"]
        rune = runes["counter_ranged"]
    else:
        build = builds["default"]
        rune = runes["default"]

    # Retorna a build e runas como uma resposta JSON
    return jsonify({'build': build, 'rune': rune})