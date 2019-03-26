class PermissionMap(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise ValueError("The permission already exists", value)
        super(PermissionMap, self).__setitem__(key, value)
