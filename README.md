# 🌱 AI Plant Health Monitoring System

This project uses machine learning to analyze plant electrical signals and detect plant stress.

## Project Goal
Plants generate electrical signals when they experience environmental stress.  
This project explores whether machine learning can detect plant stress using sensor data.

## Dataset
The dataset contains plant sensor readings including:

- Soil moisture
- Temperature
- Electrical signals
- Plant health status

## Machine Learning
A Decision Tree classifier is used to predict plant stress based on environmental conditions.

## Visualization
The project includes data visualization for:

- Electrical signal over time
- Moisture vs temperature relationships

## Technologies
- Python
- Pandas
- Scikit-learn
- Matplotlib

## Project Structure

plant-ai-health-monitoring
│
├── data
│   └── plant_signals.csv
│
├── src
│   ├── model_training.py
│   └── visualize_signals.py
