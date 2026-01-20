# E-commerce Data Analysis
# Complete analysis notebook converted to Python script

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# =============================================================================
# SECTION 1: DATA LOADING AND CLEANING
# =============================================================================

# Load the raw data
df = pd.read_csv("data/sample_advanced_ecommerce_analytics.csv")

# Remove duplicates and handle missing values
df = df.drop_duplicates()
df = df.replace(["-", "--", "NA", "N/A", "", "null"], pd.NA)

# Drop rows with missing required columns
required_cols = ['price', 'quantity', 'final_amount']
df = df.dropna(subset=required_cols)

# Convert numeric columns
numeric_cols = [
    'age', 'income', 'price', 'quantity', 'discount_percent',
    'final_amount', 'customer_lifetime_value', 'retention_score',
    'days_since_registration'
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# =============================================================================
# SECTION 2: FEATURE ENGINEERING
# =============================================================================

# Calculate derived metrics
df['Average Order Value'] = df['final_amount'] / df['quantity']
df['revenue_per_customer'] = df['final_amount'] / df['customer_id'].nunique()
df['discount_amount'] = df['price'] * df['discount_percent'] / 100
df['gross_revenue'] = df['price'] * df['quantity']
df['net_revenue'] = df['final_amount']
df['roi'] = (df['net_revenue'] - df['discount_amount']) / df['discount_amount']

# Calculate conversion rate
orders_per_customer = df.groupby('customer_id').size()
df['conversion_rate'] = df['customer_id'].map(orders_per_customer)

# =============================================================================
# SECTION 3: KPI CALCULATIONS
# =============================================================================

# Overall Conversion Rate
total_customers = df['customer_id'].nunique()
total_orders = len(df)
conversion_rate = total_orders / total_customers

print(f"Overall Conversion Rate: {conversion_rate:.2f}")

# KPI by Category
kpi_category = df.groupby('category').agg({
    'gross_revenue': 'sum',
    'net_revenue': 'sum',
    'discount_amount': 'sum',
    'quantity': 'sum'
})
kpi_category['avg_order_value'] = kpi_category['net_revenue'] / kpi_category['quantity']
kpi_category['roi'] = (kpi_category['net_revenue'] - kpi_category['discount_amount']) / kpi_category['discount_amount']
print("\nKPI by Category:")
print(kpi_category)

# KPI by Marketing Channel
kpi_channel = df.groupby('marketing_channel').agg({
    'net_revenue': 'sum',
    'gross_revenue': 'sum',
    'discount_amount': 'sum',
    'quantity': 'sum',
    'customer_id': 'nunique'
})
kpi_channel['avg_order_value'] = kpi_channel['net_revenue'] / kpi_channel['quantity']
kpi_channel['revenue_per_customer'] = kpi_channel['net_revenue'] / kpi_channel['customer_id']
kpi_channel['roi'] = (kpi_channel['net_revenue'] - kpi_channel['discount_amount']) / kpi_channel['discount_amount']
print("\nKPI by Marketing Channel:")
print(kpi_channel)

# KPI by Customer Segment
kpi_segment = df.groupby('customer_segment').agg({
    'net_revenue': 'sum',
    'gross_revenue': 'sum',
    'discount_amount': 'sum',
    'quantity': 'sum',
    'customer_id': 'nunique',
    'customer_lifetime_value': 'mean',
    'retention_score': 'mean'
})
kpi_segment['avg_order_value'] = kpi_segment['net_revenue'] / kpi_segment['quantity']
kpi_segment['revenue_per_customer'] = kpi_segment['net_revenue'] / kpi_segment['customer_id']
print("\nKPI by Customer Segment:")
print(kpi_segment)

# =============================================================================
# SECTION 4: MARKETING CHANNEL ANALYSIS
# =============================================================================

channel_perf = df.groupby('marketing_channel').agg({
    'discount_percent': 'sum',
    'final_amount': 'sum',
    'customer_id': 'nunique',
})

channel_perf['total_spend'] = channel_perf['discount_percent']
channel_perf['total_revenue'] = channel_perf['final_amount']
channel_perf['total_conversions'] = channel_perf['customer_id']
channel_perf['avg_roi'] = (
    (channel_perf['total_revenue'] - channel_perf['total_spend'])
    / channel_perf['total_spend']
)

best_revenue = channel_perf['total_revenue'].idxmax()
best_roi = channel_perf['avg_roi'].idxmax()
best_conversions = channel_perf['total_conversions'].idxmax()

print(f"\nHighest Revenue Channel: {best_revenue}")
print(f"Best ROI Channel: {best_roi}")
print(f"Most Conversions Channel: {best_conversions}")

# =============================================================================
# SECTION 5: VISUALIZATIONS
# =============================================================================

# Light theme layout
light_layout = dict(
    plot_bgcolor="#FFFFFF",
    paper_bgcolor="#FFFFFF",
    font_color="#040D2F",
    title_x=0.5,
    yaxis=dict(showgrid=True, gridcolor="#E0E0E0", zeroline=False, tickfont=dict(color="black")),
    xaxis=dict(showgrid=True, gridcolor="#E0E0E0", tickangle=45, tickfont=dict(color="black"))
)

# Revenue per Order by Channel
performance_by_channel = df.groupby('marketing_channel').agg({
    'final_amount': ['sum', 'mean'],
    'order_id': 'count',
    'customer_id': 'nunique'
}).reset_index()
performance_by_channel.columns = ['Channel', 'Total_Revenue', 'Avg_Order_Value', 'Total_Orders', 'Unique_Customers']
performance_by_channel['Revenue_Per_Order'] = (performance_by_channel['Total_Revenue'] / performance_by_channel['Total_Orders']).round(2)
performance_by_channel = performance_by_channel.sort_values('Revenue_Per_Order')

fig_performance = px.bar(
    performance_by_channel, x='Revenue_Per_Order', y='Channel', orientation='h',
    title='Revenue Per Order by Channel',
    color='Revenue_Per_Order',
    color_continuous_scale=['#3647F5', '#D9D9D9', '#FF9F0D']
)
fig_performance.update_layout(**light_layout, height=450)
fig_performance.show()

# Customer Acquisition Rate by Channel
conversion_by_channel = df.groupby('marketing_channel').agg({
    'customer_id': 'nunique',
    'order_id': 'count'
}).reset_index()
conversion_by_channel.columns = ['Channel', 'Unique_Customers', 'Total_Orders']
conversion_by_channel['Customer_Acquisition_Rate_%'] = (
    (conversion_by_channel['Unique_Customers'] / conversion_by_channel['Total_Orders']) * 100
).round(2)
conversion_by_channel = conversion_by_channel.sort_values('Customer_Acquisition_Rate_%', ascending=False)

fig_conv = px.bar(
    conversion_by_channel, x='Channel', y='Customer_Acquisition_Rate_%',
    title='Customer Acquisition Rate by Channel',
    color='Customer_Acquisition_Rate_%',
    color_continuous_scale=['#3647F5', '#D9D9D9', '#FF9F0D']
)
fig_conv.update_layout(**light_layout, height=450)
fig_conv.show()

# Channel Efficiency Ranking
efficiency = df.groupby('marketing_channel').agg({
    'final_amount': ['sum', 'mean'],
    'order_id': 'count',
    'customer_id': 'nunique'
}).reset_index()
efficiency.columns = ['Channel', 'Total_Revenue', 'Avg_Order_Value', 'Total_Orders', 'Unique_Customers']
efficiency['Revenue_Per_Order'] = (efficiency['Total_Revenue'] / efficiency['Total_Orders']).round(2)
efficiency['Customer_Acq_Rate_%'] = ((efficiency['Unique_Customers'] / efficiency['Total_Orders']) * 100).round(2)

max_rev = efficiency['Revenue_Per_Order'].max()
max_cust = efficiency['Customer_Acq_Rate_%'].max()
max_order = efficiency['Avg_Order_Value'].max()

efficiency['Efficiency_Score'] = (
    (efficiency['Revenue_Per_Order'] / max_rev) * 40 +
    (efficiency['Customer_Acq_Rate_%'] / max_cust) * 30 +
    (efficiency['Avg_Order_Value'] / max_order) * 30
).round(2)
efficiency = efficiency.sort_values('Efficiency_Score')

fig_efficiency = px.bar(
    efficiency, x='Efficiency_Score', y='Channel', orientation='h',
    title='Channel Efficiency Ranking',
    color='Efficiency_Score',
    color_continuous_scale=['#3647F5', '#D9D9D9', '#FF9F0D']
)
fig_efficiency.update_layout(**light_layout, height=450)
fig_efficiency.show()

# Revenue vs Customer Acquisition
revenue_analysis = df.groupby('marketing_channel').agg({
    'final_amount': 'sum',
    'customer_id': 'nunique',
    'order_id': 'count'
}).reset_index()
revenue_analysis.columns = ['Channel', 'Total_Revenue', 'Unique_Customers', 'Total_Orders']
revenue_analysis['Revenue_Per_Customer'] = (revenue_analysis['Total_Revenue'] / revenue_analysis['Unique_Customers']).round(2)

fig_scatter = px.scatter(
    revenue_analysis, x='Unique_Customers', y='Total_Revenue',
    size='Revenue_Per_Customer', color='Revenue_Per_Customer', text='Channel',
    title='Revenue vs Customer Acquisition',
    color_continuous_scale=['#FF9F0D', '#3647F5', '#D9D9D9']
)
fig_scatter.update_traces(textposition='top center', marker=dict(line=dict(width=2, color='#040D2F'), opacity=0.85))
fig_scatter.update_layout(**light_layout, height=500)
fig_scatter.show()

print("\nAnalysis Complete!")
