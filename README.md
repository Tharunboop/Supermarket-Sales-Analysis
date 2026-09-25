# Supermarket Sales Analysis

**IBM SkillsBuild | Data Analytics Project**

A complete business intelligence project analysing 500 supermarket transactions across three branches (Delhi, Bangalore, Mumbai) for the full calendar year 2024.

---

## Verified Final Results

| KPI | Value |
|---|---|
| **Total Sales** | ₹2,44,411.08 |
| **Total Transactions** | 500 |
| **Average Transaction Value** | ₹488.82 |
| **Average Customer Rating** | 3.99 / 5 |
| **Total Quantity Sold** | 2,768 units |
| **Top Product** | Cheese |
| **Top Category** | Beverages |
| **Top Branch** | Branch C |
| **Top City** | Mumbai |
| **Most Used Payment Method** | UPI |

---

## Project Structure

```
Supermarket-Sales-Analysis/
│
├── data/
│   └── supermarket_sales.csv                         # 500-row cleaned dataset
│
├── analysis/
│   ├── 01_data_cleaning.md                           # Data cleaning documentation
│   ├── 02_eda.md                                     # Exploratory data analysis
│   ├── 03_kpi_analysis.md                            # KPI analysis
│   ├── 04_product_analysis.md                        # Product analysis
│   ├── 05_category_analysis.md                       # Category analysis
│   ├── 06_branch_analysis.md                         # Branch analysis
│   ├── 07_city_analysis.md                           # City analysis
│   ├── 08_payment_analysis.md                        # Payment analysis
│   ├── 09_customer_type_analysis.md                  # Customer type analysis
│   ├── 10_monthly_sales_trend.md                     # Monthly sales trend
│   └── 11_rating_analysis.md                         # Rating analysis
│
├── docs/
│   ├── key_findings.md                               # 10 key analytical findings
│   ├── business_decisions.md                         # 8 data-driven business decisions
│   └── conclusion.md                                 # Project conclusion
│
├── charts/
│   ├── visualizations.py                             # Python script to generate all charts
│   ├── 01_kpi_summary.png
│   ├── 02_monthly_sales_trend.png
│   ├── 03_sales_by_category.png
│   ├── 04_top_products.png
│   ├── 05_sales_by_branch.png
│   ├── 06_payment_distribution.png
│   ├── 07_customer_type_comparison.png
│   ├── 08_rating_distribution.png
│   └── 09_sales_by_city.png
│
├── report/
│   └── Supermarket_Sales_Analysis_Report.pdf         # Final project report (PDF)
│
├── ChettukadiTharun_Supermarket_Sales_Analysis.ipynb # Jupyter Notebook
├── ChettukadiTharun_ProjectReport.docx               # Project Report (Word)
├── requirements.txt                                  # Python dependencies
└── README.md                                         # This file
```

---

## Dataset Schema

| Column | Type | Description |
|---|---|---|
| Invoice ID | String | Unique transaction ID |
| Date | Date | Transaction date (YYYY-MM-DD) |
| Branch | String | Branch A / B / C |
| City | String | Delhi / Bangalore / Mumbai |
| Customer Type | String | Member / Normal |
| Gender | String | Female / Male |
| Product | String | 15 distinct products |
| Category | String | 6 categories |
| Quantity | Integer | Units purchased |
| Unit Price | Float (₹) | Price per unit |
| Payment | String | UPI / Cash / Credit Card |
| Rating | Float | 3.5 – 4.8 |
| Sales | Float (₹) | Quantity × Unit Price |

---

## How to Run the Visualizations

### Option 1 — Local Python

```bash
pip install -r requirements.txt
python charts/visualizations.py
```

### Option 2 — Google Colab

1. Upload `data/supermarket_sales.csv` to your Colab environment.
2. Open `ChettukadiTharun_Supermarket_Sales_Analysis.ipynb`.
3. Update the `DATA_PATH` variable if needed and run all cells.

Charts are saved to the `charts/` directory.

---

## Analysis Coverage

