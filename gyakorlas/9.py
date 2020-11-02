# irj egy programot ami egy beírt mondatot szavanként visszaad, de fordítva.
# pl.: My name is John    -> John is name My

text = input('irj be egy szoveget: ')

text_list = text.split(' ')

text_list.reverse()
print(' '.join(text_list))
