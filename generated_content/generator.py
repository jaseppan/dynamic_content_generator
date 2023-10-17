import re
from generated_content.methods import faker_methods_dict

def generated_content(input_string):
    generated_string = input_string

    # Define a regular expression pattern to match keywords
    pattern = r'%(\w+)'

    # Find all matches of the pattern in the input_string
    matches = re.findall(pattern, input_string)

    for match in matches:
        if match in faker_methods_dict:
            # Call the corresponding Faker method and replace the keyword in the input string
            replacement = str(faker_methods_dict[match]())
            generated_string = generated_string.replace(f"%{match}", replacement)

    return generated_string

def main():
    string = "%name lives in %city, %country and works at %company as a %job."
    print(generated_content(string))

if __name__ == "__main__":
    main()