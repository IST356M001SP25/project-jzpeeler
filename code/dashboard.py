import streamlit as st
from load import load_clean_data
import pandas as pd
import plotly.express as px

# Load cleaned data
df = load_clean_data()

st.title("📍 NYC 311 Complaint Explorer")
st.markdown("Explore recent service complaints in New York City by borough and complaint type.")

# Sidebar Filters
st.sidebar.header("🔎 Filters")

# Filter 1: Borough
boroughs = sorted(df["borough"].dropna().unique())
selected_borough = st.sidebar.selectbox("Select Borough", boroughs)

# Filter 2: Complaint Type (limited to borough)
df_borough = df[df["borough"] == selected_borough]
complaint_types = sorted(df_borough["complaint_type"].dropna().unique())

# ✅ Select all complaint types by default
selected_complaints = st.sidebar.multiselect(
    "Select Complaint Types",
    complaint_types,
    default=complaint_types
)

# Apply filters
filtered = df_borough[df_borough["complaint_type"].isin(selected_complaints)]

# Display selected filter summary
selected_label = ", ".join(selected_complaints) if selected_complaints else "No Complaint Types Selected"
st.write(f"Showing **{len(filtered)}** complaints for **{selected_label}** in **{selected_borough}**")

# 🗺️ Complaint Density Map (Plotly)
st.subheader("🗺️ Complaint Density Map")
if not filtered.empty and not filtered[["latitude", "longitude"]].dropna().empty:
    fig = px.scatter_mapbox(
        filtered,
        lat="latitude",
        lon="longitude",
        hover_data=["descriptor"],
        color_discrete_sequence=["blue"],
        zoom=10,
        height=500,
    )
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig)
else:
    st.info("No location data available for this selection.")

# 🔠 Top Descriptors
st.subheader("🔠 Top Descriptors")
if not filtered.empty:
    top_desc = filtered["descriptor"].value_counts().head(10)
    if not top_desc.empty:
        st.bar_chart(top_desc)
    else:
        st.info("No descriptors available for this selection.")
else:
    st.info("No descriptor data available.")

# 📌 Top Complaint Types in Selected Borough
st.subheader(f"📌 Top Complaint Types in {selected_borough}")
top_types = df_borough["complaint_type"].value_counts().head(10)
if not top_types.empty:
    st.bar_chart(top_types)
else:
    st.info("No complaint types to show.")

# ⬇️ Download Button
st.subheader("⬇️ Download Filtered Data")
if not filtered.empty:
    csv = filtered.to_csv(index=False)
    st.download_button(
        label="Download as CSV",
        data=csv,
        file_name="filtered_311_complaints.csv",
        mime="text/csv",
    )
else:
    st.info("No data to download.")