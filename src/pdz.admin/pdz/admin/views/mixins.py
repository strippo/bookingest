class AdminObjectMixin(object):

    def get_object(self, queryset=None):
        return self.opts.get_object(self.request, self.kwargs['pk'])
