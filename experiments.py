# istalgan sonni ildizini chiqarish
"""
def sonini_ildizini_chiqarib_ber(son):
    ildiz = son ** 0.5
    return ildiz

son = int(input("Istalgan sonni kiriting: "))
print(f"{son} ning ildizi: {sonini_ildizini_chiqarib_ber(son)}")
"""
# random 
"""
import random
print(random.randrange(1,10))
"""
yosh = 27
yildagi_kunlar = 365
sana = 3.25 * yildagi_kunlar
natija = yosh * sana
print(f"{yosh} yoshdagi odam {sana} kun yashab {natija} kun yashab.")

print("Hello world")

import re
def clean_text(text):
    # remove extra whitespace
     text = re.sub(' +', ' ', text)
     # remove special characters
     text = re.sub('[^A-Za-z0-9 ]+', '', text)
     #convert to lowercase
     text = text.lower()
     return text
input_text = input("Enter text:")
cleaned_text = clean_text(input_text)
print("Cleaned_text:", cleaned_text)



