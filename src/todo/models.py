from abc import ABCMeta
import uuid
from datetime import datetime

class Model(object):
  """
  Abstract base class for all models -
  all models should extend this class
  """
  __metaclass__ = ABCMeta

  def __init__(self):
    """
    Initializes the model with a Universal Unique
    Identifier as an id
    """

  def to_dict(self):
    """
    Dictionary representation of this Model
    """
    return vars(self)

# TODO - Add models here
class User(Model):
    """
    model class
    """
    def __init__(self, Name, Height, Weight, Age, Gender):
        Model.__init__(self)
        self.Name = Name
        self.Height = Height
        self.Weight = Weight
        self.Age = Age
        self.Gender = Gender


    def to_dict(self):
        return vars(self)