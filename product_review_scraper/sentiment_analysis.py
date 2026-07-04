import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# ------------------------------------
# Initialize VADER Sentiment Analyzer
# ------------------------------------
analyzer = SentimentIntensityAnalyzer()

# ------------------------------------
# Load reviews from Web Scraping Team
# ------------------------------------
df = pd.read_csv("reviews.csv")

# ------------------------------------
# Function to classify sentiment
# ------------------------------------
def classify_sentiment(review):
    score = analyzer.polarity_scores(str(review))
    compound = score["compound"]

    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# ------------------------------------
# Add Sentiment Column
# ------------------------------------
df["Sentiment"] = df["Review Text"].apply(classify_sentiment)

# ------------------------------------
# Save Result
# ------------------------------------
df.to_csv("sentiment_results.csv", index=False)

# ------------------------------------
# Calculate Statistics
# ------------------------------------
total_reviews = len(df)

positive = (df["Sentiment"] == "Positive").sum()
negative = (df["Sentiment"] == "Negative").sum()
neutral = (df["Sentiment"] == "Neutral").sum()

positive_percentage = (positive / total_reviews) * 100
negative_percentage = (negative / total_reviews) * 100
neutral_percentage = (neutral / total_reviews) * 100

# ------------------------------------
# Display Statistics
# ------------------------------------
print("\n========== SENTIMENT ANALYSIS ==========")

print(f"Total Reviews       : {total_reviews}")
print(f"Positive Reviews    : {positive} ({positive_percentage:.2f}%)")
print(f"Negative Reviews    : {negative} ({negative_percentage:.2f}%)")
print(f"Neutral Reviews     : {neutral} ({neutral_percentage:.2f}%)")

print("\nOutput file generated successfully!")
print("Saved as sentiment_results.csv")