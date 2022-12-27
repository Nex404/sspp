from gtts import gTTS
import PyPDF2
from sys import argv

book = argv[1]
#insert name of your pdf 
pdfreader = PyPDF2.PdfReader(open(book, 'rb'))


ct = ""
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    ct += clean_text
#     print(clean_text)

mp3_name = book.strip(".pdf")

language = 'en'
myobj = gTTS(text=ct, lang=language, slow=False)
myobj.save(f"{mp3_name}.mp3")

