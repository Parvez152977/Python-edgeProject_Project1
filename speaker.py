import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)   # Volume (0.0 to 1.0)

# The text you want to convert to speech
text = "Hello, how are you today?"

# Use the engine to say the text
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
