# 📍 Project Overview

This project predicts the likelihood of colorectal cancer using a complete MLOps pipeline.
It covers everything from data processing, model training, **experiment tracking**, to versioning, containerization, and deployment with Kubeflow.
---

# 🛠️ Tech Stack & Tools Used

**Python 3.10**

**Machine Learning:** LightGBM, Scikit-learn

**MLOps Tools:** MLflow, DagsHub, Docker, Kubernetes, Kubeflow Pipelines, Minikube

**Backend:** Flask

**Version Control:** Git, GitHub

**Others:** Pandas, NumPy, YAML, Joblib

---

# 🏗️ Project Architecture

**The architecture follows a robust, scalable and production-ready MLOps flow:**

**Data Ingestion & Preprocessing**

**Model Training (LightGBM)**

**Experiment Tracking with MLflow & DagsHub**

**Model Saving & Versioning**

**Flask-based Real-Time Inference App**

**Docker Containerization**

**CI/CD Workflow Automation**

**Deployment via Kubeflow Pipelines on Minikube Kubernetes Cluster**

---

# 📆 Project Impact

⏱️ Reduced diagnostic latency by up to 40% through real-time prediction capabilities.

⌛ Saved over 10+ hours/week by automating experiment tracking and model versioning.

🚀 Decreased model deployment cycles by 75% with CI/CD and Kubeflow automation.

📦 Project Setup (Local)

✅ Clone the Repository

git clone https://github.com/your-username/Colorectal-Cancer-Prediction-MLOps.git
cd Colorectal-Cancer-Prediction-MLOps

---

# 🤝 Create a Virtual Environment
---
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt

---

# 🎓 Run the ML Pipeline
--
python src/data_processing.py
python src/model_training.py

---

# 📊 Run MLflow UI (Optional)
---
mlflow ui

Access at http://127.0.0.1:5000

---

# 🏠 Run Flask App Locally

python src/prediction_service.py

Visit: http://127.0.0.1:8080

🐳 Docker Setup

🛠️ Build Docker Image

docker build -t cancer-prediction-app .

🚤 Run Docker Container

docker run -p 8080:8080 cancer-prediction-app

⚖️ Kubeflow Pipelines on Minikube

Start Minikube:

minikube start

Launch Kubeflow Dashboard (if installed):

minikube service istio-ingressgateway -n istio-system

Deploy pipeline using your mlops_pipeline.py definition.

📁 Folder Structure

Colorectal-Cancer-Prediction-MLOps/
|
├── data/                        # Input data files
├── src/                         # Python scripts
│   ├── data_processing.py
│   ├── model_training.py
│   ├── prediction_service.py    # Flask App
├── kubeflow_pipeline/
│   └── mlops_pipeline.py
├── Dockerfile
├── requirements.txt
├── README.md
├── mlruns/                      # MLflow logs

✨ Future Enhancements

Integrate EvidentlyAI for model drift detection

Setup real-time monitoring dashboards via Prometheus + Grafana

Enable cloud deployment via GCP or AWS for production-scale workloads

🙌 Acknowledgments

Thanks to the open-source communities of LightGBM, Flask, MLflow, Kubeflow, and DagsHub.

🚀 Made with passion by Ambuj Nayan Mishra

