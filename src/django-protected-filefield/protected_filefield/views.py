from django.http.response import HttpResponseNotFound
from django.views.static import serve


def private_serve(request, path, document_root=None, show_indexes=False):
    if not request.user.is_authenticated():
        return HttpResponseNotFound()
    return serve(request, path, document_root, show_indexes)
