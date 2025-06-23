import streamlit as st
import pandas as pd
import joblib

st.title("💼 Job Salary Predictor")

st.markdown("""
### 📋 **Instructions**:
- Upload a **CSV file** with columns: `Title` and `Tags`
- Example:
| Title          | Tags                     |
|----------------|--------------------------|
| Data Scientist | Python, SQL, MachineLearning |

""")

sample_csv = """
Title,Tags
Data Scientist,"Python, ML, SQL"
Backend Developer,"NodeJS, Express"
"""
st.download_button("📄 Download Example CSV", data=sample_csv, file_name="example_jobs.csv")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if "Title" not in df.columns or "Tags" not in df.columns:
        st.error("❗ Please upload a CSV with 'Title' and 'Tags' columns.")
    else:
        st.write("📄 Uploaded Data", df.head())

        with st.spinner("🔄 Loading model..."):
            model = joblib.load("model/model.joblib")
        st.success("✅ Model loaded!")

        if st.button("Predict Salaries"):
            with st.spinner("🔄 Predicting salaries..."):
                X = df[["Title", "Tags"]]
                predictions = model.predict(X)
                df["Predicted Salary"] = predictions
            st.success("✅ Predictions ready!")

            st.write(df)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download Predictions CSV", data=csv, file_name="predicted_jobs.csv")
