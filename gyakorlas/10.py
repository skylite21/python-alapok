# egy felhasználó által bekért emailcímből találd ki a felhasználónevet
# úgy, hogy a @ jel utáni részt levágjuk.
# john@gmail.com  -> john

email = input('irj be egy email címet: ')

username = email.split('@')[0]

print(username)
