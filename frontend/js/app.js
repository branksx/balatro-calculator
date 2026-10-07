const API_URL = "http://127.0.0.1:8000";

//Elementos da DOM
const handSelect = document.getElementById("handSelect");
const levelInput = document.getElementById("levelInput");
const calculateButton = document.getElementById("calculateButton");
const resultCard = document.getElementById("resultCard");

const resHandName = document.getElementById("resHandName");
const resHandLevel = document.getElementById("resHandLevel");
const resChips = document.getElementById("resChips");
const resMulti = document.getElementById("resMulti");
const resScore = document.getElementById("resScore");

async function loadHands() {
    try {
        const response = await fetch(`${API_URL}/hands/`);
        const hands = await response.json();
        
        handSelect.innerHTML = ""
        hands.forEach(hand => {
            const option = document.createElement("option");
            option.value = hand.id;
            option.textContent = hand.hand_name;
            handSelect.appendChild(option);
        });
    } catch (error) {
        console.error("Erro ao carregar mãos:", error);
        handSelect.innerHTML = "<option value=''>Erro ao conectar à API</option>";
    }
}

async function calculateScore() {
    const handId = parseInt(handSelect.value);
    const level = parseInt(levelInput.value);

    if (!handId || !level || level < 1) {
        alert("Por favor, selecione uma mão válida e insira um nível válido (maior ou igual a 1).");
        return;
    } 
    try {
        const response = await fetch(`${API_URL}/calculate/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                hand_id: handId,
                level: level
            })
        });

        if(!response.ok) {
            throw new Error(`Erro ao calcular pontuação:`);
        }

        const data = await response.json();

        //Preencher o card de resultado com os dados da API
        resHandName.textContent = data.hand_name;
        resHandLevel.textContent = data.level;
        resChips.textContent = data.calculated_chips;
        resMulti.textContent = data.calculated_multi;
        resScore.textContent = data.score.toLocaleString(); // Formata com pontos (ex: 1,595)

        // Mostrar o card de resultado
        resultCard.classList.remove("hidden");

    } catch (error) {
        console.error("Erro :", error);
        alert("Ocorreu um erro ao comunicar com o servidor.");
    }
}

//Eventos
document.addEventListener("DOMContentLoaded", loadHands);
calculateButton.addEventListener("click", calculateScore);