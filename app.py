import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title('New Delhi Air Pollution Analysis')

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())  # Displaying the first few rows of the dataset

        # Data Analysis and Visualization
        st.subheader('Data Analysis')

        st.subheader('Summary Statistics')
        st.write(df.describe())

        st.subheader('Missing Values')
        st.write(df.isnull().sum())

        # Data Visualization
        st.subheader('Data Visualizations')

        # Select column for plotting
        selected_column = st.selectbox("Select Column for Histogram", df.columns)

        # Create a Matplotlib figure and axes
        fig, ax = plt.subplots(figsize=(8, 6))

        # Plotting using Seaborn and Matplotlib
        sns.histplot(df[selected_column], kde=True, bins=30, ax=ax)

        # Display the Matplotlib figure using st.pyplot()
        st.pyplot(fig)

if __name__ == "__main__":
    main()
