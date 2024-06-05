import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level']) 

    # Create first line of best fit
    first_best_fit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    year_min_to_2050 = np.arange(df['Year'].min(), 2051, 1)
    plt.plot(year_min_to_2050, first_best_fit.intercept + first_best_fit.slope*year_min_to_2050, label='First', color='red')

    # Create second line of best fit
    df_2000_beyond = df[df['Year'] >= 2000]
    second_best_fit = linregress(df_2000_beyond['Year'], df_2000_beyond['CSIRO Adjusted Sea Level'])
    
    year_2000_to_2050 = np.arange(df_2000_beyond['Year'].min(), 2051, 1)
    plt.plot(year_2000_to_2050, second_best_fit.intercept + second_best_fit.slope*year_2000_to_2050, label='Second', color='blue')

    # Add labels and title
    # plt.legend()
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()