# 🏋️‍♂️ AI Health & Fitness Planner

A highly personalized health and wellness dashboard powered by LangChain and Llama-3.3-70b (via Groq Cloud) that calculates macro splits, provides tailored 7-day diet charts, and designs custom weekly workout routines.

## 🚀 Features
- **Dynamic Metric Calculator:** Inputs age, weight, height, activity level, and goals to estimate exact caloric needs.
- **Diet Preference Sorting:** Generates customized meal structures for Vegetarian, Non-Vegetarian, Vegan, or Keto diets.
- **7-Day Plan Layout:** Outputs granular meal options with tracked calories and protein counts.
- **Targeted Workouts:** Adjusts physical training programs dynamically based on goals like Muscle Gain, Weight Loss, or Endurance.

## 🛠️ Tech Stack
- **Framework:** LangChain (LLM Chains & Prompts)
- **LLM Engine:** Groq Cloud (Llama 3.3 70B Versatile)
- **Frontend Panel:** Streamlit
- **Configuration:** python-dotenv

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/subhu770/AI-Health-Planning.git](https://github.com/subhu770/AI-Health-Planning.git)
   cd AI-Health-Planning

   Install Dependences:
   pip install streamlit langchain langchain-groq python-dotenv

   Configure API Key:
   GROQ_API_KEY=your_groq_api_key_here

   Run Server
   streamlit run app.py
