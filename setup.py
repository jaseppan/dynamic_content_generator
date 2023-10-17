from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='dynamic_content_generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'faker',
        # other dependencies...
    ],
    # additional metadata
    author='Janne Seppänen',
    author_email='j.v.seppanen@gmail.com',
    description='A module to generate dynamic content based on specific patterns',
    keywords='faker content generator',
    url='https://github.com/jaseppan/dynamic_content_generator',
)
