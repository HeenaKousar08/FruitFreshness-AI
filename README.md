# FruitFreshnessProject
# 🥦🍎 AI-Based Fruit & Vegetable Freshness Detection System

## 📌 Overview

This project is an end-to-end **Computer Vision + Deep Learning** application that classifies fruits and vegetables into **Fresh, Ripe, or Rotten** categories.

It also includes a **Smart Vendor Pricing System** that dynamically adjusts prices, calculates profit/loss, and stores results for future analysis.

---

## 🚀 Features

* 🔍 **Image Classification** using Deep Learning (Fresh / Ripe / Rotten)
* 📷 **Real-Time Camera Detection** using OpenCV
* 💰 **Dynamic Pricing System** based on freshness
* 📊 **Profit & Loss Calculation**
* 🗃️ **SQLite Database Integration** for storing history
* 📈 **Scan History Dashboard**
* 🌐 **Flask Web Application** for user interaction

---

## 🧠 Model Details

* Model Type: Convolutional Neural Network (CNN)
* Framework: TensorFlow / Keras
* Input Size: 224 × 224
* Classes: Fresh, Ripe, Rotten
* Preprocessing: Normalization, Resizing

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* Flask
* SQLite
* NumPy

---

## 📂 Project Structure

```
FruitFreshnessProject/
│
├── app.py                  # Main Flask application
├── train_model.py          # Model training script
├── freshness_model.h5      # Trained model
├── database.py            # Database functions
├── logic.py               # Shelf life logic
│
├── static/
│   └── uploads/           # Uploaded images
│
├── templates/
│   ├── index.html
│   ├── history.html
│   └── camera.html
│
├── dataset/               # Training dataset
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/fruit-freshness-project.git
cd fruit-freshness-project
```

---

### 2️⃣ Create virtual environment

```bash
conda create -n freshness_env python=3.10
conda activate freshness_env
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Train the model

```bash
python train_model.py
```

---

### 5️⃣ Run the application

```bash
python app.py
```

---

### 6️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 📊 How It Works

1. User uploads an image or uses live camera
2. Model predicts freshness (Fresh / Ripe / Rotten)
3. Shelf life is estimated
4. Pricing system applies discount if needed
5. Profit/Loss is calculated
6. Data is stored in database

---

## 💡 Use Case

* Helps vendors **reduce food waste**
* Enables **dynamic pricing strategy**
* Improves **inventory management**
* Supports **real-time decision making**

---

## 🔮 Future Enhancements

* Mobile application integration
* Cloud deployment (AWS / Azure)
* Advanced object detection (YOLO)
* Dashboard with analytics & graphs

---
## Setup Instructions

1.  **Add Images:**
    * Go to the `dataset` folder.
    * You will see three folders: `Fresh`, `Ripe`, `Rotten`.
    * Add at least 20-30 images of fruits to each folder respectively. (You can download these from Kaggle or Google Images).

2.  **Install Libraries:**
    Open your terminal in this folder and run:
    `pip install -r requirements.txt`

3.  **Train the AI:**
    Run: `python train_model.py`
    *Wait for it to finish and create the 'freshness_model.h5' file.*

4.  **Run the Web App:**
    Run: `python app.py`
    *Open the link (usually http://127.0.0.1:5000) in your browser.*

## 👩‍💻 Author

**Heena Kousar**
M.Sc Data Science Student

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share!


