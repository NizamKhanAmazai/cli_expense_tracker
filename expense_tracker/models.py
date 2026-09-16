from dataclasses import dataclass
from datetime import date 

@dataclass
class Expense:
    id: str
    amount: float
    category: str
    description: str
    date: date
