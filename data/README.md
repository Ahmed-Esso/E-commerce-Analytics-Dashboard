# Data Files

This directory contains sample data files used for the E-commerce Analytics Dashboard.

## Files

### sample_advanced_ecommerce_analytics.csv
Sample of the raw e-commerce transaction data (first 10 rows out of 15,000+).

### sample_cleaned_ecommerce_data.csv
Sample of the cleaned and processed data with calculated metrics:
- Average Order Value
- Revenue per Customer
- Discount Amount
- Gross Revenue
- Net Revenue
- ROI
- Conversion Rate

## Full Dataset

The full dataset contains 15,000+ records with the following columns:

### Transaction Data
- `order_id`: Unique order identifier
- `date`: Order date
- `customer_id`: Customer identifier
- `price`: Product price
- `quantity`: Items purchased
- `discount_percent`: Discount applied
- `final_amount`: Final transaction amount

### Customer Demographics
- `age`: Customer age
- `gender`: Customer gender
- `city`: Customer city
- `region`: Geographic region (Greater Cairo, Delta, Upper Egypt, etc.)
- `income`: Customer income bracket

### Segmentation
- `customer_segment`: Budget, Regular, Premium, VIP, First-time
- `marketing_campaign`: Campaign type (Flash Sale, Holiday Special, etc.)
- `marketing_channel`: Acquisition channel (Email, TV, Social Media, etc.)
- `device_type`: Device used (Mobile, Desktop, Tablet)

### Metrics
- `satisfaction_rating`: Customer satisfaction (1-5)
- `returned`: Whether item was returned
- `customer_lifetime_value`: CLV calculation
- `retention_score`: Customer retention score
