import json
from functools import wraps

def to_json(func):
    @wraps(func)
    def wrapper(*argv, **kwarg):
        jsonForm = json.dumps(func())
        return jsonForm
    return wrapper

@to_json
def data():
    return 5

data(3, 4, 6)