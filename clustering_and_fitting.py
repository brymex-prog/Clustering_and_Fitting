"""
This is the template file for the clustering and fitting assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
Fitting should be done with only 1 target variable and 1 feature variable,
likewise, clustering should be done with only 2 variables.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots()
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df):
    fig, ax = plt.subplots()
    plt.savefig('categorical_plot.png')
    return


def plot_statistical_plot(df):
    fig, ax = plt.subplots()
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df, col: str):
    mean =
    stddev =
    skew =
    excess_kurtosis =
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    # You should preprocess your data in this function and
    # make use of quick features such as 'describe', 'head/tail' and 'corr'.
    return df


def writing(moments, col):
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    # Delete the following options as appropriate for your data.
    # Not skewed and mesokurtic can be defined with asymmetries <-2 or >2.
    print('The data was right/left/not skewed and platy/meso/leptokurtic.')
    return


def perform_clustering(df, col1, col2):

    def plot_elbow_method():
        fig, ax = plt.subplots()
        plt.savefig('elbow_plot.png')
        return

    def one_silhouette_inertia():
        _score =
        _inertia =
        return _score, _inertia

    # Gather data and scale

    # Find best number of clusters
    one_silhouette_inertia()
    plot_elbow_method()

    # Get cluster centers
    return labels, data, xkmeans, ykmeans, cenlabels


def plot_clustered_data(labels, data, xkmeans, ykmeans, centre_labels):
    fig, ax = plt.subplots()
    plt.savefig('clustering.png')
    return


def perform_fitting(df, col1, col2):
    # Gather data and prepare for fitting

    # Fit model

    # Predict across x
    return data, x, y


def plot_fitted_data(data, x, y):
    fig, ax = plt.subplots()
    plt.savefig('fitting.png')
    return


def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = '<your chosen column for analysis>'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    clustering_results = perform_clustering(df, '<your chosen x data>', '<your chosen y data>')
    plot_clustered_data(*clustering_results)
    fitting_results = perform_fitting(df, '<your chosen x data>', '<your chosen y data>')
    plot_fitted_data(*fitting_results)
    return


if __name__ == '__main__':
    main()
