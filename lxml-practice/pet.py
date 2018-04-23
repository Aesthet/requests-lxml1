

class Pet:
    _ID = 0

    @property
    def id(self):
        self._ID += 1
        return self._ID
