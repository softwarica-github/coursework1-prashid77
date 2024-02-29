import unittest
from tkinter import Tk
from PIL import Image
from io import BytesIO
from steg import ImageSteganographyApp  # Adjusted import statement

class TestImageSteganographyApp(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = ImageSteganographyApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_encode_decode_workflow(self):
        # Create a test image
        test_image = Image.new("RGB", (100, 100), "white")

        # Test encoding and decoding workflow
        original_message = "This is a test message for steganography."
        encoded_image_stream = BytesIO()
        test_image.save(encoded_image_stream, format="PNG")
        encoded_image_stream.seek(0)
        self.app.encode_enc(test_image, original_message)

        # Decode the message from the encoded image
        decoded_message = self.app.decode(test_image)

        # Assert that the decoded message matches the original
        self.assertEqual(decoded_message, original_message)
        
        


if __name__ == '__main__':
    unittest.main()

