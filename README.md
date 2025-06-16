# sentiment-analysis-chatbot

Chatbot with Azure AI Sentiment Analysis
In this project, I integrated a chatbot with Azure's Cognitive Services to perform sentiment analysis on user input. The chatbot responds to basic queries and analyzes the sentiment (positive, neutral, or negative) of the user's message in real-time using the Azure Text Analytics API.

Project Structure
sentiment_analysis.py: This file contains the function that connects to Azure's Cognitive Services and analyzes the sentiment of user input.

chatbot.py: This file implements the chatbot that interacts with users and calls the sentiment analysis function to provide real-time feedback on the sentiment of the user's message.

Requirements
To run this project, I need the following:

Python 3.x

Azure Cognitive Services Subscription (to access the Azure Text Analytics API)

Environment variables set for the Azure API key and endpoint

Setup Instructions
1. Set up your Azure Cognitive Services
Go to the Azure Portal.

Create a Language Service or Text Analytics API resource.

Obtain the API Key and Endpoint URI from the Keys and Endpoint section of the resource.

2. Set the environment variables
Before running the project, I need to set two environment variables: one for the API Key and one for the Endpoint URI.

For Windows (Command Prompt)
bash

SET MicrosoftAPIKey=your_api_key_here
SET MicrosoftAIServiceEndpoint=https://your_endpoint_here.cognitiveservices.azure.com/
For macOS/Linux (Terminal)
bash

export MicrosoftAPIKey="your_api_key_here"
export MicrosoftAIServiceEndpoint="https://your_endpoint_here.cognitiveservices.azure.com/"
I will replace your_api_key_here and your_endpoint_here with the actual API Key and Endpoint URI from my Azure account.

3. Install the required Python packages
I need to install the necessary libraries using this command:

bash

pip install azure-ai-textanalytics
4. Run the chatbot
Once everything is set up, I can run the chatbot using the following command:

bash

python chatbot.py
The chatbot will prompt me for input. I can type messages like "hello" or "how are you" to interact with the chatbot. The bot will also provide sentiment analysis results based on my input.

To exit the chatbot, I can simply type "bye".

Example Interaction
vbnet

Welcome to the chatbot! Type 'bye' to exit.
You: hello
Bot: Hi! How can I help you today?
You: I love this chatbot!
Sentiment: positive
Positive confidence: 0.85
Neutral confidence: 0.12
Negative confidence: 0.03
Bot: The sentiment of your message is: positive
You: bye
Bot: Goodbye! Have a nice day!
Troubleshooting
I need to make sure that I have set the API Key and Endpoint URI environment variables correctly.

If I encounter any errors related to the API, I will check that my Azure subscription is active and that I have the necessary permissions.
