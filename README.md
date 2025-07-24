# 🌾 Smart Irrigation System using Machine Learning and IoT

A smart, scalable, and region-adaptive irrigation solution that utilizes soil and crop data, ML-based predictions, and IoT-based hardware to automate and optimize water distribution for agriculture.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [ML Model Workflow](#ml-model-workflow)
- [Hardware Integration](#hardware-integration)
- [Datasets](#datasets)

---

## 🌱 Overview

This project is designed to aid farmers by automating the irrigation process based on real-time environmental data and historical trends. We use *Decision Tree-based ML models* trained on *soil and crop data from Madhya Pradesh, Uttar Pradesh, and pan-India* regions to determine whether irrigation is required.

<img width="1060" height="818" alt="1753285756145" src="https://github.com/user-attachments/assets/7fa4b564-e748-4cba-951d-9bdfe7bcf609" />


---

## ⭐ Key Features

- 📊 *ML-powered Irrigation Decisions*
- 🌦 *Sensor-based real-time soil moisture and temperature input*
- 🧠 *Trained Decision Tree model with over 90% accuracy*
- ⚡ *Automatic pump control via microcontroller*
- 🌍 *Region-specific model training for high relevance*
- 🛠 *Modular & scalable for large deployment*

---

## 🧠 Architecture

<img width="628" height="558" alt="image" src="https://github.com/user-attachments/assets/d3c66d24-f21a-49c7-b322-8873a3bbf61c" />


- *Data Input:* Soil moisture, temperature, region, and crop type
- *ML Processing:* Decision Tree predicts irrigation requirement
- *Output:* Controls motor via relay module
- *Fallback:* Timer-based control with RTC (optional)

---

## 🌲 ML Model Workflow


- Model: Decision Tree Classifier
- Features: Soil moisture, temperature, soil type, crop type
- Labels: Water required (yes/no)
- Evaluation: Accuracy, precision, recall
- Tools: Python, Jupyter Notebook, Scikit-learn

---

## 🔌 Hardware Integration


*Components Used:*
- Arduino Uno
- Soil Moisture Sensor
- Relay Module
- DC Pump
- RTC Module (optional)
- LCD (optional for display)
- Power Supply

*Working:*
- Arduino reads real-time moisture data
- Sends data to ML module
- Based on prediction, pump is activated via relay

---

## 📂 Datasets

Used three datasets:
- 🌾 *Madhya Pradesh Crop-Soil Data*
- 🌾 *Uttar Pradesh Crop-Soil Data*
- 🇮🇳 *India-wide Generic Crop Dataset*

Features included:
- Soil moisture levels
- Soil type
- Crop type
- Region
- Historical water usage
- Temperature

---
