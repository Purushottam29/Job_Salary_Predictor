# 💼 Job Salary Predictor

**Job Salary Predictor** is an end-to-end project that scrapes job listings from online job boards, predicts potential salaries using a Machine Learning model, and provides an interactive web interface via **Streamlit**.

The project demonstrates **web scraping**, **machine learning**, and **web app deployment** skills in one complete package.

---

## 📌 Features

* 🌐 **Web Scraping:** Extracts job titles, companies, tags, links—and **salaries** when available—from online job boards.
* 🤖 **Machine Learning:** Uses scikit-learn (Random Forest) to predict salaries based on job titles and skills required.
* 💻 **Web Interface:** Built using Streamlit → Upload a CSV → Get predicted salaries → Download results.
* 🚀 **Deployable to Streamlit Cloud:** Share your app live with others.

---

## ⚙️ Technologies Used

| Tool / Library  | Purpose                                          |
| --------------- | ------------------------------------------------ |
| `requests`      | Making HTTP requests to websites                 |
| `BeautifulSoup` | Parsing HTML content for scraping                |
| `pandas`        | Working with datasets (CSV, DataFrames)          |
| `scikit-learn`  | Machine learning model (RandomForest)            |
| `streamlit`     | Web interface and visualization                  |
| `joblib`        | Saving and loading ML models                     |
| `selenium`      | **For scraping dynamic websites like Wellfound** |

---

## 🗂️ Project Structure

```
job-salary-predictor/
├── scraper.py          # Web scraper script
├── model.py            # ML model training script
├── app.py              # Streamlit web app
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🚨 Why Selenium?

Websites like **Wellfound (AngelList)** **load job data dynamically using JavaScript** after the initial page load.

* **BeautifulSoup** alone can **only parse static HTML**, meaning dynamically loaded content *won’t be present* in the response.
* **Selenium** **automates a real browser**, loads the page completely (including dynamic JavaScript), and **extracts fully rendered content**.

> ✅ **In short:**
> Use **BeautifulSoup** → For **static websites** or HTML pages
> Use **Selenium** → For **dynamic content** or JavaScript-loaded websites (like Wellfound)

---

## 💾 Installation & Setup

```bash
# Clone the repository
git clone git@github.com:your-username/job-salary-predictor.git
cd job-salary-predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## 📋 Example CSV Structure

| Title          | Tags                          |
| -------------- | ----------------------------- |
| Data Scientist | Python, Machine Learning, SQL |

---

## 📄 Future Improvements

* ✅ Scraping more job boards
* ✅ Adding **location** or **experience** as features
* ✅ Using real-world salary datasets for training better ML models
* ✅ Adding visualization charts (Streamlit + Plotly)

---

## 👨‍💻 Author

**Purushottam Choudhary**
GitHub: [@Purushottam29](https://github.com/Purushottam29)

---
Deployed Link: https://jobsalarypredictor-khbbnpkp8jsoshtllqzmu2.streamlit.app/

