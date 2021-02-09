def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]


word = reverse(input('Enter a word:'))


def polidrono(word):
    if word == reverse(word):
        print("the word is a polydrome")

polidrono(word)
print('finish')
       
