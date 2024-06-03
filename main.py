from MorseCodeConverter import MorseCodeConverter as MC


converter = MC()

word_to_encrypt = input("Provide a message you want to decrypt to Morse Code: ")
decrypted_message = converter.decrypt(word_to_encrypt)
print(decrypted_message)
