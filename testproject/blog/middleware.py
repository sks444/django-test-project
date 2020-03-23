class SimpleMiddleware1:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("something before view for middleware 1")

        response = self.get_response(request)

        print("something after view for middleware 1")

        # Code to be executed for each request/response after
        # the view is called.

        return response


class SimpleMiddleware2:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("something before view for middleware 2")

        response = self.get_response(request)

        print("something after view for middleware 2")

        # Code to be executed for each request/response after
        # the view is called.

        return response
