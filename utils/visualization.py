import matplotlib.pyplot as plt
import os

def generate_insights_chart(matched, missing):
    """Generate a bar chart showing matched and missing skills."""
    labels = ['Matched', 'Missing']
    values = [len(matched), len(missing)]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=['green', 'red'])
    plt.title("Matching Insights")
    plt.ylabel("Count")
    plt.savefig("static/insights_chart.png")
    return "static/insights_chart.png"
