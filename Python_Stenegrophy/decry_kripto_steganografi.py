from cryptosteganography import CryptoSteganography

crypto_steganography = CryptoSteganography('My secret password key')

secret = crypto_steganography.retrieve('output_image_file.png')

print(secret)
