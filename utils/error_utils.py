import traceback

from flask import jsonify


class ErrorUtil:
    @staticmethod
    def __handle_traceback__():
        if traceback.format_exc().strip() != 'NoneType: None':
            traceback.print_exc()
            return True
        return False

    @classmethod
    def builder(cls):
        return ErrorUtilBuilder()

    @classmethod
    def bad_request(cls, msg='', errors=None):
        cls.__handle_traceback__()

        message = {
            'status': 400,
            'message': 'Bad Request: {}'.format(msg),
            'errors': errors if errors else [],
        }

        resp = jsonify(message)
        resp.status_code = 400

        return resp

    @classmethod
    def unauthorized(cls, msg='', errors=None):
        cls.__handle_traceback__()

        message = {
            'status': 401,
            'message': 'Unauthorized: {}'.format(msg),
            'errors': errors if errors else [],
        }

        resp = jsonify(message)
        resp.status_code = 401

        return resp

    @classmethod
    def not_found(cls, msg='', errors=None):
        cls.__handle_traceback__()

        message = {
            'status': 404,
            'message': 'Not Found: {}'.format(msg),
            'errors': errors if errors else [],
        }

        resp = jsonify(message)
        resp.status_code = 404

        return resp

    @classmethod
    def forbidden(cls, msg='', errors=None):
        cls.__handle_traceback__()

        message = {'status': 403, 'message': 'Forbidden: ' + msg, 'errors': errors if errors else []}

        resp = jsonify(message)
        resp.status_code = 403

        return resp

    @classmethod
    def conflict(cls, msg='', errors=None):
        cls.__handle_traceback__()

        message = {
            'status': 409,
            'message': 'Conflict: {}'.format(msg),
            'errors': errors if errors else [],
        }

        resp = jsonify(message)
        resp.status_code = 409

        return resp

    @classmethod
    def internal_error(cls, msg='', errors=None):
        cls.__handle_traceback__()

        message = {
            'status': 500,
            'message': 'Internal Error: {}'.format(msg),
            'errors': errors if errors else [],
        }

        resp = jsonify(message)
        resp.status_code = 500

        return resp


class ErrorUtilBuilder:
    def __init__(self):
        self.errors = []

    def append(self, _field, _message, _type):
        self.errors.append({'field': _field, 'message': _message, 'type': _type})

    def append_voluptuous(self, errors):
        self.errors.extend({
            "field": ".".join(list(map(str, error.path))),
            "message": error.error_message,
            "type": 'invalid',
        } for error in errors)

    def construct(self, msg='', error_func=ErrorUtil.bad_request):
        try:
            function = getattr(ErrorUtil, error_func.__name__)
        except Exception:
            raise AttributeError('method name {} is not in ErrorUtil'.format(error_func.__name__))

        if not callable(function) or any(x in error_func.__name__ for x in ('__', 'builder')):
            raise TypeError("Invalid error function passed to construct")

        return error_func(msg, self.errors)
