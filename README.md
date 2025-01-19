# Market Anomaly Detection
A machine learning project that detects anomalies in financial market data and evaluates portfolio performance.

## Features
- Detect anomalies in financial datasets using Isolation Forest.
- Analyze portfolio performance with key metrics like Sharpe ratio.
- Chatbot interface using Flask and Streamlit.

## Installation
1. Clone the repository:
git clone https://github.com/yourusername/Market-Anomaly-Detection.git
2. Navigate to the project directory:
cd Market-Anomaly-Detection
3. Install dependencies:
pip install -r requirements.txt
4. Run the backend:
python app.py
5. Run the Streamlit frontend:
streamlit run frontend.py

## Usage
Ask questions like:
- "Are there anomalies in the dataset?"
- "What is the Sharpe ratio?"

## File Structure
- `app.py`: Flask backend for the chatbot.
- `frontend.py`: Streamlit frontend interface.
- `optimized_isolation_forest.pkl`: Trained model.
- `FinancialMarketData.csv`: Sample financial data.
- `Anomaly-ModelPrep.ipynb`: Jupyter notebook with training code.
  
