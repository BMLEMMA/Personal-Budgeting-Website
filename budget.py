import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(page_title="Personal Budget Visualizer", layout="wide")
st.title("Personal Budget Visualizer")

#___________________INCOME STREAMS__________________________________
#asking for the number of income streams:
st.header("Income Streams")
no_inc_streams=int(st.number_input("Enter your number of income streams:"))

inc_stream_lst=[]
for i in range (no_inc_streams):
    inc_stream=st.text_input(f"insert income stream #{i}", key=f"inc_name_{i}")
    inc_stream_lst.append (inc_stream)
    print(f"total income streams: {inc_stream_lst}")


inc_stream_inc_lst=[]
for i in range (no_inc_streams):
    inc_stream_inc=st.number_input(f"insert income amounts per stream #{i}", min_value=0, key=f"inc_amt_{i}")
    inc_stream_inc_lst.append (inc_stream_inc)
    print(f"total income streams: {inc_stream_inc_lst}")


inc_stream_inc_dict = {}
for i in range(len(inc_stream_lst)):
    inc_stream_inc_dict[inc_stream_lst[i]] = inc_stream_inc_lst[i]
    print(inc_stream_inc_dict)



# --- Figure 1: Bar Chart ---
fig1, ax1 = plt.subplots(figsize=(10,6))
bars = ax1.bar(inc_stream_lst, inc_stream_inc_lst, color="lightpink", edgecolor="navy")
ax1.bar_label(bars, padding=3)
ax1.set_title('Income Stream Breakdown', fontsize=26, fontweight='bold', pad=15)
ax1.set_xlabel('Income Stream', fontsize=12)
ax1.set_ylabel('Amount', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig1)

# --- Figure 2: Pie Chart ---
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.pie(inc_stream_inc_lst, labels=inc_stream_lst, autopct='%1.1f%%',
        colors=["lightpink", "skyblue", "grey"])
ax2.set_title('Income Stream Percentage')
plt.tight_layout()
st.pyplot(fig2)




#______________________________EXPENSES_________________________________
st.header("Expense Categories")
no_categories=int(st.number_input("Enter the number of expense categories: "))

exp_stream_lst=[]
for i in range (no_categories):
    exp_stream=st.text_input(f"Enter expense stream #{i}", key=f"exp_name_{i}")
    exp_stream_lst.append (exp_stream)
    print(f"total expense streams: {exp_stream_lst}")

exp_stream_exp_lst=[]
for i in range (no_categories):
    exp_stream_exp = st.number_input(f"insert income amounts per stream #{i}", min_value=0, key=f"exp_amt_{i}") 
    exp_stream_exp_lst.append (exp_stream_exp)
    print(f"total income streams: {exp_stream_exp_lst}")



# --- Figure 1: Bar Chart ---
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
fig4, ax4 = plt.subplots(figsize=(10, 6))
ax4.pie(exp_stream_exp_lst, labels=exp_stream_lst, autopct='%1.1f%%',
        colors=["lightpink", "skyblue", "grey"])
ax4.set_title('Expense Stream Percentage')

plt.tight_layout()
st.pyplot(fig4)  
