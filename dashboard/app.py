import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
ROOT=Path(__file__).resolve().parents[1]
sc=pd.read_csv(ROOT/"data/price_elasticity_scenarios.csv")
sd=pd.read_csv(ROOT/"data/scenario_analysis.csv")
seg=pd.read_csv(ROOT/"data/segment_summary.csv")

st.set_page_config(page_title="Product Pricing Optimization Simulator",page_icon="₹",layout="wide")
st.title("Product Pricing Optimization Simulator")
st.caption("LearnFlow Pro — data-driven pricing decision dashboard")

price=st.sidebar.slider("Proposed Price (₹)",499,1999,1199,100)
demand=st.sidebar.slider("Expected Demand",500,2000,1080,10)
conversion=st.sidebar.slider("Conversion Rate",0.05,0.30,0.165,0.005)
unit_cost=st.sidebar.number_input("Unit Cost (₹)",value=105.0)
cac=st.sidebar.number_input("CAC (₹)",value=520.0)
churn=st.sidebar.slider("Churn Rate",0.01,0.15,0.041,0.001)
discount=st.sidebar.slider("Discount %",0.0,0.25,0.0,0.01)
net=price*(1-discount); customers=round(demand*conversion); revenue=net*customers; cost=unit_cost*customers; profit=revenue-cost; margin=profit/revenue if revenue else 0; ltv=(net*(1-churn)/churn)*margin; ltvcac=ltv/cac

c1,c2,c3,c4,c5,c6=st.columns(6)
c1.metric("Current Price","₹999"); c2.metric("Recommended Price","₹1,199"); c3.metric("Revenue",f"₹{revenue:,.0f}"); c4.metric("Gross Profit",f"₹{profit:,.0f}"); c5.metric("Gross Margin",f"{margin:.1%}"); c6.metric("LTV:CAC",f"{ltvcac:.1f}x")

a,b=st.columns(2)
with a: st.plotly_chart(px.line(sc,x="Price",y="Expected Demand",markers=True,title="Price vs Demand"),use_container_width=True)
with b: st.plotly_chart(px.line(sc,x="Price",y="Revenue",markers=True,title="Price vs Revenue"),use_container_width=True)
c,d=st.columns(2)
with c: st.plotly_chart(px.line(sc,x="Price",y="Profit",markers=True,title="Price vs Profit"),use_container_width=True)
with d: st.plotly_chart(px.bar(sd,x="Scenario",y="Profit",title="Scenario Profit Comparison"),use_container_width=True)

e,f=st.columns(2)
with e: st.plotly_chart(px.bar(seg,x="Segment",y="Avg Gross Profit",title="Segment Profitability"),use_container_width=True)
with f: st.plotly_chart(px.bar(seg,x="Segment",y="Avg Price Sensitivity",title="Segment Price Sensitivity"),use_container_width=True)

st.subheader("Product Manager Recommendation")
st.info("Increase the core price from ₹999 to ₹1,199 for the Pro plan. Protect conversion with value messaging and keep targeted student/entry discounts rather than blanket discounts. Run an A/B pricing test before full rollout.")
st.dataframe(sd,use_container_width=True)
