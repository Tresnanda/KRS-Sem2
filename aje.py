from happytransformer import HappyTextToText
from happytransformer import TTSettings
mod = HappyTextToText("T5", "model")

def generate(input):
    input = "grammar: " + input
    beam_settings = TTSettings(num_beams=5, min_length=1, max_length=20)
    predicted = mod.generate_text(input, args=beam_settings)
    #correct = predicted.text.strip()
    return predicted.text

user_input = input("Kalimat anda: ")
#user_input = "grammar: " + user_input

correction = generate(user_input)
print("Kalimat dengan grammar yang benar: ", correction)