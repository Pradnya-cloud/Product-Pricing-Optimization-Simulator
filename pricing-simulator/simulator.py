import pandas as pd

def simulate(price, demand, conversion, unit_cost, cac, churn, discount=0):
    net_price=price*(1-discount)
    customers=round(demand*conversion)
    revenue=net_price*customers
    variable_cost=unit_cost*customers
    gross_profit=revenue-variable_cost
    margin=gross_profit/revenue if revenue else 0
    ltv=(net_price*(1-churn)/churn)*margin if churn else 0
    ltvcac=ltv/cac if cac else 0
    return {"customers":customers,"revenue":revenue,"gross_profit":gross_profit,"margin":margin,"ltv":ltv,"ltv_cac":ltvcac}

if __name__ == "__main__":
    print(simulate(1199,1080,.165,105,520,.041,.0))
