from django.utils import six

from rest_framework import serializers
from rest_framework.exceptions import ParseError

from taggit.utils import edit_string_for_tags, parse_tags

class TaggitSerializer(serializers.WritableField):
    def from_native(self, obj):
        try:
            return parse_tags(obj)
        except ValueError:
            raise ParseError(_("Please provide a comma-separated list of tags."))


    def to_native(self, obj):
        if obj is not None and not isinstance(obj, six.string_types):
            obj = edit_string_for_tags(obj.all())
        return obj