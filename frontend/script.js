document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('submit');
    button.addEventListener('click', () => {
        fetch("http://127.0.0.1:8000/predict", {
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
            console.log(data.claims_count);
            alert("Predicted claims_count: " + data.claims_count);
        })
        .catch(err => console.error(err));
    });
});
