# mlflow-terraform
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Terraform](https://img.shields.io/badge/terraform-623CE4?style=for-the-badge&logo=terraform&logoColor=white)
![MLflow](https://img.shields.io/badge/mlflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)


## 📖 Description
This project involves deploying an analytical solution originally developed by [Viktor](https://github.com/CoViktor/customer_churn_analysis.git).
I have implemented the pipelines and models using MLflow to monitor model accuracies and select the best-performing one. Subsequently, the solution was containerized using Docker to host the MLflow server. The Docker container was then set up and managed with Terraform.



## 🛠 Installation

* clone the repo
```bash
git clone https://github.com/semdeleer/mlflow_bc_sd-.git
```

* Run the terraform commands
```bash
$ terraform init
$ terraform apply
```

## Usage

* Connect to the container
```bash
$ docker exec -it <container_name_or_id> /bin/bash
```

* Go through the directory and find the run.py
```bash
$ dir
```

* run the py file
```bash
$ python run.py
```


## 🤖 Project File structure
```
C:.
├───package
│   ├───data
│   │   └───BankChurners.csv
│   ├───feature
│   │   └───data_processing.py
│   ├───ml_training
│   │   ├───preprocessing_pipeline.py
│   │   ├───retrieval.py
│   │   └───train.py
│   └───utils
├───Dockerfile
├───main.tf
├───requirements.txt
└───run.py


```

## 🔍 Contributors
- [Sem Deleersnijder](https://github.com/semdeleer)

## 📜 Timeline

This project was created in 10 days.