<div align="center">
  
# 🏠 IoT-Home-Automation-Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![InfluxDB](https://img.shields.io/badge/Database-InfluxDB-22ADF6?logo=influxdb&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

> **A comprehensive, Docker-based learning environment bridging the gap between hardware (IoT) and intelligence (Data Science).**

---

## 📖 Overview

Welcome to the **Non-Degree IoT Workshop 2025**. This project is designed to simulate a real-world industrial data pipeline. It teaches you how to capture data from sensors, transmit it efficiently, store it for analysis, and visualize it for decision-making.

For a Data Scientist or Software Engineer, understanding the full lifecycle of data—from the "Edge" (sensors) to the "Cloud" (databases/dashboards)—is a critical skill.


### 🎯 Why this project?
Real-world business problems require robust data infrastructure. This platform demonstrates:
1.  **Data Engineering:** Ingesting high-frequency time-series data using MQTT and InfluxDB.
2.  **DevOps:** Managing complex microservices architectures using Docker.
3.  **Analytics:** Visualizing trends and anomalies using Grafana.
4.  **Backend Development:** exposing data via Python Flask REST APIs.

---

## 🏗️ Architecture & Tech Stack

We use a containerized microservices approach. Each component solves a specific business problem:

| Component | Technology | Role in the Data Pipeline |
| :--- | :--- | :--- |
| **Message Broker** | **EMQX (MQTT)** | The "Post Office" of IoT. Handles high-speed communication between devices. |
| **Orchestrator** | **Node-RED** | Visual programming tool to process data flows and logic. |
| **Time-Series DB** | **InfluxDB** | Specialized storage for high-velocity sensor data (timestamped data). |
| **Backend API** | **Python (Flask)** | Custom logic and external interface for the system. |
| **Visualization** | **Grafana** | Professional analytics dashboards to monitor system health. |
| **Reverse Proxy** | **Nginx** | Routing traffic securely to the correct service. |

---

## 🚀 Quick Start Guide

Follow these steps to get your environment running in minutes.

### 1. Prerequisites
* **Docker Desktop**
* **Python**
* **Git (optional)**

### 2. Launch the Infrastructure
We use Docker Compose to spin up the entire ecosystem simultaneously.

```bash
cd docker
docker-compose up -d
```

### Access your services:
* 📊 Grafana: http://localhost:3000
* 🛢️ InfluxDB: http://localhost:8086
* 📡 EMQX Dashboard: http://localhost:18083
* 🔄 Node-RED: http://localhost:1880

📂 Project Structure
A clean structure allows for easy navigation and scaling.

```Plaintext
non-deegree-workshops-2025/
├── Simulator/                    
│   ├── humidity_sensor.py             
│   └── iot_simulator.py
│   ├── smart_switch.py   
│   └── temperature_sensor.py             
├── code/                           
├── docker/                 
│   ├── datasources/
│   ├── grafana/
│   └── nginx/
│   └── node-red/
├── .env
├── .env.example
├── README.md
├── System Architecture.md         
└── requirements.txt
```
