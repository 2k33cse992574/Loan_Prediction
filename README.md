# AI-Powered Loan Approval Prediction System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Finance](https://img.shields.io/badge/Finance-Risk%20Management-blue?style=for-the-badge)

**Loan Approval Prediction System** is a machine learning web application tailored for the banking and finance sector. It automates the initial screening of loan applications by calculating the approval probability based on financial metrics, asset values, and credit scores, enabling faster and more accurate lending decisions.

## ✨ Core Features

- **Real-Time Approval Analysis:** Evaluates key factors like Income, Loan Amount, Loan Term, and CIBIL score.
- **Automated Decision Logic:**
  - **Auto-Approve:** (Prob ≥ 0.6) Streamlined processing for low-risk applications.
  - **Manual Review:** (Prob between 0.3 - 0.6) Flagged for expert human analysis.
  - **Reject:** (Prob < 0.3) High-risk identification.
- **Asset Liability Mapping:** Factors in both luxury and residential asset values to determine financial stability.
- **Scalable REST API:** Flask-driven inference endpoint for seamless integration with banking portals.

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-CORS.
- **Machine Learning:** Scikit-Learn (Model & Scaler).
- **Data Manipulation:** NumPy.
- **Platform:** Web-based interface for easy data entry and results.

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/2k33cse992574/Loan_Prediction.git
   cd Loan_Prediction
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```
   *The system will be accessible on `http://localhost:5000`.*

## 📝 License
This project is open-source.
