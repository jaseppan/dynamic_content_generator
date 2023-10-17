from faker import Faker

fake = Faker()

# Define a dictionary mapping keywords to Faker methods
faker_methods_dict = {
    "word": fake.word,
    "int": fake.random_int,
    "float": fake.pyfloat,
    "text": fake.text,
    "name": fake.name,
    "email": fake.email,
    "address": fake.address,
    "date": fake.date_of_birth,
    "phone": fake.phone_number,
    "city": fake.city,
    "country": fake.country,
    "zipcode": fake.zipcode,
    "company": fake.company,
    "job": fake.job,
    "ssn": fake.ssn,
    "locale": fake.locale,
    "currency": fake.currency_code,
    "url": fake.url,
    "uuid": fake.uuid4,
    "user_agent": fake.user_agent,
    # Add more here as needed
}
