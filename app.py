import streamlit as st

from database import query_db
from plot import plot_wells


def app():
    st.title("Enter your well criteria")

    depth = st.number_input("Min depth", 0, 10_000, value=2000, step=50)
    gradient = st.number_input("Min Gradient", 0., 0.3, value=0.01, step=0.001)

    well_data = query_db(depth, gradient)
    chart = plot_wells(well_data)
    
    st.write(chart)


if __name__ == "__main__":
    app()
    
    
    