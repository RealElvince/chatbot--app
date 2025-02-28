from openai import OpenAI
import streamlit as st

user = OpenAI(api_key="")
gptmodel ="gpt-3.5-turbo"
userrole ="user"

pre_prompt = "Teach me the following concepts:"
response=""

# app title
st.title("ProfessorGPT App")
st.divider()

 # prompt text area
prompt = st.text_input("What do you want to learning?")

# submit button
gptbutton = st.button("Teach Me")

# caption
st.caption("ProfessorGPT will work when you press the button.")
st.divider()
 
# on button click
if gptbutton:
    with st.spinner("I am preparing your lecture"):
        response = user.chat.completions.create(
            model = gptmodel,
            messages = [
        {"role":userrole,"content":pre_prompt + prompt}]
        )
    st.snow()
    st.write(response.choices[0].message.content)

    


