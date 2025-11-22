import math
from math import sin, cos
# from math import *
import random as rnd
import json
import os
import sys

def math_usages():
    print(f'Square Root using math.sqrt(n): {math.sqrt(3)}')
    print(f'Constants (pi) using math.pi: {math.pi}')

def random_usages():
    print(f'Random integer using randint(1, 10): {rnd.randint(1, 10)}')

def specific_import_usages():
    print(f'Specific imports using "from math import sin, cos": sin(90){sin(90)}, cos(90): {cos(90)}')
    print('We can import everything as well using "from math import *"')

def json_usages():
    data = { "name": "John", "age": 21 }
    json_str = json.dumps(data)
    print(f'Dictionary to json using "json.dumps(data)": {json_str}')
    parsed_dict = json.loads(json_str)
    print(f'json to Dictionary using "json.loads(json_str)": {parsed_dict}')

def os_usages():
    print(f'Current working directory using "os.getcwd()": {os.getcwd()}')
    print(f'LIst the files in cirrent directory using "os.listdir()": {os.listdir()}')

def sys_usages():
    print(f'Python path list using sys.path: {sys.path}')
    print(f'Python version using sys.version: {sys.version}')