import pandas as pd
import numpy as np
import webbrowser  # library used to open files in a browser

# Create a DataFrame of ten rows and four columns with random values
np.random.seed(42)  # For reproducibility
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])

# Function to highlight specific columns
def highlight_columns(s):
    color_map = {'A': 'background-color: lightblue', 
                 'B': 'background-color: lightgreen', 
                 'C': 'background-color: lightpink', 
                 'D': 'background-color: lightgray'}
    return [color_map.get(s.name, '')] * len(s)

# Apply the styling function
styled_df = df.style.apply(highlight_columns, subset=['A', 'B', 'C', 'D'])

# Save the styled DataFrame to an HTML file
html_file = "styled_dataframe.html"
styled_df.to_html(html_file)

# Open the HTML file in the default web browser
webbrowser.open(html_file)
