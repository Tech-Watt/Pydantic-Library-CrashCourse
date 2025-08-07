# Learn Pydantic

This project demonstrates how to use [Pydantic](https://docs.pydantic.dev/) for data validation and settings management in Python.

## Features

- Define data models using Python type hints
- Validate and parse data from various sources
- Handle nested and complex data structures
- Environment variable and settings management

## Getting Started

### Installation

```bash
uv init
uv add pydantic
uv add pydantic-settings
```

### Example Usage

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: str

user = User(id=1, name="Alice", age=90)
print(user)
```

## Project Structure

- `.env` — Contains dummy api keys
- `main.py` — Example usage and validation logic

## Resources

- [Pydantic Documentation](https://docs.pydantic.dev/)
- [FastAPI](https://fastapi.tiangolo.com/) (for web APIs with Pydantic)

---

Feel free to explore and modify the code to learn more about Pydantic!