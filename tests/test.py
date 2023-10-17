import unittest
from generated_content.generator import generated_content

class TestDynamicContentGenerator(unittest.TestCase):

    def setUp(self):
        """Set up anything that's necessary before each test."""
        pass

    def tearDown(self):
        """Clean up after each test if necessary."""
        pass

    def test_word_generation(self):
        content = generated_content("%word")
        print("Generated Word:", content) 
        self.assertNotEqual(content, "%word", "Word generation failed.")

    def test_int_generation(self):
        content = generated_content("%int")
        print("Generated Integer:", content) 
        self.assertNotEqual(content, "%int", "Integer generation failed.")
        self.assertTrue(content.isdigit(), "Generated content is not an integer.")

    def test_float_generation(self):
        content = generated_content("%float")
        print("Generated floating number:", content) 
        self.assertNotEqual(content, "%float", "Float generation failed.")
        try:
            float_val = float(content)
        except ValueError:
            self.fail("Generated content is not a valid float.")

    # Add other tests for each of the tags you're supporting.
    # ...

if __name__ == "__main__":
    unittest.main()
