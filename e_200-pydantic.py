from pydantic import BaseModel


class Coder(BaseModel):
    name: str
    dob: str


coder = Coder(name="Jake", dob="1990-12-20")
print(coder)

# Access individual fields
print(coder.name)  # Alice
print(coder.dob)  # 1990-12-20

# Convert to dictionary
print(coder.model_dump())
# Output: {'name': 'Alice', 'dob': '1990-12-20'}

# Errors
# coder2 = Coder(name="Bob")
# coder2 = Coder(name=123, dob="1990-12-20")
