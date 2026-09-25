# Exploratory Data Analysis (EDA)
## Supermarket Sales Analysis — 2024

---

## 1. Dataset Shape

| Metric | Value |
|---|---|
| Rows | 500 |
| Columns | 13 |
| Date Range | January 2024 – December 2024 |
| Branches | 3 (Branch A, Branch B, Branch C) |
| Cities | 3 (Delhi, Bangalore, Mumbai) |

---

## 2. Descriptive Statistics

### Numerical Columns

| Column | Min | Max | Mean | Median |
|---|---|---|---|---|
| Sales (₹) | 90.00 | 1,200.00 | 488.82 | 390.00 |
| Quantity | 1 | 6 | 3.54 | 4 |
| Unit Price (₹) | 45.00 | 200.00 | 107.50 | 95.00 |
| Rating | 3.5 | 4.8 | 3.99 | 4.0 |

### Categorical Columns

| Column | Unique Values | Most Frequent |
|---|---|---|
| Branch | 3 | Branch C |
| City | 3 | Mumbai |
| Product | 15 | Cheese |
| Category | 6 | Beverages |
| Customer Type | 2 | Member |
| Gender | 2 | Female |
| Payment | 3 | UPI |

---

## 3. Distribution Analysis

### Sales Distribution

- Sales range from ₹90 to ₹1,200 per transaction.
- Average transaction value: **₹488.82**
- The distribution is right-skewed, driven by high-value Paneer and Cheese transactions.
- Most transactions fall in the ₹200–₹750 range.

### Quantity Distribution

- Quantity sold per transaction ranges from 1 to 6 units.
- Average quantity per transaction: **3.54 units**
- The quantity distribution is approximately uniform across values 2–6.

### Rating Distribution

- Ratings range from 3.5 to 4.8.
- Average rating: **3.99 / 5**
- Ratings cluster between 3.7 and 4.5.
- No ratings below 3.5 or above 4.8 observed.

---

## 4. Category Breakdown

| Category | Transaction Count | % Share |
|---|---|---|
| Beverages | ~180 | 36.0% |
| Dairy | ~115 | 23.0% |
| Grains | ~85 | 17.0% |
| Snacks | ~75 | 15.0% |
| Bakery | ~30 | 6.0% |
| Grocery | ~15 | 3.0% |

**Beverages is the dominant category**, accounting for approximately one-third of all transactions.

---

## 5. Branch Distribution

| Branch | City | Transaction Count | % Share |
|---|---|---|---|
| Branch A | Delhi | ~167 | 33.4% |
| Branch B | Bangalore | ~167 | 33.3% |
| Branch C | Mumbai | ~166 | 33.2% |

Transactions are approximately evenly distributed across branches.

---

## 6. Customer Type Split

| Customer Type | Count | % Share | Total Sales (₹) | ATV (₹) | Avg Rating |
|---|---|---|---|---|---|
| Member | 264 | 52.8% | 1,27,596.08 | 483.32 | 3.978 |
| Normal | 236 | 47.2% | 1,16,815.00 | 495.00 | 4.003 |

Member customers slightly outnumber Normal customers. Normal customers show a marginally higher ATV (₹495.00 vs ₹483.32).

---

## 7. Gender Split

| Gender | Count | % Share |
|---|---|---|
| Female | 257 | 51.4% |
| Male | 243 | 48.6% |

Gender distribution is nearly equal across all 500 transactions.

---

## 8. Payment Method Distribution

| Payment Method | Count | % Share |
|---|---|---|
| UPI | 194 | 38.8% |
| Credit Card | 158 | 31.6% |
| Cash | 148 | 29.6% |
| **Cashless Total** | **352** | **70.4%** |

UPI is the most used payment method. Combined cashless (UPI + Credit Card): 352 transactions (70.4%), consistent with India's digital payments adoption trend.

---

## 9. Monthly Transaction Volume (Actual)

| Month | Transactions | Sales (₹) | % Annual Sales |
|---|---|---|---|
| January | 41 | 21,547.00 | 8.8% |
| February | 42 | 18,938.50 | 7.8% |
| March | 42 | 22,303.08 | 9.1% |
| April | 42 | 22,495.00 | 9.2% |
| May | 42 | 19,025.50 | 7.8% |
| June | 42 | 20,397.00 | 8.3% |
| July | 42 | 21,951.00 | 9.0% |
| August | 42 | 20,354.00 | 8.3% |
| September | 42 | 18,991.00 | 7.8% |
| October | 42 | 20,208.50 | 8.3% |
| November | 42 | 20,839.00 | 8.5% |
| December | 39 | 17,361.50 | 7.1% |
| **Total** | **500** | **2,44,411.08** | **100%** |

Peak revenue month: **April 2024 (₹22,495.00)**. Lowest: **December 2024 (₹17,361.50)**. All figures from `data/supermarket_sales.csv`.

---

## 10. Correlation Observations

| Variable Pair | Observation |
|---|---|
| Sales vs Quantity | Positive correlation — higher quantity drives higher sales |
| Sales vs Unit Price | Positive correlation — premium products generate more revenue |
| Rating vs Sales | Weak relationship — high-rated products don't always have highest sales |
| Customer Type vs Rating | Member customers give slightly higher ratings on average |

---

## 11. Key EDA Takeaways

1. **Beverages dominate** — 169 transactions (33.8%), ₹1,17,511.08 (48.1% of revenue).
2. **Cheese is the top-revenue product** — ₹58,066.08 across 55 transactions, ₹185.50/unit.
3. **Branch C (Mumbai) leads** — ₹87,956.58 (36.0% of revenue, 180 transactions).
4. **UPI is the preferred payment method** — 194 transactions (38.8%); cashless total 70.4%.
5. **Customer ratings are consistently moderate-to-high** (3.5–4.8), avg 3.99/5.
6. **Normal customers have a marginally higher ATV** (₹495.00) than Members (₹483.32).
7. **April 2024 is the peak-revenue month** (₹22,495.00); December 2024 is the lowest (₹17,361.50). H1 and H2 are nearly balanced (51%/49% of revenue).
