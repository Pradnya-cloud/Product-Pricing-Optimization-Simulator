# Product Pricing Optimization Simulator

## Project Overview
A portfolio-ready Product Management pricing simulation for **LearnFlow Pro**, a fictional EdTech SaaS product. The model evaluates willingness to pay, demand, conversion, competitor benchmarks, revenue, gross profit, margin, churn, CAC, LTV and LTV:CAC to recommend a price.

> All customer data and competitor price fields are illustrative/synthetic for portfolio use.

## Business Problem
The product currently uses a ₹999 monthly anchor. The business needs to know whether a higher price can improve revenue and profit without damaging conversion, churn, or customer economics.

## Objective
Identify the price that best balances customer growth, revenue, profitability and long-term unit economics.

## Product
**LearnFlow Pro** — an AI-assisted learning and productivity subscription for students, professionals and businesses.

**Features:** AI study planner, mock tests, progress analytics, personalized learning paths, team reporting and premium support.

**Business model:** subscription with Free, Basic, Pro and Enterprise tiers.

## Dataset
`data/customer_pricing_dataset.csv` contains 150 synthetic customer-level records with segment, region, price, competitor price, unit cost, WTP, demand, conversion, churn, discount, revenue, gross profit, margin, CAC, LTV, LTV:CAC, sensitivity, scenario and recommendation.

## Pricing Methodology
The project combines value-based pricing, competitor benchmarking and demand/elasticity simulation. The core equations are:

- Revenue = Price × Customers
- Gross Profit = Revenue − Variable Cost
- Gross Margin % = Gross Profit / Revenue
- LTV:CAC = LTV / CAC

## Customer Segmentation
Students, Individual Professionals, Small Businesses, Mid-Market and Enterprise are analyzed on WTP, price sensitivity, conversion, churn, LTV and profitability.

## Competitor Analysis
`data/competitor_benchmark.csv` provides an illustrative benchmark against Coursera Plus, Udemy, LinkedIn Learning and upGrad.

## Willingness to Pay
Use surveys, interviews, historical purchases, A/B tests, Van Westendorp Price Sensitivity Meter and basic conjoint analysis. The portfolio model treats segment WTP as a key price ceiling signal.

## Price Elasticity
`data/price_elasticity_scenarios.csv` compares ₹499, ₹699, ₹899, ₹999, ₹1,199, ₹1,499 and ₹1,999 across demand, conversion, customers, revenue, cost, profit, margin, churn and LTV.

## Pricing Simulator
Run the interactive simulator with Streamlit:

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

Inputs: proposed price, demand, conversion, unit cost, CAC, churn and discount. Outputs: customers, revenue, gross profit, margin, LTV and LTV:CAC.

## Scenario Analysis
Five scenarios are modeled: penetration, current, moderate increase, premium and promotional discount. The base recommendation is **₹1,199** for the core Pro plan.

## Dashboard
The dashboard contains KPI cards, price-demand, price-revenue, price-profit, scenario comparison, segment profitability, price sensitivity and a Product Manager recommendation box.

## Key Insights
1. ₹1,199 provides the best balance in the base model.
2. Maximum customers, revenue, profit and margin can occur at different prices.
3. Students require stronger price protection than Enterprise.
4. Targeted discounts are preferable to blanket discounting.
5. Small Business and Mid-Market offer attractive expansion opportunities.
6. Profit should be evaluated per customer/visitor, not only top-line revenue.
7. Churn can erase the benefit of a higher price.
8. LTV:CAC must be monitored after a price change.
9. Competitor pricing should be a reference, not the sole pricing method.
10. A/B testing is required before full rollout.

## Recommended Price
**₹1,199/month for the Pro plan**, with segment-specific entry pricing and targeted student discounts.

## Business Impact
The simulation shows how a moderate price increase can raise revenue and gross profit while preserving a meaningful conversion rate. Exact impact depends on real experiment results.

## Subscription Packaging
| Plan | Monthly | Annual | Target | Value |
|---|---:|---:|---|---|
| Free | ₹0 | ₹0 | Students/curious users | Core planner + limited AI |
| Basic | ₹699 | ₹6,990 | Students | Study planner + limited mocks |
| Pro | ₹1,199 | ₹11,990 | Professionals/serious learners | Full AI, analytics, unlimited mocks |
| Enterprise | Custom | Custom | Businesses | Admin, SSO, analytics, support |

