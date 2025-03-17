import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="📁 File Converter & Cleaner", page_icon=":smiley:", layout="wide")
st.title("📁 File Converter & Cleaner")
st.write("Upload your CSV and Excel files and convert them to the desired format effortlessly.")

# File uploader
files = st.file_uploader("Upload your files", type=["csv", "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1]

        # Read file
        if ext == "csv":
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file, engine="openpyxl")

        # Display file preview
        st.subheader(f"🔍 {file.name} - Preview")
        st.dataframe(df.head())

        # Fill missing values
        if st.checkbox(f"Fill missing values for {file.name}"):
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.success("Missing values filled successfully")
            st.dataframe(df.head())

        # Column selection
        selected_columns = st.multiselect(
            f"Select columns - {file.name}", df.columns, default=df.columns.tolist()
        )
        df = df[selected_columns]
        st.dataframe(df.head())

        # Show chart if numerical data exists
        if st.checkbox(f"📊 Show Chart - {file.name}") and not df.select_dtypes(include=["number"]).empty:
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # Format selection
        format_choice = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        # Initialize variables
        output = BytesIO()
        new_name = ""
        mime = ""

        # Download button
        if st.button(f"⬇ Download {file.name} as {format_choice}"):
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file.name.replace("." + ext, ".csv")
            else:
                df.to_excel(output, index=False, engine="openpyxl")
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file.name.replace("." + ext, ".xlsx")

            output.seek(0)  # Move to the start of the stream
            st.download_button(label=f"⬇ Download {new_name}", data=output, file_name=new_name, mime=mime)

            st.success("Processing Complete Successfully 🏄‍♂️")
