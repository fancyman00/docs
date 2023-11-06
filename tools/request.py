import functools

from flask import request, Response


def required_payload(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*a, **k):
            json = request.get_json()
            check = [arg in json for arg in args]
            if all(check):
                return func(tuple([json[arg] for arg in args]), **k)
            else:
                return Response(status=200, response="Payload doesnt exist")
        return wrapper

    return decorator
