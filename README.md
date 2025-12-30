# 📱 Smartprix Smartphone Web Scraper (Selenium + BeautifulSoup)

Automated scraping system for **Smartprix Mobile Listings** to extract smartphone data, load dynamic content, save HTML, and prepare datasets for analytics, ML models, and recommendation systems.

---

### 🚀 Project Overview
#### 🌐 What is Smartprix?
Smartprix is a leading Indian product discovery and price comparison platform that aggregates detailed specifications and real-time pricing for electronics across 100+ online retailers. It helps shoppers make informed buying decisions by providing expert reviews, price history tracking, and side-by-side comparison tools for gadgets like smartphones and laptops.

---

### 🎯 Problem Statement
As a Data Analyst you must **gather and clean smartphone data** from the Smartprix website to perform:

1. **Analytics & Dashboards** for insights like:
   - Which brands are dominating each price segment?
   - Specs that impact price the most (Regression Insight)?
   - Yearly trend: Are smartphones becoming costlier or cheaper?
   - Cross brand comparison (Xiaomi vs Samsung vs iQOO, etc.)

2. **Machine Learning:**
   - Build a **phone price prediction model** based on specifications.

3. **Recommendation System:**
   - Suggest similar phones based on brand + specification similarity.

---

### ⚠️ The Problem with Smartprix Website
- Website: https://www.smartprix.com/mobiles/
- It is a **dynamic website**, loading data using JavaScript.
- By default, the page displays **only 20 phones**.
- To load more data, the user must click **"LOAD MORE"** repeatedly.
- Using **Requests + BeautifulSoup alone fails** because:
  - It fetches only initial HTML
  - It cannot click buttons or load more phones
  - It only retrieves the first 20 products

---

### 💡 Why Selenium is Needed
To solve this limitation, we use **Selenium** to:
- Automate Chrome Browser
- Apply filters (remove Out of Stock / Upcoming)
- Click "LOAD MORE" until end of page
- Load full dynamic content
- Download the **entire HTML** for parsing with BeautifulSoup later

This enables complete data collection for Analytics, ML Models, and Recommendation Engines.

---

## 🛠️ Tech Stack Used

| Tool / Library                                                                 | Purpose |
|------------------------------------------------------------------------------------------|----------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)        | Core programming language |
| ![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=white)  | Automates Chrome & loads dynamic content |
| ![Chrome](https://img.shields.io/badge/ChromeDriver-4285F4?logo=googlechrome&logoColor=white) | Simulate & Executes browser actions with Selenium |
| ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-FFD43B?logo=python&logoColor=black) | Parses HTML & extracts phone data |


---
## 📦 Installation & Setup

Follow these steps to install Selenium, ChromeDriver, and BeautifulSoup for Smartprix web scraping.

---

### ✔️ 1️⃣ Install Required Python Libraries
```bash
pip install selenium
pip install bs4
```

---

### ✔️ 2️⃣ Install ChromeDriver (Required for Selenium)
Since we are automating the Chrome browser, we need ChromeDriver.

#### 🔍 Step: Check Your Chrome Version
Open Chrome and visit:
```
chrome://settings/help
```
Example:
```
Version: 143.0.7499.170
```

#### 📥 Step: Download Matching ChromeDriver (one version before your Chrome)
Example:
```
https://storage.googleapis.com/chrome-for-testing-public/143.0.7499.169/win64/chromedriver-win64.zip
```

#### 📁 Step: Extract & Save Driver
1. Extract the zip
2. Find `chromedriver.exe`
3. Copy the path location which can be used in python script.

---


