from flask import Flask, request, jsonify
import pandas as pd
import pickle

# Load your financial data
df = pd.read_csv('/Users/tresoryubahwe/Downloads/FinancialMarketData.csv') 


# Load the trained Isolation Forest model (from colab)
with open('/Users/tresoryubahwe/Downloads/optimized_isolation_forest.pkl', 'rb') as f:
    model = pickle.load(f)


# Validate model compatibility
if not hasattr(model, "predict"):
    raise ValueError("The loaded model does not have a 'predict' method. Please ensure it's the correct type.")

app = Flask(__name__)

# Root route for testing in a browser
@app.route('/')
def home():
    return "Welcome to the Market Anomaly Detection Chatbot! Use the /chat endpoint for queries."


def generate_response(user_query):
    user_query = user_query.lower()

    if "anomaly" in user_query:
        # Use the loaded model to make predictions
        X = StandardScaler().fit_transform(df[['VIX']])  
        predictions = model.predict(X)
        anomaly_count = (predictions == -1).sum()  
        return f"The model detected {anomaly_count} anomalies in the dataset."
    elif "portfolio" in user_query:
        # sample portfolio-related query
        sharpe_ratio = 1.5
        final_value = "$33,498,019.18"  
        return f"The final portfolio value is {final_value} with a Sharpe ratio of {sharpe_ratio}."
    elif "benchmark" in user_query:
        return "Your portfolio outperformed the benchmark by 334,880.19%."
    else:
        return "Sorry, I don't understand your query yet. Can you rephrase?"


# Chatbot API endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get('query', '')
    response = generate_response(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
