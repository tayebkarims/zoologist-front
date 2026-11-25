import streamlit as st
import requests

st.markdown("""
# Zoologist front
""")

# st.markdown(
#     """
# Remember that there are several ways to output content into your web page...

# Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
# """
# )

# """
# ## Here we would like to add some controllers in order to ask the user to input the characteristics of the penguin. We need to know all the inputs required by our model to make a prediction.

# 1. Let's ask for:
# - island (the location where the penguin lives: Biscoe, Dream or Torgersen)
# - bill length (in mm)
# - bill depth (in mm)
# - flipper length (in mm)
# - body mass (in g)
# - sex ("Male" or "Female")
# """
st.markdown(
    """
    ## Input the characteristics of the penguin ?
    """
)
input_island = st.text_input('Island', '(Biscoe, Dream or Torgersen)')
input_bill_length = st.text_input('bill length (in mm)', '(in mm)')
input_bill_depth = st.text_input('bill depth (in mm)', '(in mm)')
input_flipper_length = st.text_input('flipper length (in mm)', '(in mm)')
input_body_mass = st.text_input('body mass', '(in g)')
selection_sex = st.radio('Select a sex ', ('Male', 'Female'))


if st.button('Prediction'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('I was predict 🎉')
else:
    st.write('I was not predict for now 😞')




# """
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Of course... The `requests` package 💡

# What are the steps to follow in order to call an API ?

# 1. Which url will you use? Save it in a variable so you can easily change it later...

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# """

url = 'http://localhost:8001/predict'

params = {
    "island" : input_island,
    "bill_length_mm" : input_bill_length,
    "bill_depth_mm" : input_bill_depth,
    "flipper_length_mm" : input_flipper_length,
    "body_mass_g" : input_body_mass,
    "sex" : selection_sex
}

response = requests.get(url, params=params).json()


st.markdown(f"""
# Your prediction is : {response['prediction']}
""")
