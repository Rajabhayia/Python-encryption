# Caesar Cipher

try:
    # The string to be encrypted/decrypted:
    message = input('Enter message:- ')

    # Whether the program encrypts or decrypts:
    mode1 = int(input("Enter '0' to encryt and '1' to decrypt your message:- "))

    # warning message
    if mode1==0:
        mode='encrypt'
        print("please remember key it also used when you want to decrypt your message")
    elif mode1==1:
        mode='decrypt'

    # The encryption/decryption key:
    key = int(input(f'Enter key for {mode}ion:- '))

    # Every possible symbol that can be encrypted:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    # Stores the encrypted/decrypted form of the message:
    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            # Handle wrap-around, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Output the translated string:
    print(translated)

except:
    print("..........incorrect input...........")
    print("........Run this code again ........")
