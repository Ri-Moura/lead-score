# Lead Scoring Model Deployment

## Overview

The Lead Scoring Model is designed to predict the probability of lead conversion based on various features such as total visits, time spent on the website, page views per visit, and more. This project involves preprocessing input data, training a machine learning model, and deploying the model using FastAPI for real-time predictions. The application is containerized using Docker for consistent and scalable deployment.

## Features

- **Machine Learning Model**: Utilizes XGBoost to predict lead conversion probabilities.
- **Data Preprocessing**: Handles missing values, feature engineering, and scaling.
- **API Integration**: FastAPI for creating a RESTful API to serve predictions.
- **Scalable Deployment**: Dockerized for easy and consistent deployment across environments.

## Task

Develop a system to:
1. Accept input data for lead scoring.
2. Preprocess the input data to match the training format.
3. Predict the probability of lead conversion using the trained model.

## Technology Stack

- **Machine Learning**: XGBoost
- **API**: FastAPI
- **Containerization**: Docker

## Installation

### Clone the repository:
```bash
git clone https://github.com/your-username/lead-scoring-model.git
cd lead-scoring-model
```

### Install the requirements:
```bash
pip install -r requirements.txt
```

## Usage

### Running the FastAPI app:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### Running the Docker Container

#### Build the Docker image:
```bash
docker build -t lead_scoring_model_fastapi .
```

#### Run the Docker container:
```bash
docker run -p 8000:8000 lead_scoring_model_fastapi
```

##### Using CURL to execute the request
```bash
curl -X POST http://your-server-ip:8000/predict/ \
-H "Content-Type: application/json" \
-d '{
    "TotalVisits": [5, 3],
    "Total_Time_Spent_on_Website": [1200, 850],
    "Page_Views_Per_Visit": [6.0, 4.2],
    "Country": ["India", "USA"],
    "Lead_Source": ["Google", "Direct Traffic"],
    "Last_Activity": ["Email Opened", "Page Visited"]
}'
```

## Endpoints

- **POST /predict/**: Accepts lead data and returns the probability of conversion.

### Example Input:
```json
{
    "TotalVisits": [5, 3],
    "Total_Time_Spent_on_Website": [1200, 850],
    "Page_Views_Per_Visit": [6.0, 4.2],
    "Country": ["India", "USA"],
    "Lead_Source": ["Google", "Direct Traffic"],
    "Last_Activity": ["Email Opened", "Page Visited"]
}
```

### Example Output:
```json
{
    "predictions": [0.85, 0.45]
}
```

## Technology Stack

- **Machine Learning**: XGBoost for model training and prediction.
- **API**: FastAPI for serving predictions.
- **Containerization**: Docker for deployment.
- **Monitoring**: Google Cloud Monitoring for system performance.
- **Model Tracking**: MLFlow for tracking model performance metrics.

## Deployment

### GCP Deployment

The plan to deploy, serve and monitoring this application is in `productization_plan` folder

## Requirements

- Docker
- Python 3.x
- FastAPI
- XGBoost
- Scikit-learn
- Pandas

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or support, please open an issue in this repository.
