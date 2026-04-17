import json
import random

def numbersGenerate(amount):
    numbers = []
    
    for j in range(amount):
        numbers.append(random.randint(1 , 100))
            
    return numbers

with open("data.json" , "r") as f:
    data = json.load(f)
    
window = data["window"]
width = window["width"]
height = window["height"]

numbers = data["numbers"]
amount = numbers["amount"]
numbers = numbersGenerate(amount)

colors = data["colors"]
white = colors["white"]
black = colors["black"]
blue = colors["blue"]
green = colors["green"]

choices = data["choices"]
algo = data["algorithms"]