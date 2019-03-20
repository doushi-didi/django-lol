class ModelMixin:
    def to_dict(self, *exclude):
        attr_list={}
        for field in self._meta.fields:
            name = field.attname
            if name not in exclude:
                attr_list[name] = getattr(self, name)
        return attr_list
