# 📊 E-commerce Analytics Dashboard

A comprehensive business intelligence solution for e-commerce performance analysis built with Python, Streamlit, and Plotly.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-green.svg)

## 🎯 Overview

This project provides end-to-end analytics for e-commerce platforms, featuring:
- **Interactive Dashboard** with real-time filtering
- **15+ Data Visualizations** for marketing channel performance
- **7 KPI Tabs** covering category, campaign, channel, segment, region, and time analysis
- **Data Explorer** with export capabilities

## 📈 Key Insights

- **+8,414%** Revenue Growth (Jan 2021 - Jan 2024)
- **+5,046%** Customer Conversions Growth
- **Email Marketing** delivers highest ROI (140.65%)
- **Direct Channel** leads in customer acquisitions (1,066 customers)

## 🚀 Features

### 🏠 Home Page
- Executive KPI summary cards
- Key business insights at a glance
- Channel performance highlights
- Strategic recommendations

### 📊 Analytics Dashboard
- Real-time filtering by channel and date range
- Monthly revenue and conversion trends
- Marketing channel performance analysis
- Efficiency scoring and ROI calculations
- Performance quadrant analysis

### 🔍 Data Explorer
- Full dataset browsing
- Multi-filter capabilities (category, region, segment)
- CSV export for offline analysis

### ℹ️ About
- Complete dataset documentation
- Data processing pipeline overview
- Metrics definitions

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** - Web application framework
- **Plotly Express** - Interactive visualizations
- **Pandas** - Data manipulation and analysis

## 📁 Project Structure

```
├── app.py                          # Streamlit dashboard application
├── Data_Analysis_Notebook.ipynb    # Jupyter notebook with analysis
├── data/
│   ├── advanced_ecommerce_analytics.csv   # Raw dataset
│   └── cleaned_ecommerce_data.csv         # Processed dataset
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## 📊 Dataset

| Metric | Value |
|--------|-------|
| Records | 15,000+ |
| Time Period | Jan 2021 - Jan 2024 |
| Columns | 38 features |
| Marketing Channels | 12 |
| Product Categories | 15 |
| Regions | 7 |

### Key Columns
- **Identifiers:** order_id, customer_id
- **Financial:** net_revenue, gross_revenue, discount_amount, roi
- **Marketing:** marketing_channel, marketing_campaign
- **Customer:** customer_segment, retention_score, customer_lifetime_value
- **Temporal:** date, month, quarter, season

## 🚀 Getting Started

### Prerequisites

```bash
pip install streamlit pandas plotly
```

### Running the App

```bash
streamlit run app.py
```

### Running the Notebook

Open `Data_Analysis_Notebook.ipynb` in Jupyter Lab or VS Code.

## 📈 Sample Visualizations

1. **Monthly Revenue Trends by Channel** - Line charts showing revenue evolution
2. **Channel Efficiency Ranking** - Horizontal bar chart with efficiency scores
3. **Performance Quadrant** - Scatter plot with customer vs revenue analysis
4. **ROI by Channel** - Color-coded bar charts
5. **Customer Acquisition Rates** - Comparative bar charts

## 🎓 Use Cases

- **Executives:** High-level KPIs and strategic insights
- **Marketing Teams:** Channel performance and campaign ROI
- **Data Analysts:** Deep-dive analysis and data exploration
- **Business Intelligence:** Trend analysis and forecasting

## 📝 License

This project is for educational and portfolio purposes.

## 👤 Author

**Ahmed Essam**
- GitHub: [@Ahmed-Esso](https://github.com/Ahmed-Esso)
- Portfolio: [ahmed-essam.framer.website](https://ahmed-essam.framer.website/)

---

⭐ Star this repo if you find it helpful!