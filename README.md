# 🌦️ CaelumFlux: Weather Data Pipeline

## 📖 Overview

CaelumFlux is an **ETL (Extract, Transform, Load) pipeline** designed to collect, process, and store weather data using **Python, PostgreSQL, Apache Airflow**, and the **OpenWeatherAPI**. This pipeline enables efficient data retrieval, transformation, and storage to support analytics and forecasting.

## ✨ Features

- 🔄 **Automated Data Collection**: Fetches real-time weather data from OpenWeatherAPI.
- 📅 **Scheduled Processing**: Uses Apache Airflow for task automation.
- 🗄️ **PostgreSQL Storage**: Stores cleaned and structured weather data for analysis.
- ⚙️ **ETL Workflow**: Extracts raw data, transforms it into a usable format, and loads it into the database.
- 📊 **Data Aggregation**: Supports historical data storage for time-series analysis.
- 🔧 **Scalable & Extendable**: Easily adaptable to integrate with other data sources.

## 🛠 Technologies Used

- 🐍 **Python**: Scripting and data processing.
- 🗄️ **PostgreSQL**: Database management for storing weather data.
- 🌬️ **Apache Airflow**: Workflow automation and scheduling.
- ☁️ **OpenWeatherAPI**: Data source for weather information.

## 📂 Database Schema

```sql
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    temperature NUMERIC(5,2),
    min_temp NUMERIC(5,2),   
    max_temp NUMERIC(5,2),   
    humidity INT,
    wind_speed NUMERIC(5,2),
    direction NUMERIC(5,2),
    weather_condition VARCHAR(255)
);
```

---

## 👤 Author
Developed by **Cley**  
📧 Contact: 02clintaudrey@gmail.com 
🌐 GitHub: SecreShall

---
