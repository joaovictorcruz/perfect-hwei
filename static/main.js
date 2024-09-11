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
        resultDiv.innerHTML = `Build Recomendada: ${data.build.join(', ')}`;
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