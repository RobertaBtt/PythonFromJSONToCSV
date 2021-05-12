from dataclasses import dataclass

# A Value Object is any domain object that is uniquely
# identified by the data it holds.


@dataclass
class Todo():
    id: int
    userId: int
    title: str
    completed: bool
