# Dynamic Content Generator

Version: 0.1.0

A Python module designed to generate dynamic content based on specific patterns using the Faker library. This tool can be seamlessly integrated into larger applications where randomized test data is required.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Testing](#testing)
4. [Integration](#integration)
5. [License](#license)

## Installation

### Via PyPI

You can install the `dynamic-content-generator` module directly from the Python Package Index using pip:

```bash
pip install dynamic-content-generator
```

### Via GitHub

Alternatively, you can also install the module directly from its GitHub repository:

1. Clone the repository:

```bash
git clone https://github.com/jaseppan/dynamic-content-generator.git
```
2. Navigate into the project directory:
```bash
cd dynamic_content_generator
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Dependencies

This module primarily depends on the Faker library.

- When you install via pip, the necessary dependencies, including Faker, will be automatically handled.
- If you are setting up the project manually via GitHub, make sure to install the dependencies using the requirements.txt file as mentioned above.

## Usage

Import the module and use the `generated_content` function:

```python
from generated_content.generator import generated_content

output = generated_content("%name lives in %city and loves %word.")
print(output)

This might produce an output like:
Jane Doe lives in Springfield and loves programming.
```

## Testing

To run the tests:
```bash
python3 -m unittest tests/test.py
```

## Integration

To use this as part of a larger application, simply import the module and integrate the generated_content function as needed. Make sure to adjust the Python path or package structure to accommodate the location of this module in your larger application.



## Adding More Data Generation Methods
To extend the set of data generation methods, update the generated_content/methods.py file by adding the desired key-method pairs to the faker_methods_dict.

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Ensure to update tests as appropriate.

## License
his project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file file.