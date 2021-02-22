MORSE_CODE = {'....': 'h', '.-': 'a', '-...': 'b', '-.-.': 'c', '-..':
              'd', '.': 'e', '..-.': 'f', '--.': 'g', '..': 'i', '.---': 'j',
              '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
              '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
              '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
              '--..': 'z', '.-.-.-': '.', '..--..': '?', '--..--': ','}


def decodeMorse(morse_code):
    morse_code = morse_code.strip()
    words = morse_code.split('   ')
    decoded_words = []
    for word in words:
        word = word.split(' ')
        decoded_word = ''
        for c in word:
            if c in MORSE_CODE:
                decoded_c = MORSE_CODE[c]
                decoded_word = decoded_word + decoded_c.upper()
        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)


print(decodeMorse('.... . -.--   .--- ..- -.. .'))
