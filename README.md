# Customer_Churn_Prediction_System
## Project Overview

Customer churn means customers leaving a service.
For telecom companies, churn directly results in revenue loss.

The goal of this project is to predict customer churn early, so companies can take preventive actions such as targeted offers, improved customer support, or personalized retention strategies.

This project demonstrates how a machine learning model can be taken from data preprocessing to a usable application with a backend API and a simple frontend interface.

## Key Objectives

Build a supervised ML model for churn prediction

Design a clean ML pipeline (preprocessing → training → evaluation)

Serve predictions using a FastAPI backend

Provide a simple HTML/CSS/JS frontend for user interaction

## Tech Stack

Programming Language: Python

Machine Learning: Scikit-learn (Random Forest)

Backend: FastAPI

Frontend: HTML, CSS, JavaScript

Data Handling: Pandas, NumPy

## How the System Works
User Input (Web Form)
        ↓
Frontend (HTML + JS)
        ↓
FastAPI Backend
        ↓
ML Model (Random Forest)
        ↓
Churn Prediction + Probability

# Machine Learning Details

Problem Type: Binary Classification

Target Variable: Churn (Yes / No)

Model Used: Random Forest Classifier

# Features:

Customer profile

Service usage

Billing information

# Evaluation Metrics

Accuracy

Precision

Recall

F1-score

ROC-AUC

# Backend (FastAPI)

Exposes a /predict endpoint

Accepts customer details as JSON

Returns:

Churn prediction (0 / 1)

Churn probability

CORS is enabled to allow frontend–backend communication.

# Frontend

Simple form-based interface

Users enter customer details

Click Predict Churn to get:

Prediction result

Probability

Risk level (Low / Medium / High)

This frontend is designed to demonstrate ML usage, not for production UI.

# How to Run the Project
# 1️ Backend
uvicorn api.main:app --reload


Backend runs at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

# 2️ Frontend
cd frontend
python -m http.server 5500


Open in browser:

http://127.0.0.1:5500/index.html

# What This Project Demonstrates

Building ML systems beyond notebooks

Handling real-world issues like feature mismatch and CORS

Separating frontend, backend, and ML logic

Deployable and extensible ML architecture
