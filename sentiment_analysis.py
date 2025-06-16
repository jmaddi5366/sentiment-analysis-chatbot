# sentiment_analysis.py
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Get API key and endpoint from environment variables
API_KEY = os.environ.get('MicrosoftAPIKey')
ENDPOINT_URI = os.environ.get('MicrosoftAIServiceEndpoint')

# Debug: Print API_KEY and ENDPOINT_URI
print(f"API Key: {API_KEY}")
print(f"Endpoint URI: {ENDPOINT_URI}")

# Ensure the variables are not None
if not API_KEY or not ENDPOINT_URI:
    raise ValueError("API Key or Endpoint URI is missing.")

# Set up the client to use the API
client = TextAnalyticsClient(endpoint=ENDPOINT_URI, credential=AzureKeyCredential(API_KEY))

# Function to analyze sentiment
def analyze_sentiment(text):
    try:
        # Analyze sentiment
        response = client.analyze_sentiment([text])[0]
        print(f"Sentiment: {response.sentiment}")
        print(f"Positive confidence: {response.confidence_scores.positive}")
        print(f"Neutral confidence: {response.confidence_scores.neutral}")
        print(f"Negative confidence: {response.confidence_scores.negative}")
        return response.sentiment
    except Exception as e:
        print(f"Error: {e}")
        return None
