# Q: Write an import statement that imports the function pyplot from the module matplotlib and renames it to plt.
import pyplot as plt
def build_histogram(data):
    hist = {}
    for i in data:
        hist[i] = hist.get(i, 0) + 1
    return hist

def plot_histogram(histogram):
    x_values = list(histogram.keys())
    y_values = list(histogram.values())

    plt.bar(x_values, y_values)
    plt.xlabel('Items')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()


