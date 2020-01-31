from django.http import HttpResponse
#from django.utils.html import escape, escapejs


class PopupReloadMixin(object):
    def response_add(self, request, obj, post_url_continue=None):
        #pk_value = obj._get_pk_val()
        if "_popup" in request.POST:
            return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body>'
                                '<script type="text/javascript">'
                                'opener.location.reload();'
                                ' this.close()</script></body></html>')  # % \
            # escape() calls force_text.
            #(escape(pk_value), escapejs(obj)))

        return super(PopupReloadMixin, self).response_add(request, obj, post_url_continue)
