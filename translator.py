from googletrans import Translator
translator = Translator()
text = input("Enter text:")
translated = translator.translate(text, dest='ta')
print("Translated Text:",translated.text)