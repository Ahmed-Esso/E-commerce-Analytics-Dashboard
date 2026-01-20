# 📊 E-commerce Analytics Dashboard

A comprehensive e-commerce analytics solution featuring a Streamlit dashboard and Python data analysis scripts for analyzing customer behavior, marketing performance, and sales metrics.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://e-commerce-analytics-dashboard-ga4tczet8rminqltnfbzyv.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-green.svg)

## 🚀 Live Demo

**👉 [View Live Dashboard](https://e-commerce-analytics-dashboard-ga4tczet8rminqltnfbzyv.streamlit.app/)**

## 🌟 Features

### Interactive Dashboard (app.py)
- **Home Page**: Executive summary with key KPIs and performance overview
- **Analytics Dashboard**: Deep-dive analysis with multiple visualization types
- **Data Explorer**: Interactive data filtering and exploration tools
- **About Page**: Project documentation and methodology

### Data Analysis (notebooks/)
- Data cleaning and preprocessing pipeline
- KPI calculations by category, channel, segment, and region
- Marketing channel performance analysis
- Customer segmentation and CLV analysis
- Trend analysis with seasonal patterns

## 📁 Project Structure

```
E-commerce-Analytics-Dashboard/
├── app.py                              # Streamlit dashboard application
├── requirements.txt                    # Python dependencies
├── data/
│   ├── README.md                       # Data documentation
│   ├── sample_advanced_ecommerce_analytics.csv   # Raw data sample
│   └── cleaned_ecommerce_data.csv      # Processed data
└── notebooks/
    └── ecommerce_analysis.py           # Data analysis script
```

## 🚀 Quick Start

### Option 1: Use the Live App
Visit the [Live Dashboard](https://e-commerce-analytics-dashboard-pbb.streamlit.app/) - no installation required!

### Option 2: Run Locally

#### 1. Clone the Repository
```bash
git clone https://github.com/Ahmed-Esso/E-commerce-Analytics-Dashboard.git
cd E-commerce-Analytics-Dashboard
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Run the Dashboard
```bash
streamlit run app.py
```

#### 4. Run the Analysis Script
```bash
python notebooks/ecommerce_analysis.py
```

## 📊 Key Metrics Analyzed

### Revenue & Sales
- Total Revenue, Gross Revenue, Net Revenue
- Average Order Value (AOV)
- Revenue per Customer
- Revenue growth trends

### Customer Analytics
- Customer Lifetime Value (CLV)
- Retention Score
- Customer Segmentation (Budget, Regular, Premium, VIP, First-time)
- Customer acquisition by channel

### Marketing Performance
- ROI by campaign and channel
- Conversion rates
- Channel efficiency scores
- Marketing spend analysis

### Geographic Insights
- Regional performance (Greater Cairo, Delta, Upper Egypt, etc.)
- City-level analysis
- Regional revenue distribution

## 🎨 Visualizations

The project includes 15+ interactive visualizations:
- Lollipop charts for revenue analysis
- Bubble charts for customer metrics
- Line charts for trend analysis
- Horizontal bar charts for channel comparison
- Scatter plots for performance quadrants

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit**: Web dashboard framework
- **Pandas**: Data manipulation
- **Plotly**: Interactive visualizations
- **NumPy**: Numerical computations

## 📈 Data Schema

| Column | Description |
|--------|-------------|
| order_id | Unique order identifier |
| date | Transaction date |
| customer_id | Customer identifier |
| category | Product category |
| subcategory | Product subcategory |
| price | Product price |
| quantity | Items purchased |
| discount_percent | Discount applied |
| final_amount | Final transaction amount |
| marketing_channel | Acquisition channel |
| customer_segment | Customer segment |
| customer_lifetime_value | CLV calculation |
| retention_score | Retention score |

## 👥 The Team
This work was a collaborative effort by:
* **[@Ahmed-Esso](https://github.com/Ahmed-Esso)** | [LinkedIn](https://www.linkedin.com/in/-ahmed-essam-/) (Team Leader)
* **[@Mayar-Hany](https://github.com/Mayar-hany-2005)** | [LinkedIn](https://www.linkedin.com/in/mayar-h-139a2a2a6)
* **[@Toqa10](https://github.com/Toqa10)** | [LinkedIn](https://www.linkedin.com/in/toqa-mohammed-mahfouz/)
* **[@ZiadAbdeen](https://github.com/ZiadAbdeen)** | [LinkedIn](https://www.linkedin.com/in/ziad-abdeen-kamal-a138a0356/)
  
## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ Star this repository if you find it helpful!
