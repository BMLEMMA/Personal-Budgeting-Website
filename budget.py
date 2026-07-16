import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pyarrow
import plotly.graph_objects as go


st.container(border=True) 
st.set_page_config(page_title="Personal Budget Visualizer", layout="wide")
st.title("Personal Budget Visualizer")
st.write("## Welcome")

pink_colors = ['#FF1493', "#010101", '#FFB6C1', '#FFC0CB']

#___________________Year & month selection_______________________________
st.header("Year and Month Selection")
years=[2026, 2027, 2028]
months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", 
        "Oct", "Nov", "Dec"]
col1, col2= st.columns(2)
with col1:
    year_option= st.selectbox(
        "Pick a year:",
        years
    )

with col2:
    month_option= st.selectbox(
        "Pick a month",
        months
    )

st.write(f"You selected: {month_option} {year_option}")


#___________________INCOME STREAMS__________________________________
#asking for the number of income streams:
st.header(f"Income Streams for the year of {year_option} and month of {month_option}")
no_inc_streams=int(st.number_input("Enter your number of income streams:", step=1))

inc_stream_lst=[]
inc_stream_hrly_lst=[]
inc_stream_hrs_lst=[]
for i in range (no_inc_streams):
    inc_stream=st.text_input(f"insert income stream #{i}", key=f"inc_name_{i}")
    inc_stream_lst.append (inc_stream)
    #st.write(f"total income streams: {inc_stream_lst}")
    inc_stream_inc=st.number_input(f"insert hourly income per stream #{i}", min_value=0, key=f"inc_hrly_{i}")
    inc_stream_hrly_lst.append (inc_stream_inc)
    #st.write(f"total income streams: {inc_stream_hrly_lst}")
    inc_stream_inc=st.number_input(f"insert number of hours worked per stream #{i}", min_value=0, key=f"inc_hrs_{i}")
    inc_stream_hrs_lst.append (inc_stream_inc)
    #st.write(f"total income streams: {inc_stream_hrs_lst}")


inc_stream_inc_lst=[]
for i in range (no_inc_streams):
    inc_stream_inc = inc_stream_hrly_lst[i] * inc_stream_hrs_lst[i]
    #st.write(i, inc_stream_hrly_lst[i], inc_stream_hrs_lst[i], inc_stream_inc)
    inc_stream_inc_lst.append (inc_stream_inc)
    st.write(f"total income from stream {i+1}: {inc_stream_inc_lst[i]}")



# --- Figure 1: Bar Chart ---
chart1, chart2=st.columns(2)
with chart1:
    fig1, ax1 = plt.subplots(figsize=(10,6))
    bars = ax1.bar(inc_stream_lst, inc_stream_inc_lst, color="lightpink", edgecolor="navy")
    ax1.bar_label(bars, padding=3)
    ax1.set_title('Income Stream Breakdown', fontsize=26, fontweight='bold', pad=15)
    ax1.set_xlabel('Income Stream', fontsize=12)
    ax1.set_ylabel('Amount', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig1)

with chart2:
# --- Figure 2: Pie Chart ---
    if sum(inc_stream_inc_lst) >0:
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        ax2.pie(inc_stream_inc_lst, labels=inc_stream_lst, autopct='%1.1f%%',
            colors=["lightpink", "skyblue", "grey"])
        ax2.set_title('Income Stream Percentage')
        plt.tight_layout()
        st.pyplot(fig2)




#______________________________EXPENSES_________________________________
st.header("Expense Categories")
no_categories=int(st.number_input("Enter the number of expense categories: ", step=1))


expense_choices = ["Emergency Fund", "Debt payments", "Major Purchase", "Improving Credit Score",
      "Down Payment", "Travelling or Fun Fund", "Retirement"]


# The widget returns a list directly into 'expense_options'
expense_options = st.multiselect("Choose your expenses:", expense_choices)

exp_stream_lst=[]
exp_stream_exp_lst=[]
label_sankey=["Income"]

for i in range (no_categories):
    exp_stream=expense_options[i]
    exp_stream_lst.append (expense_options[i])
    #st.write(f"total expense streams: {exp_stream_lst}")
    exp_stream_exp = st.number_input(f"insert expense amounts per stream #{i}", min_value=0, key=f"exp_amt_{i}") 
    exp_stream_exp_lst.append (exp_stream_exp)
    #st.write(f"total income streams: {exp_stream_exp_lst}")
    label_sankey.append(exp_stream)
    

#______________________SANKEY DIAGRAMS_______________________________________
st.write (label_sankey)
source=[]
target=[]
value=[]
for i in range (no_categories):
    source.append(0)
    target.append(i+1)
    value.append(exp_stream_exp_lst[i])

fig = go.Figure(
    go.Sankey(
        node=dict(
            label=label_sankey
        ),
        link=dict(
            source=source,
            target=target,
            value=value
        )
    )
)
st.plotly_chart(fig)


# --- Figure 1: Bar Chart ---
chart3, chart4=st.columns(2)
with chart3:
    fig3, ax3 = plt.subplots(figsize=(10,6))
    bars = ax3.bar(exp_stream_lst, exp_stream_exp_lst, color="lightpink", edgecolor="navy")
    ax3.set_title('Expense Stream Breakdown', fontsize=26, fontweight='bold', pad=15)
    ax3.bar_label(bars, padding=3)
    ax3.set_xlabel('Income Stream', fontsize=12)
    ax3.set_ylabel('Amount', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig3)  
    

# --- Figure 2: Pie Chart ---
with chart4:
    if sum(exp_stream_exp_lst)>0:
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        ax4.pie(exp_stream_exp_lst, labels=exp_stream_lst, autopct='%1.1f%%',
            colors=["lightpink", "skyblue", "grey"])
        ax4.set_title('Expense Stream Percentage')
        plt.tight_layout()
        st.pyplot(fig4)  


#____________________GOALS__________________________________________
st.write(f"The next few questions are aimed at assessing your financial goals")
goal_options= st.selectbox (
    "Select your current financial goals: ",
    ("Emergency Fund", "Debt payments", "Major Purchase", "Improving Credit Score",
      "Down Payment", "Travelling or Fun Fund", "Retirement")
)

st.success(f"Goal: {goal_options}")
st.write("A couple more questions about your financial situation")
