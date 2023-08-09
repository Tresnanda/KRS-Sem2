import streamlit as st
from happytransformer import HappyTextToText
from happytransformer import TTSettings
import pandas as pd

happy_tt = HappyTextToText("T5", "model")

def correct_grammar(input_text):
    beam_settings = TTSettings(num_beams=5, min_length=1, max_length=20)
    predicted_result = happy_tt.generate_text(input_text, args=beam_settings)
    corrected_text = predicted_result.text.strip()
    return corrected_text

def main():
    st.title("Project KRS Semester 2")

    user_input = st.text_area("Kalimat anda:")

    if user_input: #kalo ga kosong
        full_input = "grammar: " + user_input
        corrected_sentence = correct_grammar(full_input)
        st.subheader("Kalimat dengan grammar yang benar:")
        st.write(corrected_sentence)

if __name__ == "__main__":
    main()
