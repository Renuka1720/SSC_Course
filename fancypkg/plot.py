# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_time_series(data, time_column, title, xlabel, ylabel):
    """Plot time series data."""
    data.set_index(time_column, inplace=True)
    data.plot(figsize=(10, 6), marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_filtered_data(data, threshold, time_column, title, xlabel, ylabel):
    """Plot data after filtering columns based on variance."""
    data.set_index(time_column, inplace=True)
    variances = data.var()
    filtered_data = data.loc[:, variances > threshold]

    print("Dropped columns:", variances[variances <= threshold].index.tolist())
    print("Remaining columns:", filtered_data.columns.tolist())

    filtered_data.plot(figsize=(10, 6), marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("filtered_plot.pdf")  # Save as PDF
    plt.show()


def plot_fourier_transform(data, time_column, title):
    """Plot the Fourier transform of the data."""
    data.set_index(time_column, inplace=True)
    fourier_transforms = np.fft.fft(data, axis=0)
    freq = np.fft.fftfreq(data.shape[0])

    plt.figure(figsize=(10, 6))
    for i in range(data.shape[1]):
        plt.plot(freq, np.abs(fourier_transforms[:, i]), label=f"Column {i+1}")

    plt.title(title)
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("fourier_plot.pdf")  # Save as PDF
    plt.show()
