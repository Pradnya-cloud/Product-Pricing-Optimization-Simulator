# Data Cleaning

**Before → After examples**

| Issue | Before | After |
|---|---|---|
| Duplicate ID | CUST0042 repeated | Keep one valid row |
| Missing WTP | blank | Impute segment median |
| Price format | `₹ 1,199/month` | `1199` numeric |
| Segment spelling | `student`, `Students ` | `Students` |
| Percentage | `18` | `0.18` |
| Impossible value | churn `-0.05` | flag and correct |

Validation rules: unique Customer ID; prices/costs > 0; 0 ≤ conversion/churn/discount ≤ 1; revenue = net price × customers; gross profit = revenue − variable cost; margins between 0 and 1.
