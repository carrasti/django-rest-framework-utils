
class TaggitViewMixin(object):
    taggit_fields = ('tags',)

    def post_save(self, obj, *args,**kwargs):
        item = self.model.objects.get(pk=obj.pk)
        for tag_field in self.taggit_fields:
            if hasattr(obj, tag_field) and not getattr(obj, tag_field) is None and isinstance(getattr(obj, tag_field), list):
                getattr(item, tag_field).set(*getattr(obj, tag_field))
                setattr(obj, tag_field, getattr(item, tag_field))
        super(TaggitViewMixin, self).post_save(obj, *args, **kwargs)