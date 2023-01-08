from flask import Blueprint
import random


numeric = Blueprint('numeric', __name__)
all_numbers = list(range(1,10+1))


@numeric.get('/random')
def paige_random():
    return str(random.choice(all_numbers))