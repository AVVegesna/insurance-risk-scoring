# Insurance Risk Scoring API & Web App
A full-stack machine learning application that predicts insurance claim counts based on customer and vehicle characteristics.<br>
The project demonstrates end-to-end ML engineering: data processing, model training, API serving, frontend integration, containerization, and cloud deployment.<br>
<br>
Live App (Google Cloud Run):<br>
👉 https://insurance-app-520162048776.australia-southeast1.run.app<br>
Docker Image:<br>
Pull the Docker image<br>
```bash
docker pull australia-southeast1-docker.pkg.dev/insurance-risk-scoring/insurance-repo/insurance-api:latest
```
<br>
Demo Video:<br>
👉https://youtu.be/pYxfWCzLBi4<br>
<br>

## Features
- Predicts insurance claim count using a trained ML pipeline
- REST API built with FastAPI
- Frontend built with HTML, CSS, and JavaScript
- Fully Dockerized
- Deployed on Google Cloud Run
- Input validation using Pydantic
- Logging & error handling
- CORS-enabled for frontend integration
<br>

## Machine Learning Overview
- Problem Type: Count prediction (claims frequency)
- Response Variable: claims_count
- Model Pipeline:
    - Feature preprocessing
    - Categorical encoding
    - Model training (via sklearn pipeline)
- Training Trigger: Application startup (for demo purposes)<br>
In a production system, the model would typically be trained offline and loaded from storage.
<br>

## Tech Stack
Backend<br>
- Python 3.11
- FastAPI
- Pydantic
- Pandas
- Scikit-learn
- Uvicorn
Frontend<br>
- HTML5
- CSS3
- Vanilla JavaScript (Fetch API)
Infrastructure & DevOps<br>
- Docker
- Google Cloud Run
- Google Artifact Registry
<br>

## Project Structure
```powershell
insurance-risk-scoring/
│
├── api/
│   ├── main.py            
│   └── schemas.py         
│
├── models/
│   ├── train.py           
│   └── predict.py        
│
├── frontend/
│   ├── index.html
│   ├── static/
│   │   ├── styles.css
│   │   ├── script.js
│   │   └── images/
│
├── data/
│   └── raw/
│       └── labeled_insurance.csv
│
├── Dockerfile
├── requirements.txt
└── README.md
```
<br>

## Running Locally (Without Docker)
```bash
pip install -r requirements.txt
python -m uvicorn api.main:app --reload
```
Visit<br>
👉http://127.0.0.1:8080<br>
<br>

## Running with Docker
```bash
docker build -t insurance-api .
docker run -p 8000:8080 insurance-api
```
<br>

## Deployment (Google Cloud Run)
- Container built locally
- Image pushed to Artifact Registry
- Deployed using Cloud Run (managed)
- Public access enabled
<br>

## Future Improvements
- Offline model training & versioning
- Persistent model storage (GCS)
- Authentication
- Feature store integration
- Monitoring & metrics
- CI/CD pipeline
<br>

## Author
Akshay Varma Vegesna<br>
Graduate Software Engineer @ IAG<br>
LinkedIn: https://www.linkedin.com/in/a-vegesna/