| # | Analysis Module | File |
|---|---|---|
| 1 | Data Cleaning | `analysis/01_data_cleaning.md` |
| 2 | Exploratory Data Analysis | `analysis/02_eda.md` |
| 3 | KPI Analysis | `analysis/03_kpi_analysis.md` |
| 4 | Product Analysis | `analysis/04_product_analysis.md` |
| 5 | Category Analysis | `analysis/05_category_analysis.md` |
| 6 | Branch Analysis | `analysis/06_branch_analysis.md` |
| 7 | City Analysis | `analysis/07_city_analysis.md` |
| 8 | Payment Analysis | `analysis/08_payment_analysis.md` |
| 9 | Customer Type Analysis | `analysis/09_customer_type_analysis.md` |
| 10 | Monthly Sales Trend | `analysis/10_monthly_sales_trend.md` |
| 11 | Rating Analysis | `analysis/11_rating_analysis.md` |
| 12 | Key Findings | `docs/key_findings.md` |
| 13 | Business Decisions | `docs/business_decisions.md` |
| 14 | Conclusion | `docs/conclusion.md` |

---

## Key Findings Summary

1. **Beverages** is the top category — 169 transactions (33.8%), ₹1,17,511.08 revenue (48.1% of total).
2. **Cheese** is the top product — ₹58,066.08 revenue, 55 transactions, 313 units sold.
3. **Branch C (Mumbai)** leads all three branches — ₹87,956.58 (36.0% of revenue).
4. **70.4% of transactions are cashless** — UPI 38.8% (194 txn), Credit Card 31.6% (158 txn).
5. **Customer types are closely matched** — Member 52.8% (264 txn, ATV ₹483.32), Normal 47.2% (236 txn, ATV ₹495.00).
6. **April 2024 is the peak-revenue month (₹22,495)** — December 2024 is the lowest (₹17,361.50).
7. **Average rating of 3.99/5** — solid floor, with room to reach 4.2+.
8. **Q4 is the weakest quarter** — ₹58,409.00 (23.9% of annual revenue); Q1 is the strongest (₹62,788.58).

---

## Business Decisions Summary

1. Protect premium product supply chain (Cheese, Paneer).
2. Launch Q4 revival campaign (Oct–Dec).
3. Convert Normal customers to Members.
4. Invest in UPI payment infrastructure reliability.
5. Implement branch-specific promotional strategies.
6. Expand Bakery and Grocery product range.
7. Target 4.2+ average customer rating.
8. Reduce cash dependency at Branch A (Delhi).

---

## Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python 3.10+ | Primary programming language |
| Pandas | Data loading, cleaning, analysis |
| Matplotlib | Chart generation |
| Seaborn | Statistical visualisation |
| Jupyter Notebook | Interactive analysis environment |
| Google Colab | Cloud-based notebook execution |
| Microsoft Word (.docx) | Project report |

---

## Outputs

| Output | Path |
|---|---|
| Cleaned dataset | `data/supermarket_sales.csv` |
| Jupyter Notebook | `ChettukadiTharun_Supermarket_Sales_Analysis.ipynb` |
| Project Report | `ChettukadiTharun_ProjectReport.docx` |
| KPI Dashboard chart | `charts/01_kpi_summary.png` |
| Monthly trend chart | `charts/02_monthly_sales_trend.png` |
| Category sales chart | `charts/03_sales_by_category.png` |
| Top products chart | `charts/04_top_products.png` |
| Branch sales chart | `charts/05_sales_by_branch.png` |
| Payment distribution | `charts/06_payment_distribution.png` |
| Customer type comparison | `charts/07_customer_type_comparison.png` |
| Rating distribution | `charts/08_rating_distribution.png` |
| City sales chart | `charts/09_sales_by_city.png` |

---

## Requirements

```
pandas>=2.0
matplotlib>=3.7
seaborn>=0.13
```

Install with:

```bash
pip install -r requirements.txt
```

---

## Author

**Name:** Chettukadi Tharun
**Programme:** IBM SkillsBuild Data Analytics
**Year:** 2024

---

## GitHub Repository

```
https://github.com/ChettukadiTharun/Supermarket-Sales-Analysis
```

*(Add your GitHub repository URL here after creating the repository.)*

---

## Project Information

| Attribute | Value |
|---|---|
| Project Title | Supermarket Sales Analysis |
| Analysis Period | January 2024 – December 2024 |
| Author | Chettukadi Tharun |
| Platform | Google Colab |
| Language | Python 3 |
| Transactions Analysed | 500 |
| Total Revenue Verified | ₹2,44,411.08 |
