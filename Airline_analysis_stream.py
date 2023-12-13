import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
from scipy.stats import ttest_ind, ttest_1samp

# Load default data
default_data = pd.read_csv("C:\\Users\\markc\\Downloads\\Airline_issues.csv")

# Function to perform bootstrap sampling
def bootstrap_sampling(data, columns, n_bootstrap=10000):
    bootstrap_means = []
    for _ in range(n_bootstrap):
        sample = data.sample(n=len(data), replace=True)
        means = sample[columns].mean()
        bootstrap_means.append(means)
    return pd.DataFrame(bootstrap_means)

# Function to create a confidence interval plot
def create_ci_plot(data, columns, n_bootstrap=10000):
    bootstrap_means = bootstrap_sampling(data, columns, n_bootstrap)
    fig = px.histogram(bootstrap_means, nbins=30)
    for column in columns:
        lower_bound = np.percentile(bootstrap_means[column], 2.5)
        upper_bound = np.percentile(bootstrap_means[column], 97.5)
        fig.add_vline(x=lower_bound, line_color='red')
        fig.add_vline(x=upper_bound, line_color='red')
        fig.update_layout(title=f'Bootstrap Sampling of {column}')
    return fig

# Function to perform hypothesis testing
def perform_hypothesis_test(data, col1, col2, alpha, test_type):
    if test_type == "quantitative":
        stat, p_value = ttest_ind(data[col1], data[col2], nan_policy='omit')
    elif test_type == "categorical":
        unique_categories = data[col1].unique()
        category = st.selectbox("Select category for comparison", unique_categories)
        category_mean = data[data[col1] == category][col2].mean()
        stat, p_value = ttest_1samp(data[col2], category_mean)
    return stat, p_value, "Reject Null Hypothesis" if p_value < alpha else "Fail to Reject Null Hypothesis"

def create_diff_means_ci_plot(data, col1_name, col2_name, n_bootstrap=1000):
    bootstrap_diff_means = []
    for _ in range(n_bootstrap):
        sample1 = data[col1_name].sample(n=len(data), replace=True)
        sample2 = data[col2_name].sample(n=len(data), replace=True)
        diff_mean = sample1.mean() - sample2.mean()
        bootstrap_diff_means.append(diff_mean)

    lower_bound = np.percentile(bootstrap_diff_means, 2.5)
    upper_bound = np.percentile(bootstrap_diff_means, 97.5)
    ci_fig = px.histogram(x=bootstrap_diff_means, nbins=30, title=f'Bootstrap Sampling of Difference in Means')
    ci_fig.add_vline(x=lower_bound, line_color='red')
    ci_fig.add_vline(x=upper_bound, line_color='red')

    return ci_fig

def create_plot(data, graph_type, numeric_columns, categorical_columns, suffix):
    x_var = st.selectbox(f'Select a variable for x-axis {suffix}', categorical_columns + numeric_columns, key=f'x_var{suffix}')
    y_var = st.selectbox(f'Select a variable for y-axis {suffix}', numeric_columns, key=f'y_var{suffix}')

    if graph_type == 'Line':
        fig = px.line(data, x=x_var, y=y_var, markers=True, title=f'{graph_type} Plot')
    elif graph_type == 'Bar':
        fig = px.bar(data, x=x_var, y=y_var, title=f'{graph_type} Plot')
    elif graph_type == 'Scatter':
        fig = px.scatter(data, x=x_var, y=y_var, title=f'{graph_type} Plot')
    elif graph_type == 'Box':
        fig = px.box(data, x=x_var, y=y_var, title=f'{graph_type} Plot')
    else:
        fig = px.line(data, x=x_var, y=y_var, title='Default Line Plot')

    return fig

