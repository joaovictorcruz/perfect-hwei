function getBuild() {
    console.log('Função getBuild chamada');
    const champion = document.getElementById('champion').value;

    fetch("/get_build", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ champion: champion })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Dados recebidos:', data);
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '<h3 class="slide-in">Build Recomendada: </h3>';

        const buildContainer = document.createElement('div');
        buildContainer.classList.add('result-container', 'slide-in');

        // Exibe a build
        data.build.forEach(item => {
            const itemName = item[0];
            const itemImage = item[1];

            const itemContainer = document.createElement('div');
            itemContainer.classList.add('item-container');

            const imgElement = document.createElement('img');
            imgElement.src = itemImage;
            imgElement.alt = itemName;
            imgElement.classList.add('item-img');
            
            const itemText = document.createElement('span');
            itemText.textContent = itemName;
            itemText.classList.add('item-name');

            itemContainer.appendChild(imgElement);
            itemContainer.appendChild(itemText);
            buildContainer.appendChild(itemContainer);
        });

        // Adiciona o contêiner das builds ao resultado
        resultDiv.appendChild(buildContainer);

        // Exibe as runas abaixo das builds
        const runeContainer = document.createElement('div');
        runeContainer.classList.add('rune-container', 'slide-in');  // Nova classe para runas

        data.rune.forEach(rune => {
            const runeImage = rune;

            const runeImgElement = document.createElement('img');
            runeImgElement.src = runeImage;
            runeImgElement.alt = 'Runa';
            runeImgElement.classList.add('rune-img');  // Classe específica para runas

            runeContainer.appendChild(runeImgElement);
        });

        // Adiciona o contêiner das runas ao resultado, abaixo das builds
        resultDiv.appendChild(runeContainer);
    })
    .catch(error => console.error('Erro:', error));
}
// Detectar tecla Enter no campo de input
document.getElementById('champion').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        getBuild();  // Chama a função getBuild quando Enter for pressionado
    }
});

// Detectar clique no botão
document.getElementById('searchButton').addEventListener('click', getBuild);