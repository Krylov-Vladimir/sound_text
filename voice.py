from gtts import gTTS
from playsound import playsound
text_val = 'Welcome to it develop'

language = 'en'

obj = gTTS(text=text_val, lang=language, slow=False)
obj.save("test.mp3")
playsound("test.mp3")
