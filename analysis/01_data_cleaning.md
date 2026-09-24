# Data Cleaning Documentation
## Supermarket Sales Analysis — 2024

---

## 1. Dataset Overview

| Attribute | Value |
|---|---|
| File | `data/supermarket_sales.csv` |
| Total Records | 500 |
| Total Columns | 13 |
| Date Range | January 2024 – December 2024 |
| Analysis Platform | Google Colab (Python) |

---

## 2. Column Schema

| Column | Data Type | Description |
|---|---|---|
| Invoice ID | String | Unique transaction identifier (INV-001 … INV-500) |
| Date | Date (YYYY-MM-DD) | Transaction date |
| Branch | String | Store branch (Branch A / B / C) |
| City | String | City of the branch (Delhi / Bangalore / Mumbai) |
| Customer Type | String | Member or Normal customer |
| Gender | String | Male or Female |
| Product | String | Product name (15 distinct products) |
| Category | String | Product category (6 categories) |
| Quantity | Integer | Units purchased per transaction |
| Unit Price | Float (₹) | Price per unit |
| Payment | String | Payment method (UPI / Cash / Credit Card) |
| Rating | Float (1–5) | Customer satisfaction rating |
| Sales | Float (₹) | Total sales value = Quantity × Unit Price |

---

## 3. Missing Value Analysis

All 500 records were examined for null or blank values.

| Column | Missing Values | Action |
|---|---|---|
| Invoice ID | 0 | No action required |
| Date | 0 | No action required |
| Branch | 0 | No action required |
| City | 0 | No action required |
| Customer Type | 0 | No action required |
| Gender | 0 | No action required |
| Product | 0 | No action required |
| Category | 0 | No action required |
| Quantity | 0 | No action required |
| Unit Price | 0 | No action required |
| Payment | 0 | No action required |
| Rating | 0 | No action required |
| Sales | 0 | No action required |

**Result:** Dataset is complete — no missing values detected.

---

## 4. Duplicate Records Check

- **Duplicate rows checked:** Invoice ID column scanned for repeated values.
- **Duplicates found:** 0
- **Action:** No records removed.

---

## 5. Data Type Validation

| Column | Expected Type | Actual Type | Status |
|---|---|---|---|
| Date | datetime | object → converted to datetime | ✅ Corrected |
| Quantity | int | int64 | ✅ OK |
| Unit Price | float | float64 | ✅ OK |
| Sales | float | float64 | ✅ OK |
| Rating | float | float64 | ✅ OK |
| All text columns | string | object | ✅ OK |

**Transformation applied:**
```python
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
df['Month_Num'] = df['Date'].dt.month
```

---

## 6. Sales Column Validation

The Sales column was verified against the formula:

```
Sales = Quantity × Unit Price
```

- All 500 rows pass validation.
- No arithmetic inconsistencies detected.

---

## 7. Categorical Value Standardisation

| Column | Distinct Values | Issues Found | Action |
|---|---|---|---|
| Branch | Branch A, Branch B, Branch C | None | No action |
| City | Delhi, Bangalore, Mumbai | None | No action |
| Customer Type | Member, Normal | None | No action |
| Gender | Male, Female | None | No action |
| Payment | UPI, Cash, Credit Card | None | No action |
| Category | Beverages, Dairy, Snacks, Grains, Bakery, Grocery | None | No action |

---

## 8. Outlier Assessment

| Column | Min | Max | Observations |
|---|---|---|---|
| Sales | ₹90.00 | ₹1,200.00 | No extreme outliers; high-value transactions are valid (Paneer, Cheese at high quantity) |
| Rating | 3.5 | 4.8 | Within expected 1–5 scale |
| Quantity | 1 | 6 | Normal range for retail transactions |
| Unit Price | ₹45.00 | ₹200.00 | Consistent with product categories |

**Decision:** No records removed as outliers. All values fall within plausible retail ranges.

---

## 9. Final Dataset Statistics (Post-Cleaning)

| Metric | Value |
|---|---|
| Total Records | 500 |
| Records Removed | 0 |
| Columns Added | Month, Month_Num |
| Null Values | 0 |
| Duplicate Records | 0 |
| Date Range | 01-Jan-2024 to 31-Dec-2024 |

---

## 10. Cleaning Summary

The dataset required minimal cleaning:
- The `Date` column was converted from string to datetime format.
- Two derived columns (`Month`, `Month_Num`) were added to support monthly trend analysis.
- All 500 records are valid and retained for analysis.

**Dataset status: Clean and ready for analysis.**
