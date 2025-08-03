import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\PALASH\Downloads\twitter_training.csv")
df.columns = ["Tweet_ID", "Topic", "Sentiment", "Tweet"]

sns.countplot(data=df, x="Sentiment", palette="pastel")
plt.title("Overall Sentiment Distribution")
plt.show()