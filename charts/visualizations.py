"""
Supermarket Sales Analysis — Visualizations
============================================
Run from project root:
    pip install -r requirements.txt
    python charts/visualizations.py

Charts saved to charts/ directory.
Verified KPIs:
  Total Sales      : Rs 244,411.08
  Transactions     : 500
  Avg Trans Value  : Rs 488.82
  Avg Rating       : 3.99/5
  Total Qty Sold   : 2,768
  Top Product      : Cheese
  Top Category     : Beverages
  Top Branch       : Branch C
  Top City         : Mumbai
  Top Payment      : UPI
"""

import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# ── Config ───────────────────────────────────────────────────────────────────
DATA_PATH  = os.path.join(os.path.dirname(__file__), "..", "data", "supermarket_sales.csv")
OUTPUT_DIR = os.path.dirname(__file__)

BLUE   = "#3b82d4"
PURPLE = "#7c5cd8"
GREEN  = "#16a34a"
ORANGE = "#ea580c"
TEAL   = "#0891b2"
BROWN  = "#b45309"
PALETTE = [BLUE, PURPLE, GREEN, ORANGE, TEAL, BROWN]

sns.set_theme(style="whitegrid", font_scale=1.05)
plt.rcParams["figure.dpi"] = 120

# ── Load ─────────────────────────────────────────────────────────────────────
df = pd.read_csv(DATA_PATH)
df["Date"]      = pd.to_datetime(df["Date"])
df["Month_Num"] = df["Date"].dt.month
df["Month"]     = df["Date"].dt.strftime("%b")

MONTH_ORDER = ["Jan","Feb","Mar","Apr","May","Jun",
               "Jul","Aug","Sep","Oct","Nov","Dec"]

def save(name):
    path = os.path.join(OUTPUT_DIR, name)
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {name}")

print("Generating charts...")

# ════════════════════════════════════════════════════════════════════════════
# 1. KPI Dashboard
# ════════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("Supermarket Sales — KPI Dashboard (2024)", fontsize=14, fontweight="bold")

kpi_labels  = ["Total Sales\n(Rs Lakh)", "Avg Trans\nValue (Rs)", "Total Qty\n(/100)", "Avg Rating\n(/5)"]
kpi_values  = [df["Sales"].sum()/100000, df["Sales"].mean(), df["Quantity"].sum()/100, df["Rating"].mean()]
kpi_display = [f"Rs {df['Sales'].sum():,.2f}", f"Rs {df['Sales'].mean():.2f}",
               f"{int(df['Quantity'].sum())} units", f"{df['Rating'].mean():.2f}/5"]

bars = axes[0].bar(kpi_labels, kpi_values, color=PALETTE[:4], edgecolor="white", linewidth=1.2)
axes[0].set_title("Core KPIs", fontsize=12)
axes[0].set_ylabel("Value (scaled)")
for bar, lbl in zip(bars, kpi_display):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height()*1.03,
                 lbl, ha="center", fontsize=8.5, fontweight="bold")

top_labels = ["Top Product", "Top Category", "Top Branch", "Top Payment"]
top_values = [
    df.groupby("Product")["Sales"].sum().idxmax(),
    df.groupby("Category")["Sales"].sum().idxmax(),
    df.groupby("Branch")["Sales"].sum().idxmax(),
    df["Payment"].value_counts().idxmax(),
]
axes[1].axis("off")
axes[1].set_title("Top Performers", fontsize=12)
for k, (lbl, val) in enumerate(zip(top_labels, top_values)):
    axes[1].text(0.05, 0.82 - k*0.20, f"{lbl}:", fontsize=11, fontweight="bold",
                 transform=axes[1].transAxes, color="#1f2328")
    axes[1].text(0.55, 0.82 - k*0.20, val, fontsize=11,
                 transform=axes[1].transAxes, color=BLUE)

plt.tight_layout()
save("01_kpi_summary.png")

# ════════════════════════════════════════════════════════════════════════════
# 2. Monthly Sales Trend
# ════════════════════════════════════════════════════════════════════════════
monthly = (df.groupby("Month_Num")["Sales"].sum()
             .reset_index().sort_values("Month_Num"))
monthly["Month"] = monthly["Month_Num"].apply(lambda x: MONTH_ORDER[x-1])

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(range(len(monthly)), monthly["Sales"], marker="o",
        color=BLUE, linewidth=2.5, markersize=7)
ax.fill_between(range(len(monthly)), monthly["Sales"], alpha=0.12, color=BLUE)
ax.set_xticks(range(len(monthly)))
ax.set_xticklabels(monthly["Month"])
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rs {x:,.0f}"))
ax.set_title("Monthly Sales Trend — 2024", fontsize=13, fontweight="bold")
ax.set_xlabel("Month"); ax.set_ylabel("Total Sales (Rs)")
plt.tight_layout()
save("02_monthly_sales_trend.png")

# ════════════════════════════════════════════════════════════════════════════
# 3. Sales by Category
# ════════════════════════════════════════════════════════════════════════════
cat_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(cat_sales.index, cat_sales.values, color=PALETTE, edgecolor="white", linewidth=1.2)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rs {x:,.0f}"))
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()*1.02,
            f"Rs {bar.get_height():,.0f}", ha="center", fontsize=8.5)
