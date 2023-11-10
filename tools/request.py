import functools

from flask import request, Response


def required_payload(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*a, **k):
            json = request.get_json()
            check = [arg in json for arg in args]
            if all(check):
                return func(tuple([json[arg] for arg in args]), *k.values())
            else:
                raise Exception("Payload doesnt exist")

        return wrapper

    return decorator


def error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            return Response(status=500, response=str(error))

    return wrapper
