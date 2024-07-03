from enum import Enum

class Gender(Enum):
  MALE=0
  FEMALE=1

# character can have
  # name
  # gender
  # age
  # weight
  # height
  # family
  # job
  # stats
    # temperment
    # skills

class Character: 

  def __init__(
      self,
      name: str,
      gender: Gender,
      age: int,
      weight: int, 
      height: int,
  ):
 
    if age <= 0 or 999 < age:
      raise Exception("cannot create a character with this age")
 
    self._age = age
    self._gender = gender
    self._name = name
    self._weight = weight
    self._height = height