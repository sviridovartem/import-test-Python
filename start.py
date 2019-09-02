from packA import a1
from packA import a2
from packA.subA import sa1
from packA.subA import sa2
from packB import b1
from packB import b2
from . import math as ma
from . import other
from . import random

from packA.a1 import a1_function

print(a1_function())
print(ma.math_function())
