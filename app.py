import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load Environment Variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# App Configuration
st.set_page_config(page_title="AI Health & Fitness Planner", page_icon="💪", layout="wide")
st.title("🏋️‍♂️ AI Health & Fitness Planner")
st.write("Get your customized, expert-level Diet Plan and Workout Routine instantly powered by AI!")

# Input Form Layout
with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age:", min_value=10, max_value=100, value=25)
        weight = st.number_input("Weight (in kg):", min_value=30, max_value=200, value=70)
        
    with col2:
        height = st.number_input("Height (in cm):", min_value=100, max_value=250, value=170)
        fitness_goal = st.selectbox("Fitness Goal:", ["Weight Loss", "Muscle Gain", "Stay Fit / Maintenance", "Endurance Training"])
        
    with col3:
        diet_preference = st.selectbox("Diet Preference:", ["Vegetarian", "Non-Vegetarian", "Vegan", "Keto"])
        activity_level = st.selectbox("Daily Activity Level:", ["Sedentary (Little or no exercise)", "Lightly Active", "Moderately Active", "Very Active"])

# Generate Button
if st.button("Generate My Fitness Plan 🚀"):
    if not groq_api_key:
        st.error("Please add your GROQ_API_KEY in the .env file!")
    else:
        with st.spinner("Calculating macros and designing your custom routine..."):
            try:
                # Initialize Llama 3.3 via Groq
                llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key, temperature=0.5)
                
                # Setup Expert Prompt Template
                fitness_prompt = ChatPromptTemplate.from_messages([
                    ("system", """You are a certified professional Nutritionist and Personal Fitness Trainer. 
                    Based on the user's metrics, create a highly personalized health package.
                    Structure your response cleanly using markdown with clear headings for:
                    1. Estimated Daily Caloric Needs & Macros (Protein, Carbs, Fats)
                    2. Customized 7-Day Diet Chart (matching their diet preference)
                    3. Weekly Workout Routine (matching their fitness goal)
                    4. Important Health & Hydration Tips"""),
                    ("human", f"""Here are my details:
                    - Age: {age}
                    - Weight: {weight} kg
                    - Height: {height} cm
                    - Fitness Goal: {fitness_goal}
                    - Diet Preference: {diet_preference}
                    - Activity Level: {activity_level}""")
                ])
                
                # Run Chain
                fitness_chain = fitness_prompt | llm
                plan_output = fitness_chain.invoke({}).content
                
                st.success("🎉 Your Personalized Fitness Plan is Ready!")
                st.markdown("---")
                st.markdown(plan_output)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")