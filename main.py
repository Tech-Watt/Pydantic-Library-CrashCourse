"""
Pydantic is a Python library primarily used for data validation and settings management.

Key aspects of Pydantic include:

Data Validation:
Pydantic enforces data types and constraints based on type hints defined in Python classes, 
automatically validating data upon model instantiation. 
This helps catch data errors early, preventing issues in applications.

Serialization and Deserialization:
Pydantic models can be easily converted to and from common data 
formats like JSON, making it suitable 
for handling data from APIs or other external sources.

Settings Management:
Pydantic can be used to manage application settings, allowing for type-safe 
configuration and validation of environment variables or configuration files.

Performance:
Pydantic is known for its speed, with core validation logic often 
implemented in Rust for optimal performance.

"""



# Data Validation Example
from pydantic import BaseModel
import json

class User(BaseModel):
    id: int
    name: str
    age: int

# # # Example of creating a User instance with valid data
# valid_user = User(id=1, name="John Doe", age=30)
# print(valid_user)


# # Example of creating a User instance with invalid data
# # invalid_user = User(id="invalid", name="Jane Doe", age="invalid")  # This will raise a validation error
# # print(invalid_user)  # Uncommenting this line will raise a validation error because
# # print(invalid_user)  # This will raise a validation error because id is not an int




# Serialization and Deserialization Example
'''
Serialization – Converting data structures or objects into a format 
that can be stored (e.g. JSON, XML, or binary) and later reconstructed.
'''


user_one = User(id=2, name="Jane Doe", age=25)
print(user_one)

# Convert User model to JSON
data_s = user_one.model_dump_json()
print(f'from pydantic to json: {data_s}')


# Deserialization – The process of converting serialized data back into a usable format,
# such as reconstructing an object from its serialized form.

# Convert JSON back to User model
data_d = User.model_validate_json(data_s)
print(f'from json to pydantic format: {data_d}')

# Example of unpacking a dictionary into a Pydantic model
# This is useful when you have data in dictionary format and want to create a Pydantic model instance from it.

json_data = '{"id": 3, "name": "Alice Smith", "age": 28}'
parse_json = json.loads(json_data)
print(f'data: {parse_json}')


# Create a User model instance from the dictionary
json_to_model = User(**parse_json) # Unpacking the dictionary into the User model
print(f'user_3: {json_to_model}')




# Settings Management Example
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    key: str
    name : str
    id : str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = True
        

keys = Settings()
print(keys.key)
print(keys.name)
print(keys.id)