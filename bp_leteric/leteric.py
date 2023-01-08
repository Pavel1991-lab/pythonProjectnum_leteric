import string
from flask import Blueprint
import random

all_letters = list(string.ascii_lowercase)

leteric = Blueprint('leteric', __name__)


@leteric.get('/random')
def paige_random():
    return random.choice(all_letters)
