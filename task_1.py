import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("worldpopulation.csv")  # Replace "your_data.csv" with the path to your CSV file

# Now, you can explore your data and create visualizations.
# For example, let's say you have a column named "age" in your dataset.
# You can create a histogram to visualize the distribution of ages:

plt.figure(figsize=(8, 6))
sns.histplot(data['age'], bins=20, kde=True, color='skyblue')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')
plt.show()

