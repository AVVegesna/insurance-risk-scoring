document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('submit');
    button.addEventListener('click', () => {
        event.preventDefault();
        fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                age: Number(document.getElementById('Age').value),
                tenure: Number(document.getElementById('Tenure').value),
                vehicle_type: document.getElementById('Vehicle').value,
                claims_history: Number(document.getElementById('Claim_history').value)
            })
        })
        .then(res => res.json())
        .then(data => {
            const modal = document.getElementById("resultModal");
            const resultText = document.getElementById("resultText");
            const closeBtn = document.getElementById("closeModal");

            resultText.textContent = `Predicted claims count: ${data.claims_count}`;
            modal.classList.remove("hidden");

            closeBtn.onclick = () => {
                modal.classList.add("hidden");
            };
        })
        .catch(err => console.error(err));
    });
});
