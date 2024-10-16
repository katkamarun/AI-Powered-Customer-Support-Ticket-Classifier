# AI-Powered Customer Support Ticket Classifier

This project is an **AI-Powered Customer Support Ticket Classifier** built using Streamlit. The app uses OpenAI's API to classify customer support tickets based on content, assessing urgency, sentiment, and other key information. The project is containerized using Docker and deployed to Azure App Service.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Local Setup](#local-setup)
   - Prerequisites
   - Cloning the Repository
   - Setting up the Environment
4. [Running the App Locally](#running-the-app-locally)
5. [Building and Pushing Docker Image](#building-and-pushing-docker-image)
6. [Deploying the App to Azure App Service](#deploying-the-app-to-azure-app-service)
7. [Additional Features and Future Enhancements](#additional-features-and-future-enhancements)
8. [Conclusion](#conclusion)

## 1. Project Overview

This project is designed to classify customer support tickets using OpenAI's API. The app identifies key ticket attributes such as urgency, sentiment, and categorization, and suggests actions based on the ticket content. It's containerized with Docker and deployed on **Azure App Service**.

## 2. Project Structure

/project-root
├── /src
│   ├── app.py                  # Main Streamlit app
│   ├── ticket_classifier.py     # Classification logic
│
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker instructions
├── .env                         # Environment variables (not uploaded to GitHub)
├── README.md                    # Documentation

## 3. Local Setup

### Prerequisites
- **Python 3.9+**
- **Docker** installed and running
- **Azure CLI** installed (for deployment)

### Cloning the Repository

```bash
git clone https://github.com/katkamarun/AI-Powered-Customer-Support-Ticket-Classifier.git
cd AI-Powered-Customer-Support-Ticket-Classifier
```

### Setting Up the Environment
Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up your .env file in the project root (do not push this file to GitHub):

```
OPENAI_API_KEY=your-openai-api-key
LANGFUSE_SECRET_KEY=your-langfuse-secret-key
LANGFUSE_PUBLIC_KEY=your-langfuse-public-key
```

## 4. Running the App Locally
To run the app locally:

```bash
streamlit run src/app.py
```

Once the app starts, open your browser and navigate to http://localhost:8501 to access the app.

## 5. Building and Pushing Docker Image

### Building the Docker Image
Build the Docker image:

```bash
docker build -t streamlit-ticket-classifier .
```

Run the Docker image locally (optional):

```bash
docker run -p 8000:8000 streamlit-ticket-classifier
```

### Pushing the Docker Image to DockerHub
Log in to DockerHub:

```bash
docker login
```

Tag the image for DockerHub:

```bash
docker tag streamlit-ticket-classifier your-dockerhub-username/streamlit-ticket-classifier
```

Push the image to DockerHub:

```bash
docker push your-dockerhub-username/streamlit-ticket-classifier
```

## 6. Deploying the App to Azure App Service

### Creating a Resource Group
```bash
az group create --name your-resource-group --location eastus
```

### Creating an App Service Plan
```bash
az appservice plan create --name your-app-plan --resource-group your-resource-group --sku B1 --is-linux
```

### Deploying the Docker Image from DockerHub
```bash
az webapp create --resource-group your-resource-group --plan your-app-plan --name your-app-name --deployment-container-image-name your-dockerhub-username/streamlit-ticket-classifier
```

### Setting Environment Variables
```bash
az webapp config appsettings set --resource-group your-resource-group --name your-app-name --settings OPENAI_API_KEY=your-openai-api-key LANGFUSE_SECRET_KEY=your-langfuse-secret-key LANGFUSE_PUBLIC_KEY=your-langfuse-public-key
```

### Restarting and Testing the App
```bash
az webapp restart --resource-group your-resource-group --name your-app-name
```

Visit your app at:

```
https://your-app-name.azurewebsites.net
```

## 7. CI/CD Pipeline with GitHub Actions
This project uses GitHub Actions to automate the build and deployment process. The pipeline is triggered upon every push to the main branch and follows these steps:

- **Checkout Code**: Pull the latest code from the GitHub repository.
- **Build Docker Image**: Build the Docker image using the provided Dockerfile.
- **Push Docker Image to DockerHub**: Automatically log in to DockerHub and push the Docker image.
- **Deploy to Azure**: Deploy the Docker image to Azure App Service using the `azure/webapps-deploy@v2` GitHub Action.
- **Run Tests**: Execute any defined tests to ensure code quality and functionality.

The workflow configuration can be found in `.github/workflows/main.yml`.

## 8. Additional Features and Future Enhancements
This project can be extended by adding:
- User authentication: To limit access to the app.
- Database integration: Store classified tickets for further analysis.
- Additional AI features: Such as text summarization or response generation based on ticket content.

## 9. Conclusion
This project demonstrates how to build, containerize, and deploy an AI-powered web app using Streamlit, Docker, and Azure App Service. It’s a great starting point for more complex AI applications 

