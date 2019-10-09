from flask import Blueprint

api = Blueprint('api', __name__) # What on earth is blueprint

from app.api import ships, errors
