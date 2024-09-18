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
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '';  // Limpa resultados anteriores

        // Verifica se há um erro (campeão não existente)
        if (data.error) {
            const errorMessage = document.createElement('p');
            errorMessage.textContent = data.error;
            errorMessage.style.color = 'red';
            resultDiv.appendChild(errorMessage);
            return;
        }

        // Exibe a build
        resultDiv.innerHTML = '<h3 class="slide-in">Build Recomendada: </h3>';

        const buildContainer = document.createElement('div');
        buildContainer.classList.add('result-container', 'slide-in');

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

        resultDiv.appendChild(buildContainer);

        // Exibe as runas
        const runeContainer = document.createElement('div');
        runeContainer.classList.add('rune-container', 'slide-in');

        data.rune.forEach(rune => {
            const runeImage = rune;

            const runeImgElement = document.createElement('img');
            runeImgElement.src = runeImage;
            runeImgElement.alt = 'Runa';
            runeImgElement.classList.add('rune-img');

            runeContainer.appendChild(runeImgElement);
        });

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