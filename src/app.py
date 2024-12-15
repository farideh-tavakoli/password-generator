import os
import streamlit as st
from main import PinGenerator, RandomPasswordGenerator, MemorablePasswordGenerator


current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "images", "banner.jpeg")

st.image(image_path, width=600)
st.title(":zap: Password Generator")

option = st.radio(
    "Select a password generator",
    ("Random Password", "Memorable Password", "Pin Code")
)

if option == "Pin Code":
    length = st.slider("Selct the length of the pin code", 4, 32, 8)
    generator = PinGenerator(length)
elif option == "Random Password":
    length = st.slider("Selct the length of the password", 4, 32, 8)
    include_symbols = st.toggle("include Symbols")
    include_number = st.toggle("include Number")
    generator = RandomPasswordGenerator(length, include_number, include_symbols)
elif option == "Memorable Password":
    number_of_words = st.slider("Select nimber of words in the password:", 4, 10, 6)
    seperator = st.text_input("Seperator", value="-")
    capitalize = st.toggle("Capitalization")
    generator = MemorablePasswordGenerator(number_of_words, seperator, capitalize)

if generator:
    password = generator.generate()
    st.write(fr"Your Password is: ``` {password} ``` ")
else:
    st.error("No generator selected.")