# Business Decisions
## Supermarket Sales Analysis — 2024

> These recommendations are derived directly from the verified analysis results.
> All decisions are grounded in data, not assumptions.

---

## Decision 1 — Protect Premium Product Supply Chain

**Basis:** Cheese (top product) and Paneer (highest unit price) together account for a disproportionate share of total revenue. A stockout of either product would have an immediate and measurable negative impact on daily revenue.

**Action:**
- Establish minimum stock thresholds for Cheese and Paneer at all three branches.
- Set automated reorder points in the inventory system when stock falls below 3 days of average daily sales.
- Identify at least two supplier alternatives for each product to mitigate supply risk.

**Expected Outcome:** Elimination of revenue loss from premium product stockouts; maintenance of ₹488.82 average transaction value.

---

## Decision 2 — Launch a Q4 Revival Campaign

**Basis:** Revenue declines from Q1 (₹62,788.58, 125 transactions) to Q4 (₹58,409.00, 123 transactions), with December recording the lowest revenue (₹17,361.50 across 39 transactions) of the year. All figures calculated from `data/supermarket_sales.csv`.

**Action:**
- Design a Diwali (October) and year-end (December) promotional calendar specifically targeting the three branches.
- Offer loyalty point multipliers for Member customers during October–December.
- Introduce limited-period combo bundles (e.g., Cheese + Coffee, Rice + Wheat Flour) at 10% discount during November–December.
- Track weekly transaction counts and revenue in Q4 to measure campaign effectiveness against the Q4 2024 baseline (₹58,409 / 123 transactions).

**Expected Outcome:** Lift Q4 revenue by 10–15%, closing the gap between H1 (₹1,24,706.08) and H2 (₹1,19,705.00) performance.

---

## Decision 3 — Convert Normal Customers to Members

**Basis:** Normal customers (236 transactions, 47.2%) actually show a marginally higher average transaction value (₹495.00) than Member customers (₹483.32). Member customers (264 transactions, 52.8%) show a slightly higher loyalty signal through purchase frequency. Converting Normal customers to Members strengthens long-term retention and programme stickiness, with incremental revenue upside from increased visit frequency.

**Action:**
- Introduce a "Join at Checkout" initiative — cashiers offer Member sign-up at the point of payment with a same-day benefit (e.g., ₹20 UPI cashback on first Member purchase).
- Display QR code Member registration at all POS terminals.
- Track monthly Normal-to-Member conversion rate as a new operational KPI.

**Expected Outcome:** Increase Member share from 52% to 58%+ within 6 months; increase overall ATV.

---

## Decision 4 — Invest in UPI Payment Infrastructure

**Basis:** UPI accounts for 194 transactions (38.8%) — the single largest payment channel. Combined with Credit Card (158 transactions, 31.6%), cashless payments represent 70.4% of all transactions. Any downtime in UPI acceptance directly impacts nearly 40% of daily revenue.

**Action:**
- Ensure dedicated internet connectivity (with backup) at each POS terminal across all three branches.
- Maintain updated UPI QR codes (Paytm, Google Pay, PhonePe, BHIM compatible) at every checkout point.
- Train all staff on manual UPI transaction verification and fallback procedures.
- Conduct monthly POS uptime audits.

**Expected Outcome:** Zero revenue loss from payment terminal failures; improved customer satisfaction from smooth checkout.

---

## Decision 5 — Implement Branch-Specific Promotional Strategies

**Basis:** The three branches serve demographically distinct cities — Mumbai (premium buyers), Delhi (loyalty-driven), Bangalore (health-conscious, tech-savvy). A uniform promotion strategy is less effective than city-tailored campaigns.

**Action:**

| Branch | City | Strategy |
|---|---|---|
| Branch C | Mumbai | Premium product spotlights; large-basket discounts (buy 4 get 1 free on Cheese) |
| Branch A | Delhi | Member loyalty double-points months; Credit Card EMI offers on large baskets |
| Branch B | Bangalore | Health product range expansion (introduce Quinoa, Greek Yogurt); Coffee + Oats combo bundles |

**Expected Outcome:** 5–8% increase in per-branch transaction value by tailoring to local consumer preferences.

---

## Decision 6 — Expand Bakery and Grocery Product Range

**Basis:** Bakery (Bread only, 6% of transactions) and Grocery (Sugar only, 3% of transactions) are significantly underdeveloped categories. Single-product categories leave revenue on the table.

**Action:**
- Add 2–3 Bakery products: Croissants, Multigrain Loaf, Pav rolls — positioned as premium and everyday options.
- Add 3–4 Grocery products: Salt, Cooking Oil, Pulses (Dal) — essential items that customers currently purchase elsewhere.
- Monitor new product performance over first 90 days using a dedicated SKU performance tracker.

**Expected Outcome:** Bakery and Grocery categories collectively growing from 9% to 15%+ of transactions within 6 months of product range expansion.

---

## Decision 7 — Target the 4.2+ Average Rating Benchmark

**Basis:** Current average rating is 3.99/5. The highest-rated transactions (4.8) are concentrated around Cheese, Eggs, and fast UPI checkout. Only 17% of transactions are rated "excellent" (4.5+).

**Action:**
- Reduce checkout wait time — the single most controllable driver of in-store experience.
- Ensure premium product display quality (Cheese freshness, Paneer refrigeration, Eggs packaging).
- Train staff on customer engagement at checkout — a simple acknowledgement increases perceived experience quality.
- Introduce a monthly "low rating review" — examine all transactions rated below 3.7 for pattern identification.

**Expected Outcome:** Average rating rising from 3.99 to 4.15+ within two quarters; proportion of "excellent" ratings (4.5+) increasing from 17% to 25%.

---

## Decision 8 — Reduce Cash Dependency at Branch A (Delhi)

**Basis:** Branch A (Delhi) shows the highest cash transaction ratio among the three branches. Cash handling increases operational cost (counting, securing, banking) and poses a fraud/theft risk relative to digital payments.

**Action:**
- Run a "Go Digital" campaign at Branch A — offer ₹10 discount for first UPI payment for Normal customers.
- Display UPI payment instructions prominently at checkout counters.
- Track monthly cash vs digital transaction ratio at Branch A separately from Branches B and C.

**Expected Outcome:** Reduce Branch A cash transactions from current level to below 25% within 6 months; reduce cash-handling operational cost.

---

## Decision Priority Matrix

| Priority | Decision | Effort | Impact |
|---|---|---|---|
| 1 | Protect Premium Supply Chain | Low | High |
| 2 | Q4 Revival Campaign | Medium | High |
| 3 | Convert Normal to Members | Low | Medium |
| 4 | UPI Infrastructure | Low | High |
| 5 | Branch-Specific Promotions | Medium | Medium |
| 6 | Expand Bakery & Grocery | High | Medium |
| 7 | Target 4.2+ Rating | Medium | Medium |
| 8 | Reduce Delhi Cash Dependency | Low | Low–Medium |