## GitHub Structure
```text
product-pricing-optimization-simulator/
├── data/
│   ├── customer_pricing_dataset.csv
│   ├── price_elasticity_scenarios.csv
│   ├── scenario_analysis.csv
│   ├── segment_summary.csv
│   └── competitor_benchmark.csv
├── analysis/
│   └── pricing_analysis.py
├── dashboard/
│   └── app.py
├── pricing-simulator/
│   └── simulator.py
├── sql/
│   └── analysis.sql
├── docs/
│   ├── data_cleaning.md
│   ├── pricing_strategies.md
│   ├── business_insights.md
│   └── experiment.md
├── screenshots/
├── requirements.txt
└── README.md
```

## Tools
**Mandatory:** Excel/Google Sheets for data review and Power BI/Tableau or Streamlit for dashboarding.
**Optional:** SQL for analysis, Python for simulation, AI tools for interpretation.

## Resume
**One-line:** Built a Product Pricing Optimization Simulator using price elasticity, customer segmentation, willingness-to-pay and unit economics to recommend an optimal SaaS price.

**2–3 lines:** Built an end-to-end pricing analytics project for an EdTech SaaS product using 150 synthetic customer records. Modeled demand, conversion, revenue, gross profit, margin, churn, CAC, LTV and LTV:CAC across seven price points and five scenarios, recommending ₹1,199 for the Pro plan.

**ATS:** Product Management | Pricing Strategy | Revenue Optimization | Price Elasticity | Customer Segmentation | Willingness to Pay | Unit Economics | CAC | LTV | Product Analytics | Scenario Analysis | Business Strategy

## Interview Pitch
“I built a Product Pricing Optimization Simulator for a fictional EdTech SaaS product called LearnFlow Pro. The problem was deciding whether the existing ₹999 price was actually optimal. I created a synthetic customer dataset, segmented customers by willingness to pay and price sensitivity, benchmarked competitors, and simulated seven price points. I then compared conversion, customers, revenue, profit, margin, churn and LTV:CAC. The model recommended ₹1,199 for the Pro plan, while protecting price-sensitive users with lower entry tiers and targeted discounts. Before rollout, I would validate the recommendation through a controlled A/B pricing test.”

## LinkedIn Post
I built a **Product Pricing Optimization Simulator** to answer a practical Product Management question: *What price maximizes business value without damaging customer conversion and retention?*

I created a 150-record synthetic customer dataset and modeled willingness to pay, price sensitivity, demand, conversion, churn, CAC, LTV, revenue and gross profit across multiple pricing scenarios.

The base model recommends **₹1,199/month** for the Pro plan versus the ₹999 current anchor, with targeted discounts for price-sensitive segments.

Tools: Python, Pandas, Streamlit, SQL, Product Analytics, Unit Economics and Pricing Strategy.

GitHub: [ADD YOUR REPOSITORY LINK]

#ProductManagement #PricingStrategy #ProductAnalytics #RevenueOptimization #UnitEconomics #PriceElasticity #CustomerSegmentation

## Suggested LinkedIn Screenshots
1. Full pricing dashboard.
2. Price vs profit/revenue charts.
3. Customer segment economics.
4. Scenario comparison.
5. GitHub repository README.

## Final AI Dashboard Image Prompt
Create a realistic premium enterprise SaaS Product Management analytics dashboard titled “Product Pricing Optimization Simulator”. Show a complete desktop dashboard without cropping. Use a clean modern executive analytics UI, white/light background, subtle grid, dark typography, restrained blue/teal accent colors, rounded KPI cards, crisp charts and professional spacing. KPI cards: Current Price ₹999, Recommended Price ₹1,199, Revenue, Gross Profit, Gross Margin, LTV:CAC. Include Price vs Demand curve, Price vs Revenue graph, Price vs Profit graph, competitor pricing comparison, customer willingness-to-pay distribution, segment-wise price sensitivity, interactive-looking pricing scenario simulator, subscription plan comparison, and a final Product Manager Recommendation panel stating “Increase Pro price to ₹1,199; validate with A/B test”. Make it look like a real portfolio-quality Product Analytics dashboard, not a concept mockup. Entire dashboard visible in one screen.

## Future Scope
Add real transaction data, Bayesian price optimization, cohort retention, multi-product cannibalization, geo-pricing, experiment significance testing, automated competitor data collection and ML demand forecasting.
