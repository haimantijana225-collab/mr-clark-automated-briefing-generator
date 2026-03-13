import re
import matplotlib.pyplot as plt


def generate_chart_from_text(text):

    numbers = re.findall(r"\d+", text)

    if len(numbers) < 2:
        return None

    numbers = [int(n) for n in numbers[:5]]

    labels = [f"Item {i+1}" for i in range(len(numbers))]

    plt.figure()

    plt.bar(labels, numbers)

    chart_path = "chart.png"

    plt.savefig(chart_path)

    plt.close()

    return chart_path