''' Defines Main Streamlit app function and creates interactive features to play with data sets'''
def streamlit_app():
    st.title('Data Analysis App')

    # Custom file uploader
    uploaded_file = st.file_uploader("Upload your cleaned data file", type=['csv', 'xlsx'])

    # Data loading for new files. This removes default file
    if uploaded_file:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            data = pd.read_excel(uploaded_file, engine='openpyxl')
    else:
        data = default_data

    is_default_data = uploaded_file is None

    # Dropdowns for selecting variables
    numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
    categorical_columns = ['month'] if is_default_data else data.select_dtypes(include=['object', 'category']).columns.tolist()

    graph_types = ['Bar', 'Line', 'Scatter', 'Box']

    # Checkbox to select a second airline for comparison (only if default dataset is used)
    compare_second_airline = st.checkbox("Compare with another Airline") if is_default_data else False

    # Side-by-side graphs for the first airline
    col1, col2 = st.columns(2)
    with col1:
        selected_graph_type_a1 = st.selectbox('Select Graph Type - Graph A', graph_types, key='graph_type_a1')
        fig_1a = create_plot(data, selected_graph_type_a1, numeric_columns, categorical_columns, "_1a")
        st.plotly_chart(fig_1a, use_container_width=True)

    with col2:
        selected_graph_type_b1 = st.selectbox('Select Graph Type - Graph B', graph_types, key='graph_type_b1')
        fig_1b = create_plot(data, selected_graph_type_b1, numeric_columns, categorical_columns, "_1b")
        st.plotly_chart(fig_1b, use_container_width=True)

    # Side-by-side graphs for the second airline (if box is checked)
    if compare_second_airline:
        selected_airline_2 = st.selectbox('Choose a Second Airline to Compare', default_data['carrier_name'].unique(), key='airline_2')
        airline_data_2 = default_data[default_data['carrier_name'] == selected_airline_2]

        col3, col4 = st.columns(2)
        with col3:
            selected_graph_type_a2 = st.selectbox('Select Graph Type for Airline 2 - Graph A', graph_types, key='graph_type_a2')
            fig_2a = create_plot(airline_data_2, selected_graph_type_a2, numeric_columns, categorical_columns, "_2a")
            st.plotly_chart(fig_2a, use_container_width=True)

        with col4:
            selected_graph_type_b2 = st.selectbox('Select Graph Type for Airline 2 - Graph B', graph_types, key='graph_type_b2')
            fig_2b = create_plot(airline_data_2, selected_graph_type_b2, numeric_columns, categorical_columns, "_2b")
            st.plotly_chart(fig_2b, use_container_width=True)

    # Confidence interval and bootstrap section with two variable selection
    st.header("Confidence Intervals and Bootstrap Sampling")
    select_two_variables = st.checkbox("Select two variables")

    if select_two_variables:
        selected_columns = st.multiselect("Select two Columns for Analysis", numeric_columns, default=numeric_columns[:2])
        if len(selected_columns) != 2:
            st.error("Please select exactly two variables.")
        else:
            if st.button("Generate Bootstrap Plot for Two Variables"):
                ci_fig = create_ci_plot(data, selected_columns)
                st.plotly_chart(ci_fig, use_container_width=True)
    else:
        selected_column = st.selectbox("Select a Column for Analysis", numeric_columns)
        if st.button("Generate Bootstrap Plot"):
            ci_fig = create_ci_plot(data, [selected_column])
            st.plotly_chart(ci_fig, use_container_width=True)

    # Confidence interval and hypothesis testing section-- create titles
    st.header("Confidence Intervals, Bootstrap Sampling, and Hypothesis Testing")
    analysis_type = st.radio("Choose analysis type", ("Difference in Two Means", "Hypothesis Test"))
    #Drop down menu for difference in two means
    if analysis_type == "Difference in Two Means":
        col1_name = st.selectbox("Select first quantitative variable", numeric_columns, key="col1")
        col2_name = st.selectbox("Select second quantitative variable", numeric_columns, key="col2")
        if st.button("Generate Bootstrap Plot for Difference in Means"):
            ci_fig = create_diff_means_ci_plot(data, col1_name, col2_name)
            st.plotly_chart(ci_fig, use_container_width=True)

    elif analysis_type == "Hypothesis Test":
        test_type = st.radio("Select Test Type", ("quantitative", "categorical"))
        hypothesis_col1 = st.selectbox("Select first variable for hypothesis test", numeric_columns, key="hyp_col1")
        hypothesis_col2 = st.selectbox("Select second variable for hypothesis test", numeric_columns, key="hyp_col2")
        alpha = st.number_input("Enter significance level (alpha)", value=0.05, min_value=0.0, max_value=1.0, step=0.01)
        if st.button("Perform Hypothesis Test"):
            stat, p_value, result = perform_hypothesis_test(data, hypothesis_col1, hypothesis_col2, alpha, test_type)
            st.write(f"T-statistic: {stat}, P-value: {p_value:.4f}")
            st.write(f"Result: {result}")


if __name__ == '__main__':
    streamlit_app()
