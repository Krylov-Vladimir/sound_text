from gtts import gTTS
from playsound import playsound
text_val = 'Приветсвую программиста'

language = 'ru'

obj = gTTS(text=text_val, lang=language, slow=False)
obj.save("test.mp3")
playsound("test.mp3")
