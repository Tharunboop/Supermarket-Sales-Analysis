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

| Customer Type | Count | % Share |
|---|---|---|
| Member | ~260 | 52% |
| Normal | ~240 | 48% |

Member customers slightly outnumber Normal customers.

---

## 7. Gender Split

| Gender | Count | % Share |
|---|---|---|
| Female | ~255 | 51% |
| Male | ~245 | 49% |

Gender distribution is nearly equal across all 500 transactions.

---

## 8. Payment Method Distribution

| Payment Method | Count | % Share |
|---|---|---|
| UPI | ~190 | 38% |
| Cash | ~165 | 33% |
| Credit Card | ~145 | 29% |

UPI is the most used payment method, consistent with India's digital payments adoption trend.

---

## 9. Monthly Transaction Volume

| Month | Transaction Count |
|---|---|
| January | 50 |
| February | 46 |
| March | 46 |
| April | 44 |
| May | 44 |
| June | 42 |
| July | 42 |
| August | 42 |
| September | 40 |
| October | 38 |
| November | 38 |
| December | 28 |

Note: Transaction count is slightly front-loaded (Jan–Mar) with a dip in Q4.

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

1. **Beverages dominate** both in transaction count and revenue contribution.
2. **Cheese is the top-selling product** appearing in the most transactions.
3. **Branch C (Mumbai) leads** in transaction volume among the three branches.
4. **UPI is the preferred payment method**, used in ~38% of transactions.
5. **Customer ratings are consistently moderate-to-high** (3.5–4.8), indicating general satisfaction.
6. **Member customers generate marginally more revenue** than Normal customers.
7. **Sales peak in H1 (Jan–Jun)** and taper slightly in H2.
