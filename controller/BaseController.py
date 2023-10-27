from app import app


class ControllerMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        metacls.base_route = kwargs.get("base_route", "/")
        return dict()

    def __new__(cls, name, bases, attrs, *args, **kwargs):
        return super().__new__(cls, name, bases, attrs)


class BaseController(metaclass=ControllerMeta, base_route=""):
    @staticmethod
    def controllerRoute(rule, **kwargs):
        def wrapper(func):
            base_route = BaseController.base_route
            if BaseController.base_route == "/":
                base_route = ""
            endpoint = kwargs.pop("endpoint", None)
            app.add_url_rule(base_route + rule, endpoint, func, **kwargs)

            return func
        return wrapper
