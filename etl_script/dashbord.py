import duckdb
import streamlit as st
import plotly.express as px

# Load data
con = duckdb.connect("burger_info.duckdb")
df = con.execute("SELECT * FROM burgers").fetchdf()

df["veg_label"] = df["veg"].map({True: "Veg 🍔", False: "Non-Veg 🍔"})

st.title("🍔 Burger Dashboard")

# Create 2 columns for side-by-side display
col1, spacer, col2 = st.columns([5, 1, 5])

with col1:
    st.subheader("💰 Price Bar Chart")
    price_fig = px.bar(
        df, 
        x="name", 
        y="price", 
        title="Price Chart",
        text="price",
        color_discrete_sequence=["#636EFA"]
        )
    st.plotly_chart(price_fig, use_container_width=True)

with col2:
    st.subheader("🥦 Veg vs 🍖 Non-Veg Pie Chart")
    veg_fig = px.pie(
        df, 
        names="veg_label", 
        title="Veg vs Non-Veg", 
        color="veg_label", 
        color_discrete_map={"Veg 🍔": "green", "Non-Veg 🍔": "red"}
        )
    veg_fig.update_traces(
    textinfo='percent',
    textfont_size=16,
    textfont_color='black',
    insidetextorientation='radial')
    veg_fig.update_layout(
    showlegend=True,  # Make sure legend is visible
    legend=dict(
        title="Category",
        itemsizing='constant',  # fixes the size of legend items
        traceorder="normal",
        font=dict(size=14),
        bgcolor='rgba(0,0,0,0)',  # transparent background
        bordercolor='Black',
        borderwidth=0,
        itemclick='toggleothers',
        itemdoubleclick='toggle'
    ))
    st.plotly_chart(veg_fig, use_container_width=True)