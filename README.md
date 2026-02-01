# Customer Segmentation using RFM Analysis (Retail Dataset)

## 📌 Project Overview
This project performs customer segmentation using **RFM (Recency, Frequency, Monetary)** analysis and **K-Means clustering** on a retail dataset.  
The goal is to identify high-value customers, loyal customers, and at-risk customers to help marketing and retention strategies.

---

## 🧠 What I learned from this project
- Data cleaning and preprocessing
- Handling returns/cancelled transactions
- RFM feature engineering
- K-Means clustering for segmentation
- Building a Streamlit web app

---

## 🔍 Dataset
The dataset used is the **Online Retail dataset** (available on Kaggle/UCI).  
It contains retail transaction records with the following columns:

- Customer ID
- Invoice
- InvoiceDate
- Quantity
- Price

---

## 🧾 Project Workflow

### 1. Data Cleaning
- Removed cancelled invoices (starting with "C")
- Removed negative quantities
- Converted InvoiceDate to datetime
- Calculated total revenue per order

### 2. RFM Calculation
- **Recency**: Days since last purchase
- **Frequency**: Number of purchases
- **Monetary**: Total money spent

### 3. Clustering
- Standardized the RFM values
- Applied K-Means clustering
- Created customer segments

---

## 🚀 How to run the app
1. Clone the repository
2. Install dependencies:
