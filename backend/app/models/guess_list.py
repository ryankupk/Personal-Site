
from pydantic import BaseModel
from typing import List, Dict

class GuessList(BaseModel):
    guess_list: Dict[str, str]