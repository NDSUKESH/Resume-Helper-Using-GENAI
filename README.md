# Resume-Helper-Using-GENAI

## Overview
This project uses Google Gemini Pro model the Resume evaluation and helping to upgrade it 

### Prerequisites

Before running the code, ensure you have the required libraries installed. You can install them using:

```bash
pip install -r requirements.txt
```

- Note: First run sql.py to create the db then run app.py

### Setting up Environment Variables

Create a `.env` file in the project directory and add your Google API key:

```dotenv
GOOGLE_API_KEY=your_api_key_here
```

### Running the Application
Run the main.py file:
```run
streamlit run app.py
```


### Model Information
The code uses the GeminiAI Generative Model named 'gemini-pro' for output

### Dependencies
- Python 3.10
- Streamlit
- GeminiAI
