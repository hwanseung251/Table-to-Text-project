# -*- coding: utf-8 -*-
"""summary_generation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QkDb5f1GSAhz8FFLifd-MQ_8lzSAFez-
"""

from google.colab import drive
drive.mount('/content/gdrive')

import pandas as pd
import re

summary = pd.read_excel("/content/gdrive/MyDrive/2024_컨퍼런스/data/lime_summary_test.xlsx")
summary.head()

import pandas as pd
import re

# Function to generate analysis based on subscription status
def generate_subscription_analysis(row):
    text = row["text"]
    feature_contributions = row["feature_contributions"]
    y_value = row["y"]

    # Split feature contributions into a dictionary with absolute impact values
    contributions = {item.split(':')[0]: abs(float(item.split(':')[1])) for item in feature_contributions.split(', ')}
    sentences = re.split(r'[.!?]', text)  # Split text into sentences
    relevant_sentences = []

    # Sort features by descending absolute impact
    sorted_contributions = sorted(contributions.items(), key=lambda x: x[1], reverse=True)

    # Generate explanations based on subscription status
    for word, impact in sorted_contributions:
        for sentence in sentences:
            if word in sentence:
                if y_value.lower() == "no":
                    explanation = f"The word '{word}' (absolute impact: {impact}) is included in the following sentence, contributing to the customer's decision not to subscribe: '{sentence.strip()}'."
                elif y_value.lower() == "yes":
                    explanation = f"The word '{word}' (absolute impact: {impact}) is included in the following sentence, supporting the customer's decision to subscribe: '{sentence.strip()}'."
                relevant_sentences.append(explanation)
                break  # Only consider the first occurrence of each feature word

    return " ".join(relevant_sentences)  # Join explanations for a single output

# Apply the function to each row in the DataFrame
summary["analysis"] = summary.apply(generate_subscription_analysis, axis=1)

# Display the resulting DataFrame with the new 'analysis' column
print(summary[["text", "feature_contributions", "y", "analysis"]])

summary['analysis'][0]

summary.to_csv("summary_new.csv", index=False)

