### ML project


this is  end to end NLP project with deployment using github action
### Objectives Approach

The project addresses the challenge of condensing lengthy texts, such as articles, documents, or paragraphs, into concise summaries without losing the core message and key information. This involves identifying significant sentences or phrases from the original text and presenting them in a condensed form. The primary objective is to develop an efficient text summarization model that can accurately capture the essence of the input text and produce coherent summaries.

###  Solution Approach
Gather a diverse dataset for training the summarization model and tokenize the text into sentences or words. Train the selected model on the preprocessed dataset to learn the relationships between input text and summaries.Assess the performance of the trained model using evaluation metrics. Deploy the trained model as a web service with CI/CD Deployment on AWS

### Workflows
1 Update config.yaml
2 Update params.yaml
3 Update entity
4 Update the configuration manager in src config
5 update the conponents
6 update the pipeline
7 update the main.py
8 update the app.py
### How to run?
### STEPS:
Clone the repository
https://github.com/NimraAslamkhan/MLPROJECT-student-performance-prediction

### STEP 01- Create a conda environment after opening the repository
conda create -n summary python=3.12.1 -y
conda activate summary

### STEP 02- install the requirements
pip install -r requirements.txt
# Finally run the following command
python app.py
open up you local host and port
Author: NimraAslmaKhan
Data Scientist
Email: nimraaslam3132@gmail.com


### AWS-CICD-Deployment-with-Github-Actions


## 1. Login to AWS console.


## 2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess


### 3. Create ECR repo to store/save docker image


### 4. Create EC2 machine (Ubuntu)

### 5Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

### 6Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
### 7Setup github secrets:

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
