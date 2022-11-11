import pytest
import sys
sys.path.append('C:/SEDS_LAB4/src/models')
from module import serve_beer

def test_serve_beer_legal():
  adult = 25
  assert serve_beer(adult) == "Have beer"
 
def test_serve_beer_illegal():
  child = 10
  assert serve_beer(child) == "No beer"