# 🏠 Bangalore House Price Prediction

A full-stack Machine Learning web application that predicts house prices in Bangalore based on user inputs such as location, square footage, number of bedrooms (BHK), and bathrooms.

The project combines Machine Learning, Flask, and a responsive frontend to provide real-time price predictions through an interactive web interface.

---

## 🚀 Live Demo

🔗 https://bangalore-house-price-rqyw.onrender.com/

---

## 📌 Features

* Predict Bangalore house prices instantly
* Dynamic location dropdown loaded from the backend
* User-friendly and responsive interface
* Real-time prediction using a trained ML model
* End-to-end deployment using Render
* REST API integration between frontend and backend

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn

### Backend

* Flask
* Flask-CORS
* Gunicorn

### Frontend

* HTML5
* CSS3
* JavaScript
* jQuery

### Deployment

* GitHub
* Render

---

## 📂 Project Structure

```text
Realestate-model/
│
├── app.py
├── util.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── Model/
    ├── bengaluru_house_price_prediction.csv
    ├── columns.json
    ├── model.pkl
    └── realestate.py
```

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Outlier Detection & Removal
5. One-Hot Encoding
6. Model Training
7. Model Serialization
8. Web Application Integration
9. Deployment

---

## 📊 Model Inputs

The application accepts the following inputs:

| Feature     | Description                     |
| ----------- | ------------------------------- |
| Area (sqft) | Total house area in square feet |
| BHK         | Number of bedrooms              |
| Bath        | Number of bathrooms             |
| Location    | Area within Bangalore           |

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git

cd YOUR_REPOSITORY_NAME
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🌐 API Endpoints

### Get Locations

```http
GET /get_location_names
```

### Predict Price

```http
POST /predict_price
```

Request Body:

```json
{
  "location": "Indira Nagar",
  "sqft": 1000,
  "bath": 2,
  "bhk": 2
}
```

Response:

```json
{
  "estimated_price": 85.4
}
```

---

## 🎯 Future Improvements

* Improve model accuracy
* Add advanced regression algorithms
* Better UI/UX
* Add charts and analytics
* User authentication
* Database integration
* Docker containerization

---

## 👨‍💻 Author

MADHUBALAKUMAR S

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: Add your LinkedIn profile

---

## ⭐ Support

If you found this project useful, please give it a star ⭐ on GitHub.
