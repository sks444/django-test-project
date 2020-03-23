# from rest_framework import viewsets
# from rest_framework.views import APIView
# from .serializers import AuthorS
# from .models import Author


# class AutherV(APIView):
#     # queryset = 
#     serializer_class = AuthorS

#     def get_queryset(self):
#         return Author.objects.all()

#     def list(self, request, *args, **kwargs):
#         print("I am in the view")
#         queryset = self.get_queryset()
#         return queryset


from rest_framework import parsers
from rest_framework.views import APIView
from rest_framework.response import Response


class MyParser(parsers.BaseParser):
    media_type = 'application/x-www-form-urlencoded'

    def parse(self, stream, media_type=None, parser_context=None):
        import ipdb; ipdb.set_trace()
        raise AttributeError()
        # return stream.read()


class AutherV(APIView):
    parser_classes = [MyParser]

    def post(self, request):
        return Response(request.data)
