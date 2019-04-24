def decrypt():
    # For improved efficiency, repalce ciphertext with the encoded word as a string.
    ciphertext = input('Please enter the encoded word.')
    shift = int(input('Please enter its shift value: '))
    space = []

    # create a list of encrypted words.
    ciphertext = ciphertext.split()

    # creat a list to hold decrypted words.
    sentence = []

    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)

    # join each word in the sentence list back together by a space.
    sentence = ' '.join(sentence)
    print('Decryption Successful\n')
    print('Your encrypted sentence is:', sentence)

decrypt()
