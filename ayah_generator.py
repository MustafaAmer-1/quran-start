import arabic_reshaper
from bidi.algorithm import get_display

import requests, random

ayah = random.randint(0, 6236)
url = 'http://api.alquran.cloud/v1/ayah/' + str(ayah)

res = requests.get(url)
data = res.json()

text_ayah = data['data']['text'] # the text which will be passed to the website  

reshaped_text = arabic_reshaper.reshape(text_ayah)    # correct its shape
bidi_text = get_display(reshaped_text)           # correct its direction

print(bidi_text) # reshaped text for python only
