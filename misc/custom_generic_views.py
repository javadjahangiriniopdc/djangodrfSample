from rest_framework import mixins
from rest_framework.generics import GenericAPIView


class PartialUpdateAPIView(mixins.UpdateModelMixin, GenericAPIView):
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
