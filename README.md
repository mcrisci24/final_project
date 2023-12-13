# Airline Data Analysis App

## Introduction
The Data Analysis App is a comprehensive web-based application designed to facilitate the exploration and visualization of data sets, but defaults to an airline performance dataset from the Bureau of Transportation Statistics. This tool enables users to upload their datasets for analysis or use a default dataset featuring major U.S. airlines. It supports a variety of interactive data visualizations, including comparisons between airlines.

## Purpose
This application serves as a platform for data analysts, students, and aviation enthusiasts to gain insights into airline performance metrics. The interactive nature of the app allows for dynamic exploration of data, aiding in educational and analytical pursuits.This project features a comprehensive Data Analysis Application built with Streamlit. The application provides interactive data visualization, hypothesis testing, and confidence interval analysis capabilities. It's designed to work with a default airline dataset, but users can upload their own datasets in CSV or XLSX format for analysis.

## Features
- Custom file upload for data analysis.
- Default dataset analysis of major U.S. airlines.
- Interactive visualizations with options for graph types including bar, line, scatter, and box plots.
- Comparative analysis feature to juxtapose two different airlines.
- Responsive web interface suitable for various devices.
- **Data Visualization**: Users can generate various types of plots like Bar, Line, Scatter, and Box plots.
- **Custom Data Upload**: Supports CSV and XLSX files for custom data analysis.
- **Confidence Intervals & Bootstrap Sampling**: Provides insights into the distribution and confidence intervals of selected data columns.
- **Hypothesis Testing**: Supports hypothesis testing for both quantitative and categorical variables.

## How to Use
1. Launch the application through a web browser.
2. Upload a cleaned Excel file or use the default dataset.
3. Choose an airline (or two for comparison).
4. Select variables and graph types for analysis.
5. Interact with the visualizations for insights.

## Packages and Libraries Used

### [Streamlit](https://streamlit.io/)
- **Description**: Used for building the web interface of the application.
- **Installation**: `pip install streamlit`.

### [Pandas](https://pandas.pydata.org/)
- **Description**: Used for data manipulation and analysis.
- **Installation**: `pip install pandas`.

### [Plotly Express](https://plotly.com/python/plotly-express/)
- **Description**: Used for creating interactive graphs.
- **Installation**: `pip install plotly`.

### [Seaborn](https://seaborn.pydata.org/)
- **Description**: Used for drawing statistical graphics.
- **Installation**: `pip install seaborn`.

### [Matplotlib](https://matplotlib.org/)
- **Description**: Used for generating additional graphs.
- **Installation**: `pip install matplotlib`.

### [Plotly.io](https://plotly.com/python-api-reference/plotly.io.html)
- **Description**: Used for low-level figure display operations.
- **Installation**: `pip install plotly.io`.

### [NumPy](https://numpy.org/)
- **Description**: Used for numerical operations.
- **Installation**: `pip install numpy`.

### [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)
- **Description**: Used for handling Excel file uploads.
- **Installation**: `pip install openpyxl`.

## How to Run the Application
1. Install all required packages.
2. Run the Streamlit application using the command: `streamlit run app.py`
3. Interact with the application through the web interface.

## Contributions
Contributions to this project are welcome. Please submit a pull request or open an issue for suggestions or bug reports.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contact
For more information or inquiries, please contact [m.crisci24@ncf.edu].

---
*Note: This project was developed as part of a final coursework assignment in [Intermediate Python, Professor Gil Salu] at [New College of Florida].*
