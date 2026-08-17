-- Core pricing analysis
SELECT "Proposed Price", SUM(Revenue) AS revenue, SUM("Gross Profit") AS gross_profit, AVG("Gross Margin %") AS avg_margin
FROM customer_pricing_dataset
GROUP BY "Proposed Price"
ORDER BY gross_profit DESC;

-- Segment economics
SELECT "Customer Segment", AVG("Willingness to Pay") AS avg_wtp, AVG("Price Sensitivity Score") AS avg_sensitivity, AVG(LTV) AS avg_ltv
FROM customer_pricing_dataset
GROUP BY "Customer Segment"
ORDER BY avg_ltv DESC;
