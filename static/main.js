function getBuild() { 
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
        resultDiv.innerHTML = '<h3>Build Recomendada: </h3>';

        const container = document.createElement('div');
        container.classList.add('result-container');

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

            // Adicionar a imagem e o nome ao contêiner
            itemContainer.appendChild(imgElement);
            itemContainer.appendChild(itemText);

            // Adicionar o contêiner ao container
            container.appendChild(itemContainer);
        });

        // Adicionar o container ao resultDiv
        resultDiv.appendChild(container);
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