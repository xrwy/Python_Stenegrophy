from cryptosteganography import CryptoSteganography

crypto_steganography = CryptoSteganography('My secret password key')

# Save the encrypted file inside the image
crypto_steganography.hide('exampleImage.png', 'output_image_file.png', 'This text is hidden in the photo')

