
import pyttsx3

print("===== CONTINUOUS TEXT TO SPEECH =====")
print("Type 'exit' to stop.\n")

while True:
    text = input("Enter text: ").strip()

    if text.lower() == "exit":
        print("Program stopped.")
        break

    if not text:
        print("Please enter some text.")
        continue

    try:
        # Create a fresh speech engine for each sentence
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        del engine

    except Exception as e:
        print("Speech error:", e)
