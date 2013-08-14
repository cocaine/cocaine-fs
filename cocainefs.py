#!/usr/bin/env python

import cocaine.services, routes, routefs

class CocaineFS(routefs.RouteFS):
    def __init__(self, *args, **kwargs):
        super(CocaineFS, self).__init__(*args, **kwargs)

        # Initialize the Storage Service connection
        self.storage = cocaine.services.Service('storage')

    def make_map(self):
        result = routes.Mapper()

        result.connect('/', controller = 'namespaces')
        result.connect('/{namespace}', controller = 'keys')
        result.connect('/{namespace}/{key}', controller = 'read')

        return result

    def namespaces(self, **kwargs):
        return list(self.storage.find('system', ['public', 'namespace']).get())

    def keys(self, namespace, **kwargs):
        return list(self.storage.find(namespace, ['public']).get())

    def read(self, namespace, key, **kwargs):
        return str(self.storage.read(namespace, key).get())

if __name__ == "__main__":
    routefs.main(CocaineFS)
