import streamlit as st
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.set_page_config(page_title="Customer Segmentation App", layout="wide")

st.title("🧠 Customer Segmentation using RFM & K-Means")

st.write(
    "Upload a dataset and perform **RFM-based customer segmentation** using K-Means clustering."
)

# -------------------------------
# File upload
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload CSV or Excel file", type=["csv", "xlsx"]
)

if uploaded_file is not None:
    # Load data
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # -------------------------------
    # Check required columns
    # -------------------------------
    required_cols = [
        "Customer ID",
        "Invoice",
        "InvoiceDate",
        "Quantity",
        "Price",
    ]

    missing_cols = [c for c in required_cols if c not in df.columns]

    if missing_cols:
        st.error(f"Missing required columns: {missing_cols}")
        st.stop()

    # -------------------------------
    # Data cleaning
    # -------------------------------
    df = df.dropna(subset=["Customer ID"])
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["TotalAmount"] = df["Quantity"] * df["Price"]

    # -------------------------------
    # RFM calculation
    # -------------------------------
    st.subheader("📊 RFM Calculation")

    snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("Customer ID").agg(
        Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
        Frequency=("Invoice", "nunique"),
        Monetary=("TotalAmount", "sum"),
    )

    st.write("RFM Table (before scaling):")
    st.dataframe(rfm.head())

    # -------------------------------
    # Scaling
    # -------------------------------
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm)

    # -------------------------------
    # K-Means
    # -------------------------------
    st.subheader("🔢 K-Means Clustering")

    k = st.slider("Select number of clusters (K)", 2, 10, 4)

    kmeans = KMeans(n_clusters=k, random_state=42)
    rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

    # -------------------------------
    # Results
    # -------------------------------
    st.subheader("✅ Segmented Customers")
    st.dataframe(rfm.head())

    # Cluster summary
    st.subheader("📌 Cluster Summary")

    cluster_summary = rfm.groupby("Cluster").agg(
        Avg_Recency=("Recency", "mean"),
        Avg_Frequency=("Frequency", "mean"),
        Avg_Monetary=("Monetary", "mean"),
        Customers=("Cluster", "count"),
    )

    st.dataframe(cluster_summary)

    st.success("🎉 Customer segmentation completed successfully!")