ax.set_title("Total Sales by Category — 2024", fontsize=13, fontweight="bold")
ax.set_xlabel("Category"); ax.set_ylabel("Total Sales (Rs)")
plt.tight_layout()
save("03_sales_by_category.png")

# ════════════════════════════════════════════════════════════════════════════
# 4. Top 10 Products by Sales
# ════════════════════════════════════════════════════════════════════════════
prod_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(prod_sales.index[::-1], prod_sales.values[::-1],
               color=BLUE, edgecolor="white", linewidth=1.1)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rs {x:,.0f}"))
for bar in bars:
    ax.text(bar.get_width()*1.01, bar.get_y() + bar.get_height()/2,
            f"Rs {bar.get_width():,.0f}", va="center", fontsize=8.5)
ax.set_title("Top 10 Products by Total Sales — 2024", fontsize=13, fontweight="bold")
ax.set_xlabel("Total Sales (Rs)"); ax.set_ylabel("Product")
plt.tight_layout()
save("04_top_products.png")

# ════════════════════════════════════════════════════════════════════════════
# 5. Sales by Branch
# ════════════════════════════════════════════════════════════════════════════
branch_sales = df.groupby("Branch")["Sales"].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(branch_sales.index, branch_sales.values,
              color=[BLUE, PURPLE, GREEN], edgecolor="white", linewidth=1.2)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rs {x:,.0f}"))
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()*1.02,
            f"Rs {bar.get_height():,.0f}", ha="center", fontsize=9)
ax.set_title("Total Sales by Branch — 2024", fontsize=13, fontweight="bold")
ax.set_xlabel("Branch"); ax.set_ylabel("Total Sales (Rs)")
plt.tight_layout()
save("05_sales_by_branch.png")

# ════════════════════════════════════════════════════════════════════════════
# 6. Payment Method Distribution
# ════════════════════════════════════════════════════════════════════════════
pay_counts = df["Payment"].value_counts()

fig, ax = plt.subplots(figsize=(7, 6))
wedges, texts, autotexts = ax.pie(
    pay_counts.values, labels=pay_counts.index,
    autopct="%1.1f%%", colors=[BLUE, PURPLE, GREEN],
    startangle=140, wedgeprops={"edgecolor": "white", "linewidth": 2})
for at in autotexts:
    at.set_fontsize(11); at.set_fontweight("bold")
ax.set_title("Payment Method Distribution — 2024", fontsize=13, fontweight="bold")
plt.tight_layout()
save("06_payment_distribution.png")

# ════════════════════════════════════════════════════════════════════════════
# 7. Member vs Normal Customer Comparison
# ════════════════════════════════════════════════════════════════════════════
ctype = df.groupby("Customer Type").agg(
    Transactions=("Invoice ID", "count"),
    Total_Sales=("Sales", "sum"),
    Avg_Rating=("Rating", "mean")
).reset_index()

fig, axes = plt.subplots(1, 3, figsize=(13, 5))
fig.suptitle("Member vs Normal Customer Comparison — 2024",
             fontsize=12, fontweight="bold")
cols   = ["Transactions", "Total_Sales", "Avg_Rating"]
titles = ["Transaction Count", "Total Sales (Rs)", "Avg Rating"]
fmts   = ["{:.0f}", "Rs {:,.0f}", "{:.2f}"]
for ax, col, title, fmt in zip(axes, cols, titles, fmts):
    bars = ax.bar(ctype["Customer Type"], ctype[col],
                  color=[BLUE, PURPLE], edgecolor="white", linewidth=1.2)
    ax.set_title(title, fontsize=11)
    for bar, val in zip(bars, ctype[col]):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()*1.03,
                fmt.format(val), ha="center", fontsize=9.5, fontweight="bold")
    ax.set_xlabel("")
plt.tight_layout()
save("07_customer_type_comparison.png")

# ════════════════════════════════════════════════════════════════════════════
# 8. Rating Distribution
# ════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(df["Rating"], bins=14, color=BLUE, edgecolor="white", linewidth=1.2, alpha=0.85)
ax.axvline(df["Rating"].mean(), color=ORANGE, linewidth=2, linestyle="--",
           label=f"Mean = {df['Rating'].mean():.2f}")
ax.set_title("Customer Rating Distribution — 2024", fontsize=13, fontweight="bold")
ax.set_xlabel("Rating (out of 5)"); ax.set_ylabel("Transactions")
ax.legend(fontsize=11)
plt.tight_layout()
save("08_rating_distribution.png")

# ════════════════════════════════════════════════════════════════════════════
# 9. Sales by City
# ════════════════════════════════════════════════════════════════════════════
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(city_sales.index, city_sales.values,
              color=[BLUE, PURPLE, GREEN], edgecolor="white", linewidth=1.2)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rs {x:,.0f}"))
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()*1.02,
            f"Rs {bar.get_height():,.0f}", ha="center", fontsize=9)
ax.set_title("Total Sales by City — 2024", fontsize=13, fontweight="bold")
ax.set_xlabel("City"); ax.set_ylabel("Total Sales (Rs)")
plt.tight_layout()
save("09_sales_by_city.png")

print(f"\nAll 9 charts generated in: {OUTPUT_DIR}")
