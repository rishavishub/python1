import tkinter as tk
from translate import Translator

def translate_text():
    text = input_text.get("1.0", "end-1c")
    target_language = language_variable.get()

    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)

    output_text.delete("1.0", "end")
    output_text.insert("end", translation)

# Create the main window
window = tk.Tk()
window.title("Language Translator")

# Create input label and text box
input_label = tk.Label(window, text="Enter text:")
input_label.pack()
input_text = tk.Text(window, height=5)
input_text.pack()

# Create language selection drop-down menu
languages = ["en", "es", "fr", "de", "ja"]  # List of supported languages
language_variable = tk.StringVar(window)
language_variable.set(languages[0])  # Set default language
language_dropdown = tk.OptionMenu(window, language_variable, *languages)
language_dropdown.pack()

# Create translate button
translate_button = tk.Button(window, text="Translate", command=translate_text)
translate_button.pack()

# Create output label and text box
output_label = tk.Label(window, text="Translation:")
output_label.pack()
output_text = tk.Text(window, height=5)
output_text.pack()

# Start the main event loop
window.mainloop()
