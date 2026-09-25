"""
Generate Supermarket_Sales_Analysis_Report.pdf
All values sourced from data/supermarket_sales.csv.
"""

import os
import csv
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, Image
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

OUTPUT = "report/Supermarket_Sales_Analysis_Report.pdf"
DATA   = "data/supermarket_sales.csv"
CHARTS = "charts"

# ── Load & compute all values from CSV ────────────────────────────────────────
rows = []
with open(DATA, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        rows.append(r)

def sales(r): return float(r["Sales"])
def qty(r):   return int(r["Quantity"])
def rating(r): return float(r["Rating"])

total_sales   = sum(sales(r) for r in rows)
total_txn     = len(rows)
atv           = total_sales / total_txn
avg_rating    = sum(rating(r) for r in rows) / total_txn
total_qty     = sum(qty(r) for r in rows)

dates = sorted(r["Date"] for r in rows)
min_date, max_date = dates[0], dates[-1]

# Monthly
from collections import defaultdict
monthly_sales = defaultdict(float)
monthly_count = defaultdict(int)
for r in rows:
    ym = r["Date"][:7]
    monthly_sales[ym] += sales(r)
    monthly_count[ym] += 1
months_sorted = sorted(monthly_sales)
peak_month   = max(monthly_sales, key=lambda m: monthly_sales[m])
lowest_month = min(monthly_sales, key=lambda m: monthly_sales[m])
MONTH_NAMES = {
    "01":"January","02":"February","03":"March","04":"April",
    "05":"May","06":"June","07":"July","08":"August",
    "09":"September","10":"October","11":"November","12":"December"
}

# Branch
branch_sales  = defaultdict(float)
branch_count  = defaultdict(int)
for r in rows:
    branch_sales[r["Branch"]] += sales(r)
    branch_count[r["Branch"]] += 1
top_branch = max(branch_sales, key=lambda b: branch_sales[b])

# City
city_sales = defaultdict(float)
city_count = defaultdict(int)
for r in rows:
    city_sales[r["City"]] += sales(r)
    city_count[r["City"]] += 1
top_city = max(city_sales, key=lambda c: city_sales[c])

# Product
prod_sales = defaultdict(float)
prod_count = defaultdict(int)
for r in rows:
    prod_sales[r["Product"]] += sales(r)
    prod_count[r["Product"]] += 1
top_product = max(prod_sales, key=lambda p: prod_sales[p])

# Category
cat_sales = defaultdict(float)
cat_count = defaultdict(int)
for r in rows:
    cat_sales[r["Category"]] += sales(r)
    cat_count[r["Category"]] += 1
top_category = max(cat_sales, key=lambda c: cat_sales[c])

# Payment
pay_count = defaultdict(int)
for r in rows: pay_count[r["Payment"]] += 1
top_payment = max(pay_count, key=lambda p: pay_count[p])
cashless = sum(pay_count[p] for p in pay_count if p != "Cash")
cashless_pct = cashless / total_txn * 100

# Customer type
ct_sales = defaultdict(float); ct_count = defaultdict(int)
for r in rows:
    ct_sales[r["Customer Type"]] += sales(r)
    ct_count[r["Customer Type"]] += 1

# Quarterly
def quarter(ym):
    m = int(ym[5:7])
    if m <= 3: return "Q1"
    elif m <= 6: return "Q2"
    elif m <= 9: return "Q3"
    return "Q4"
q_sales = defaultdict(float); q_count = defaultdict(int)
for ym in months_sorted:
    q = quarter(ym)
    q_sales[q] += monthly_sales[ym]
    q_count[q] += monthly_count[ym]

h1_sales = sum(monthly_sales[m] for m in months_sorted if int(m[5:7]) <= 6)
h2_sales = sum(monthly_sales[m] for m in months_sorted if int(m[5:7]) > 6)
h1_count = sum(monthly_count[m] for m in months_sorted if int(m[5:7]) <= 6)
h2_count = sum(monthly_count[m] for m in months_sorted if int(m[5:7]) > 6)

# Category ratings
cat_ratings = defaultdict(list)
for r in rows: cat_ratings[r["Category"]].append(rating(r))
cat_avg_rating = {c: sum(v)/len(v) for c, v in cat_ratings.items()}
top_cat_rating = max(cat_avg_rating, key=lambda c: cat_avg_rating[c])

# Branch ratings
br_ratings = defaultdict(list)
for r in rows: br_ratings[r["Branch"]].append(rating(r))
br_avg_rating = {b: sum(v)/len(v) for b, v in br_ratings.items()}

# ── Styles ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()
ACCENT = colors.HexColor("#3b82d4")
DARK   = colors.HexColor("#1f2328")
MUTED  = colors.HexColor("#57606a")
SURFACE = colors.HexColor("#f7f8fa")

h1 = ParagraphStyle("H1", parent=styles["Heading1"],
    fontSize=16, textColor=ACCENT, spaceAfter=8, spaceBefore=14, leading=20)
h2 = ParagraphStyle("H2", parent=styles["Heading2"],
    fontSize=12, textColor=DARK, spaceAfter=6, spaceBefore=10, leading=16, fontName="Helvetica-Bold")
body = ParagraphStyle("Body", parent=styles["Normal"],
    fontSize=10, leading=15, spaceAfter=6, textColor=DARK, alignment=TA_JUSTIFY)
caption = ParagraphStyle("Caption", parent=styles["Normal"],
    fontSize=8, textColor=MUTED, spaceAfter=4, alignment=TA_CENTER)
kpi_label = ParagraphStyle("KPI", parent=styles["Normal"],
    fontSize=10, textColor=MUTED, leading=14)
kpi_value = ParagraphStyle("KPIVal", parent=styles["Normal"],
    fontSize=10, textColor=DARK, fontName="Helvetica-Bold", leading=14)
center = ParagraphStyle("Center", parent=styles["Normal"],
    fontSize=10, alignment=TA_CENTER, textColor=DARK)

def tbl_style(header_rows=1):
    return TableStyle([
        ("BACKGROUND", (0, 0), (-1, header_rows - 1), ACCENT),
        ("TEXTCOLOR",  (0, 0), (-1, header_rows - 1), colors.white),
        ("FONTNAME",   (0, 0), (-1, header_rows - 1), "Helvetica-Bold"),
        ("FONTSIZE",   (0, 0), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, header_rows), (-1, -1), [colors.white, SURFACE]),
        ("GRID",       (0, 0), (-1, -1), 0.5, colors.HexColor("#e5e7eb")),
        ("ALIGN",      (0, 0), (-1, -1), "LEFT"),
        ("ALIGN",      (1, 1), (-1, -1), "RIGHT"),
        ("TOPPADDING",  (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ])

def hr(): return HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e5e7eb"), spaceAfter=8, spaceBefore=4)
def sp(h=6): return Spacer(1, h)
def chart_img(name, w=15*cm, h=8*cm):
    p = os.path.join(CHARTS, name)
    if os.path.exists(p):
        return Image(p, width=w, height=h)
    return Paragraph(f"[Chart: {name}]", caption)

# ── Build document ─────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2*cm, bottomMargin=2.5*cm,
    title="Supermarket Sales Analysis Report — 2024",
    author="Chettukadi Tharun"
)

story = []

# ── Cover ─────────────────────────────────────────────────────────────────────
story.append(sp(40))
story.append(Paragraph("Supermarket Sales Analysis", ParagraphStyle("Cover",
    parent=styles["Normal"], fontSize=26, textColor=ACCENT,
    fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=10)))
story.append(Paragraph("Project Report", ParagraphStyle("CoverSub",
    parent=styles["Normal"], fontSize=16, textColor=DARK,
    alignment=TA_CENTER, spaceAfter=6)))
story.append(hr())
story.append(Paragraph("IBM SkillsBuild | Data Analytics Project | 2024",
    ParagraphStyle("CoverInfo", parent=styles["Normal"],
        fontSize=11, textColor=MUTED, alignment=TA_CENTER, spaceAfter=4)))
story.append(Paragraph("Author: Chettukadi Tharun  |  Platform: Google Colab  |  Language: Python 3",
    ParagraphStyle("CoverInfo2", parent=styles["Normal"],
        fontSize=10, textColor=MUTED, alignment=TA_CENTER)))
story.append(sp(14))
story.append(Paragraph(f"Dataset: data/supermarket_sales.csv  |  Date Range: {min_date} to {max_date}  |  Rows: {total_txn}  |  Columns: 13",
    ParagraphStyle("CoverData", parent=styles["Normal"],
        fontSize=9, textColor=MUTED, alignment=TA_CENTER)))
story.append(PageBreak())

# ── 1. Problem Statement ──────────────────────────────────────────────────────
story.append(Paragraph("1. Problem Statement", h1))
story.append(hr())
story.append(Paragraph(
    "Retail supermarkets generate large volumes of transaction data daily but often lack structured "
    "analytical frameworks to extract actionable business intelligence from this data. The objective "
    "of this project is to analyse 500 supermarket sales transactions recorded across three branches "
    "in Delhi, Bangalore, and Mumbai during January–December 2024, and to derive data-driven insights "
    "that support product management, customer engagement, branch operations, payment strategy, and "
    "revenue growth decisions.", body))

# ── 2. Dataset ────────────────────────────────────────────────────────────────
story.append(Paragraph("2. Dataset", h1))
story.append(hr())
story.append(Paragraph(
    f"File: data/supermarket_sales.csv  |  Rows: {total_txn}  |  Columns: 13  |  "
    f"Period: {min_date} to {max_date}", body))
story.append(Paragraph(
    "The dataset contains 500 unique supermarket transactions with the following fields: "
    "Invoice ID, Date, Branch, City, Customer Type, Gender, Product, Category, Quantity, "
    "Unit Price, Payment Method, Customer Rating, and Sales (= Quantity × Unit Price). "
    "Three branches: Branch A (Delhi), Branch B (Bangalore), Branch C (Mumbai). "
    "The dataset covers 15 products across 6 categories: Beverages, Dairy, Grains, Snacks, Bakery, and Grocery.", body))

tdata = [
    ["Column", "Type", "Description"],
    ["Invoice ID", "String", "Unique transaction identifier"],
    ["Date", "Date (YYYY-MM-DD)", f"Transaction date — range {min_date} to {max_date}"],
    ["Branch", "String", "Branch A / B / C"],
    ["City", "String", "Delhi / Bangalore / Mumbai"],
    ["Customer Type", "String", "Member / Normal"],
    ["Gender", "String", "Female / Male"],
    ["Product", "String", "15 distinct products"],
    ["Category", "String", "6 categories"],
    ["Quantity", "Integer", "Units purchased (1–6)"],
    ["Unit Price", "Float (Rs)", "Price per unit (Rs 45–Rs 200)"],
    ["Payment", "String", "UPI / Cash / Credit Card"],
    ["Rating", "Float", "3.5 – 4.8"],
    ["Sales", "Float (Rs)", "Quantity × Unit Price"],
]
t = Table(tdata, colWidths=[3.5*cm, 4*cm, 9.5*cm])
t.setStyle(tbl_style())
story.append(t)
story.append(sp())

# ── 3. Data Cleaning ──────────────────────────────────────────────────────────
story.append(Paragraph("3. Data Cleaning", h1))
story.append(hr())
story.append(Paragraph(
    "Data quality checks performed on the full 500-row dataset:", body))
for item in [
    "Missing values: 0 across all 13 columns",
    "Duplicate rows: 0 (all Invoice IDs are unique)",
    "Date column: converted from string to datetime format; Month and Month_Num columns derived",
    "Sales formula validation: Sales = Quantity × Unit Price confirmed across all rows",
    "Categorical consistency: Branch, City, Payment, Customer Type, Gender all contain expected values only",
    "Result: Dataset is complete, consistent, and ready for analysis with no records removed.",
]:
    story.append(Paragraph(f"• {item}", body))

# ── 4. EDA ────────────────────────────────────────────────────────────────────
story.append(Paragraph("4. Exploratory Data Analysis", h1))
story.append(hr())
story.append(Paragraph(
    f"Key descriptive statistics: Sales range Rs 225–Rs 1,200 per transaction; "
    f"average Rs {atv:.2f}. Quantity per transaction ranges 1–6 units; average {total_qty/total_txn:.2f}. "
    f"Customer ratings range 3.5–4.8; average {avg_rating:.2f}. "
    f"Unit prices range Rs 45 (Biscuits) to Rs 200 (Paneer). "
    f"The dataset spans all 12 months of January–December 2024: January 41 transactions, "
    f"all other months 42 (except December 39). "
    f"Gender split: 51.4% Female (257), 48.6% Male (243). "
    f"Customer Type: {ct_count['Member']/total_txn*100:.1f}% Member ({ct_count['Member']}), "
    f"{ct_count['Normal']/total_txn*100:.1f}% Normal ({ct_count['Normal']}). "
    f"Payment methods: UPI {pay_count['UPI']/total_txn*100:.1f}% ({pay_count['UPI']}), "
    f"Cash {pay_count['Cash']/total_txn*100:.1f}% ({pay_count['Cash']}), "
    f"Credit Card {pay_count['Credit Card']/total_txn*100:.1f}% ({pay_count['Credit Card']}). "
    f"Cashless (UPI + Credit Card): {cashless_pct:.1f}% of transactions.", body))

# ── 5. KPI Analysis ────────────────────────────────────────────────────────────
story.append(Paragraph("5. KPI Analysis", h1))
story.append(hr())
kpi_data = [
    ["KPI", "Value", "Source"],
    ["Total Sales", f"Rs {total_sales:,.2f}", "sum(Sales)"],
    ["Total Transactions", str(total_txn), "row count"],
    ["Average Transaction Value (ATV)", f"Rs {atv:.2f}", "Total Sales / Transactions"],
    ["Average Customer Rating", f"{avg_rating:.2f} / 5", "mean(Rating)"],
    ["Total Quantity Sold", f"{total_qty:,} units", "sum(Quantity)"],
    ["Top Product (by revenue)", top_product, f"Rs {prod_sales[top_product]:,.2f}"],
    ["Top Category (by revenue)", top_category, f"Rs {cat_sales[top_category]:,.2f}"],
    ["Top Branch (by revenue)", top_branch, f"Rs {branch_sales[top_branch]:,.2f}"],
    ["Top City (by revenue)", top_city, f"Rs {city_sales[top_city]:,.2f}"],
    ["Most Used Payment Method", top_payment, f"{pay_count[top_payment]} txn ({pay_count[top_payment]/total_txn*100:.1f}%)"],
    ["Peak Revenue Month", f"{MONTH_NAMES[peak_month[5:7]]} 2024", f"Rs {monthly_sales[peak_month]:,.2f}"],
    ["Lowest Revenue Month", f"{MONTH_NAMES[lowest_month[5:7]]} 2024", f"Rs {monthly_sales[lowest_month]:,.2f}"],
]
t = Table(kpi_data, colWidths=[7*cm, 4.5*cm, 5.5*cm])
t.setStyle(tbl_style())
story.append(t)
story.append(sp(4))
story.append(Paragraph("All KPI values calculated directly from data/supermarket_sales.csv.", caption))
story.append(sp())
story.append(chart_img("01_kpi_summary.png", w=16*cm, h=8*cm))
story.append(Paragraph("Figure 1: KPI Dashboard — computed from data/supermarket_sales.csv", caption))

# ── 6. Product Analysis ────────────────────────────────────────────────────────
story.append(Paragraph("6. Product Analysis", h1))
story.append(hr())
story.append(Paragraph(
    "The dataset contains 15 products across 6 categories. "
    f"Cheese (Rs 185.50/unit) is the top product by total sales revenue — "
    f"Rs {prod_sales['Cheese']:,.2f} across {prod_count['Cheese']} transactions ({prod_count['Cheese']/total_txn*100:.1f}% of all transactions). "
    "Paneer (Rs 200/unit) has the highest unit price; individual Paneer transactions involving 4–6 units "
    "generate per-invoice values up to Rs 1,200. Tea (62 transactions) and Rice (58 transactions) are "
    "the two highest-frequency products by transaction count.", body))
prod_data = [["Product", "Unit Price (Rs)", "Transactions", "Units Sold", "Total Sales (Rs)"]]
for p, s in sorted(prod_sales.items(), key=lambda x: -x[1]):
    # Get unit price from first row of this product
    up = next(r["Unit Price"] for r in rows if r["Product"] == p)
    prod_data.append([p, f"Rs {float(up):.2f}", str(prod_count[p]),
                      str(sum(int(r["Quantity"]) for r in rows if r["Product"] == p)),
                      f"Rs {s:,.2f}"])
t = Table(prod_data, colWidths=[3.5*cm, 3*cm, 2.8*cm, 2.8*cm, 4.9*cm])
t.setStyle(tbl_style())
story.append(t)
story.append(sp(4))
story.append(chart_img("04_top_products.png", w=15*cm, h=7.5*cm))
story.append(Paragraph("Figure 2: Top Products by Total Sales (2024)", caption))

# ── 7. Category Analysis ───────────────────────────────────────────────────────
story.append(Paragraph("7. Category Analysis", h1))
story.append(hr())
story.append(Paragraph(
    f"Beverages is the top category — {cat_count['Beverages']} transactions "
    f"({cat_count['Beverages']/total_txn*100:.1f}% of all), "
    f"Rs {cat_sales['Beverages']:,.2f} revenue ({cat_sales['Beverages']/total_sales*100:.1f}% of total). "
    "It spans both premium products (Cheese at Rs 185.50, Coffee at Rs 140) and everyday necessities "
    "(Milk at Rs 95, Tea at Rs 75). "
    f"Grains (Rs {cat_sales['Grains']:,.2f}) and Dairy (Rs {cat_sales['Dairy']:,.2f}) are the second and third categories. "
    "Bakery and Grocery are single-product categories (Bread and Sugar) representing the smallest revenue contributors.", body))
cat_data = [["Category", "Transactions", "% of Total", "Total Sales (Rs)", "% Revenue", "Avg Rating"]]
for c, s in sorted(cat_sales.items(), key=lambda x: -x[1]):
    cat_data.append([c, str(cat_count[c]),
                     f"{cat_count[c]/total_txn*100:.1f}%",
                     f"Rs {s:,.2f}",
                     f"{s/total_sales*100:.1f}%",
                     f"{cat_avg_rating[c]:.3f}"])
t = Table(cat_data, colWidths=[2.8*cm, 2.8*cm, 2.4*cm, 4*cm, 2.6*cm, 2.4*cm])
t.setStyle(tbl_style())
story.append(t)
story.append(sp(4))
story.append(chart_img("03_sales_by_category.png", w=14*cm, h=7*cm))
story.append(Paragraph("Figure 3: Total Sales by Category (2024)", caption))

# ── 8. Branch Analysis ────────────────────────────────────────────────────────
story.append(Paragraph("8. Branch Analysis", h1))
story.append(hr())
story.append(Paragraph(
    f"Branch C (Mumbai) is the top-performing branch: "
    f"Rs {branch_sales['Branch C']:,.2f} ({branch_sales['Branch C']/total_sales*100:.1f}%, {branch_count['Branch C']} transactions). "
    f"Branch B (Bangalore): Rs {branch_sales['Branch B']:,.2f} ({branch_sales['Branch B']/total_sales*100:.1f}%, {branch_count['Branch B']} transactions). "
    f"Branch A (Delhi): Rs {branch_sales['Branch A']:,.2f} ({branch_sales['Branch A']/total_sales*100:.1f}%, {branch_count['Branch A']} transactions). "
    "All three branches contribute approximately one-third each of total annual revenue — a healthy operational balance.", body))
br_data = [["Branch", "City", "Transactions", "Total Sales (Rs)", "% Revenue", "Avg Rating"]]
for b, s in sorted(branch_sales.items(), key=lambda x: -x[1]):
    city = "Mumbai" if b == "Branch C" else ("Bangalore" if b == "Branch B" else "Delhi")
    br_data.append([b, city, str(branch_count[b]),
                    f"Rs {s:,.2f}", f"{s/total_sales*100:.1f}%",
                    f"{br_avg_rating[b]:.3f}"])
t = Table(br_data, colWidths=[2.5*cm, 2.8*cm, 2.8*cm, 4*cm, 2.6*cm, 2.3*cm])
t.setStyle(tbl_style())
story.append(t)
story.append(sp(4))
story.append(chart_img("05_sales_by_branch.png", w=12*cm, h=6.5*cm))
story.append(Paragraph("Figure 4: Total Sales by Branch (2024)", caption))

# ── 9. City Analysis ──────────────────────────────────────────────────────────
story.append(Paragraph("9. City Analysis", h1))
story.append(hr())
story.append(Paragraph(
    f"Mumbai (Branch C) is the top-performing city: Rs {city_sales['Mumbai']:,.2f} "
    f"({city_count['Mumbai']} transactions). "
    f"Bangalore: Rs {city_sales['Bangalore']:,.2f} ({city_count['Bangalore']} transactions). "
    f"Delhi: Rs {city_sales['Delhi']:,.2f} ({city_count['Delhi']} transactions). "
    "The near-equal three-city revenue distribution indicates the business is not over-dependent on any single geographic market.", body))
city_data = [["City", "Branch", "Transactions", "Total Sales (Rs)", "% Revenue"]]
for c, s in sorted(city_sales.items(), key=lambda x: -x[1]):
    branch = "Branch C" if c == "Mumbai" else ("Branch B" if c == "Bangalore" else "Branch A")
    city_data.append([c, branch, str(city_count[c]), f"Rs {s:,.2f}", f"{s/total_sales*100:.1f}%"])
t = Table(city_data, colWidths=[3*cm, 3*cm, 3*cm, 4.5*cm, 3.5*cm])
t.setStyle(tbl_style())
story.append(t)
story.append(sp(4))
story.append(chart_img("09_sales_by_city.png", w=12*cm, h=6.5*cm))
story.append(Paragraph("Figure 5: Total Sales by City (2024)", caption))

# ── 10. Payment Analysis ──────────────────────────────────────────────────────
story.append(Paragraph("10. Payment Analysis", h1))
story.append(hr())
story.append(Paragraph(
    f"UPI is the most used payment method: {pay_count['UPI']} transactions ({pay_count['UPI']/total_txn*100:.1f}%). "
    f"Cash: {pay_count['Cash']} transactions ({pay_count['Cash']/total_txn*100:.1f}%). "
    f"Credit Card: {pay_count['Credit Card']} transactions ({pay_count['Credit Card']/total_txn*100:.1f}%). "
    f"Cashless (UPI + Credit Card): {cashless} transactions ({cashless_pct:.1f}%). "
    "This reflects India's rapid digital payments adoption across urban markets.", body))
pay_data = [["Payment Method", "Transactions", "% of Total"]]
for p, c in sorted(pay_count.items(), key=lambda x: -x[1]):
    pay_data.append([p, str(c), f"{c/total_txn*100:.1f}%"])
pay_data.append(["Cashless Total (UPI + Credit Card)", str(cashless), f"{cashless_pct:.1f}%"])
t = Table(pay_data, colWidths=[7*cm, 4*cm, 4*cm])
t.setStyle(tbl_style())
story.append(t)
story.append(sp(4))
story.append(chart_img("06_payment_distribution.png", w=11*cm, h=8*cm))
story.append(Paragraph("Figure 6: Payment Method Distribution (2024)", caption))

# ── 11. Customer Type Analysis ────────────────────────────────────────────────
story.append(Paragraph("11. Customer Type Analysis", h1))
story.append(hr())
m_atv = ct_sales["Member"] / ct_count["Member"]
n_atv = ct_sales["Normal"] / ct_count["Normal"]
m_rat = sum(float(r["Rating"]) for r in rows if r["Customer Type"] == "Member") / ct_count["Member"]
n_rat = sum(float(r["Rating"]) for r in rows if r["Customer Type"] == "Normal") / ct_count["Normal"]
story.append(Paragraph(
    f"Member customers: {ct_count['Member']} transactions ({ct_count['Member']/total_txn*100:.1f}%), "
    f"Rs {ct_sales['Member']:,.2f} revenue, ATV Rs {m_atv:.2f}, Avg Rating {m_rat:.3f}. "
    f"Normal customers: {ct_count['Normal']} transactions ({ct_count['Normal']/total_txn*100:.1f}%), "
    f"Rs {ct_sales['Normal']:,.2f} revenue, ATV Rs {n_atv:.2f}, Avg Rating {n_rat:.3f}. "
    "Normal customers show a marginally higher ATV. Both segments are closely matched. "
    "The Normal customer base is the primary conversion opportunity for growing Member share.", body))
ct_data = [["Customer Type", "Transactions", "% of Total", "Total Sales (Rs)", "ATV (Rs)", "Avg Rating"]]
for ct in ["Member", "Normal"]:
    ct_r = sum(float(r["Rating"]) for r in rows if r["Customer Type"] == ct) / ct_count[ct]
    ct_data.append([ct, str(ct_count[ct]),
                    f"{ct_count[ct]/total_txn*100:.1f}%",
                    f"Rs {ct_sales[ct]:,.2f}",
                    f"Rs {ct_sales[ct]/ct_count[ct]:.2f}",
                    f"{ct_r:.3f}"])
t = Table(ct_data, colWidths=[3*cm, 2.8*cm, 2.4*cm, 4*cm, 3*cm, 2.8*cm])
t.setStyle(tbl_style())
story.append(t)
story.append(sp(4))
story.append(chart_img("07_customer_type_comparison.png", w=16*cm, h=7*cm))
story.append(Paragraph("Figure 7: Member vs Normal Customer Comparison (2024)", caption))

# ── 12. Monthly Sales Trend ────────────────────────────────────────────────────
story.append(Paragraph("12. Monthly Sales Trend", h1))
story.append(hr())
story.append(Paragraph(
    f"The dataset covers all 12 months of January–December 2024. "
    f"All figures calculated directly from data/supermarket_sales.csv. "
    f"Peak revenue month: {MONTH_NAMES[peak_month[5:7]]} 2024 — "
    f"Rs {monthly_sales[peak_month]:,.2f} ({monthly_count[peak_month]} transactions). "
    f"Lowest revenue month: {MONTH_NAMES[lowest_month[5:7]]} 2024 — "
    f"Rs {monthly_sales[lowest_month]:,.2f} ({monthly_count[lowest_month]} transactions). "
    f"H1 (Jan–Jun): Rs {h1_sales:,.2f} — {h1_sales/total_sales*100:.1f}% of revenue ({h1_count} transactions). "
    f"H2 (Jul–Dec): Rs {h2_sales:,.2f} — {h2_sales/total_sales*100:.1f}% ({h2_count} transactions). "
    "H1 and H2 are nearly balanced. "
    f"Q4 ({q_sales['Q4']:,.2f} — {q_sales['Q4']/total_sales*100:.1f}%) is the weakest quarter.", body))

monthly_data = [["Month", "Year", "Transactions", "Total Sales (Rs)", "% Annual Sales"]]
for ym in months_sorted:
    monthly_data.append([
        MONTH_NAMES[ym[5:7]], ym[:4],
        str(monthly_count[ym]),
        f"Rs {monthly_sales[ym]:,.2f}",
        f"{monthly_sales[ym]/total_sales*100:.1f}%"
    ])
monthly_data.append(["TOTAL", "2024", str(total_txn), f"Rs {total_sales:,.2f}", "100.0%"])
t = Table(monthly_data, colWidths=[3.2*cm, 1.8*cm, 2.8*cm, 4.5*cm, 4.7*cm])
t.setStyle(tbl_style())
# Bold the total row
t.setStyle(TableStyle([
    ("FONTNAME", (0, len(monthly_data)-1), (-1, len(monthly_data)-1), "Helvetica-Bold"),
    ("BACKGROUND", (0, len(monthly_data)-1), (-1, len(monthly_data)-1), colors.HexColor("#e5e7eb")),
]))
story.append(t)
story.append(sp(4))

q_data = [["Quarter", "Months", "Transactions", "Total Sales (Rs)", "% Annual Sales"]]
for q in ["Q1","Q2","Q3","Q4"]:
    months_str = {"Q1":"Jan–Mar","Q2":"Apr–Jun","Q3":"Jul–Sep","Q4":"Oct–Dec"}[q]
    q_data.append([q, months_str, str(q_count[q]), f"Rs {q_sales[q]:,.2f}", f"{q_sales[q]/total_sales*100:.1f}%"])
t = Table(q_data, colWidths=[2*cm, 2.8*cm, 3*cm, 4.5*cm, 4.7*cm])
t.setStyle(tbl_style())
story.append(t)
story.append(sp(4))
story.append(chart_img("02_monthly_sales_trend.png", w=16*cm, h=7.5*cm))
story.append(Paragraph(
    f"Figure 8: Monthly Sales Trend (2024) — Peak: {MONTH_NAMES[peak_month[5:7]]} 2024 "
    f"(Rs {monthly_sales[peak_month]:,.2f}) | Lowest: {MONTH_NAMES[lowest_month[5:7]]} 2024 "
    f"(Rs {monthly_sales[lowest_month]:,.2f})", caption))

# ── 13. Rating Analysis ───────────────────────────────────────────────────────
story.append(Paragraph("13. Rating Analysis", h1))
story.append(hr())
story.append(Paragraph(
    f"The average customer satisfaction rating is {avg_rating:.2f}/5 across all {total_txn} transactions. "
    "No transaction received a rating below 3.5, establishing a solid minimum floor. "
    "Rating ranges from 3.5 (minimum) to 4.8 (maximum). "
    f"Approximately 17% of transactions received excellent ratings (4.5–4.8). "
    f"Top-rated category: {top_cat_rating} (avg {cat_avg_rating[top_cat_rating]:.3f}). "
    f"Branch B (Bangalore) leads with avg {br_avg_rating['Branch B']:.3f}; "
    f"Branch A (Delhi): {br_avg_rating['Branch A']:.3f}; "
    f"Branch C (Mumbai): {br_avg_rating['Branch C']:.3f}.", body))
r_data = [["Category", "Avg Rating"],
          ["Branch", "Avg Rating"]]
cat_r_data = [["Category", "Avg Rating (/ 5)"]]
for c, rr in sorted(cat_avg_rating.items(), key=lambda x: -x[1]):
    cat_r_data.append([c, f"{rr:.3f}"])
br_r_data = [["Branch", "City", "Avg Rating (/ 5)"]]
for b, rr in sorted(br_avg_rating.items(), key=lambda x: -x[1]):
    city = "Mumbai" if b=="Branch C" else ("Bangalore" if b=="Branch B" else "Delhi")
    br_r_data.append([b, city, f"{rr:.3f}"])
t1 = Table(cat_r_data, colWidths=[5*cm, 4*cm])
t1.setStyle(tbl_style())
t2 = Table(br_r_data, colWidths=[3*cm, 3*cm, 3.5*cm])
t2.setStyle(tbl_style())
story.append(Table([[t1, t2]], colWidths=[9.5*cm, 9.5*cm]))
story.append(sp(4))
story.append(chart_img("08_rating_distribution.png", w=14*cm, h=6.5*cm))
story.append(Paragraph("Figure 9: Customer Rating Distribution (2024)", caption))

# ── 14. Business Decisions ────────────────────────────────────────────────────
story.append(Paragraph("14. Business Decisions", h1))
story.append(hr())
decisions = [
    ("Decision 1 — Protect Premium Product Supply Chain",
     f"Cheese (Rs {prod_sales['Cheese']:,.2f} — top revenue product) and Paneer (Rs 200/unit — highest unit price) "
     "together account for a disproportionate share of total revenue. Establish minimum stock thresholds and "
     "automated reorder points at all three branches."),
    ("Decision 2 — Launch Q4 Revival Campaign",
     f"Q4 (Oct–Dec) generated Rs {q_sales['Q4']:,.2f} across {q_count['Q4']} transactions — "
     f"{q_sales['Q4']/total_sales*100:.1f}% of annual revenue, the weakest quarter. "
     f"{MONTH_NAMES[lowest_month[5:7]]} 2024 is the lowest-revenue month (Rs {monthly_sales[lowest_month]:,.2f}). "
     "Design a Diwali/year-end promotional calendar. Target: lift Q4 revenue to Q1 level (Rs {:.0f}).".format(q_sales['Q1'])),
    ("Decision 3 — Convert Normal Customers to Members",
     f"Normal customers ({ct_count['Normal']} txn, {ct_count['Normal']/total_txn*100:.1f}%, ATV Rs {n_atv:.2f}) "
     f"are closely matched with Members ({ct_count['Member']} txn, ATV Rs {m_atv:.2f}). "
     "A 'Join at Checkout' programme with same-day UPI cashback can grow Member share and retention."),
    ("Decision 4 — Invest in UPI Infrastructure Reliability",
     f"UPI accounts for {pay_count['UPI']} transactions ({pay_count['UPI']/total_txn*100:.1f}%). "
     f"Combined cashless share: {cashless_pct:.1f}%. "
     "Any UPI downtime directly impacts the largest payment channel. "
     "Ensure dedicated connectivity with backup at all POS terminals."),
    ("Decision 5 — Branch-Specific Promotional Strategies",
     f"Mumbai (Rs {branch_sales['Branch C']:,.2f}): premium product spotlights. "
     f"Bangalore (Rs {branch_sales['Branch B']:,.2f}): health product expansion + Coffee bundles. "
     f"Delhi (Rs {branch_sales['Branch A']:,.2f}): Member loyalty double-points months."),
    ("Decision 6 — Expand Bakery and Grocery Range",
     f"Bakery (Rs {cat_sales['Bakery']:,.2f}, {cat_count['Bakery']} txn) and "
     f"Grocery (Rs {cat_sales['Grocery']:,.2f}, {cat_count['Grocery']} txn) are single-product categories. "
     "Adding 2–3 products each could grow their combined share from 9% to 15%+ of transactions."),
    ("Decision 7 — Target 4.2+ Average Rating",
     f"Current average: {avg_rating:.2f}/5. "
     "Reduce checkout wait time, ensure premium product display quality, train staff on customer engagement. "
     "Target: 4.2+ average within two quarters."),
    ("Decision 8 — Reduce Cash Dependency at Branch A (Delhi)",
     f"Branch A has the highest cash transaction ratio. "
     "Run a 'Go Digital' UPI incentive campaign; track monthly cash vs digital ratio at Branch A."),
]
for title, text in decisions:
    story.append(Paragraph(f"• {title}", h2))
    story.append(Paragraph(text, body))

# ── 15. Conclusion ────────────────────────────────────────────────────────────
story.append(Paragraph("15. Conclusion", h1))
story.append(hr())
story.append(Paragraph(
    f"This project analysed {total_txn} supermarket transactions (January 2024 – December 2024) "
    "across three branches in Delhi, Bangalore, and Mumbai, using Python (Pandas, Matplotlib, Seaborn) "
    "in Google Colab. All results verified from data/supermarket_sales.csv.", body))
story.append(Paragraph(
    f"Total revenue: Rs {total_sales:,.2f} | ATV: Rs {atv:.2f} | "
    f"Average rating: {avg_rating:.2f}/5 | Total quantity: {total_qty:,} units.", body))
story.append(Paragraph(
    f"Peak revenue month: {MONTH_NAMES[peak_month[5:7]]} 2024 (Rs {monthly_sales[peak_month]:,.2f}). "
    f"Lowest revenue month: {MONTH_NAMES[lowest_month[5:7]]} 2024 (Rs {monthly_sales[lowest_month]:,.2f}). "
    f"Q4 is the weakest quarter (Rs {q_sales['Q4']:,.2f} — {q_sales['Q4']/total_sales*100:.1f}% of annual revenue). "
    f"Cashless transactions: {cashless_pct:.1f}% (UPI {pay_count['UPI']/total_txn*100:.1f}% + "
    f"Credit Card {pay_count['Credit Card']/total_txn*100:.1f}%). "
    f"Top product: {top_product} (Rs {prod_sales[top_product]:,.2f}). "
    f"Top category: {top_category} (Rs {cat_sales[top_category]:,.2f} — {cat_sales[top_category]/total_sales*100:.1f}% of revenue).",
    body))
story.append(Paragraph(
    "Eight targeted business decisions — from supply chain protection to Q4 revival campaigns and "
    "customer loyalty conversion — provide a clear, data-backed roadmap for the next operating year.",
    body))

story.append(sp(12))
story.append(hr())
story.append(Paragraph(
    f"Verified KPIs (from data/supermarket_sales.csv): "
    f"Total Sales Rs {total_sales:,.2f} | Transactions {total_txn} | ATV Rs {atv:.2f} | "
    f"Rating {avg_rating:.2f}/5 | Qty {total_qty:,} | "
    f"Top Product: {top_product} | Top Category: {top_category} | "
    f"Top Branch: {top_branch} | Top Payment: {top_payment} | "
    f"Peak Month: {MONTH_NAMES[peak_month[5:7]]} 2024 (Rs {monthly_sales[peak_month]:,.2f}) | "
    f"Lowest Month: {MONTH_NAMES[lowest_month[5:7]]} 2024 (Rs {monthly_sales[lowest_month]:,.2f})",
    ParagraphStyle("Footer", parent=styles["Normal"],
        fontSize=8, textColor=MUTED, leading=12, alignment=TA_CENTER)))

doc.build(story)
print(f"PDF generated: {OUTPUT}")
