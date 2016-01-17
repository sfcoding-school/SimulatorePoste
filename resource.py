import simpy


class TagliaCode(simpy.Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []

    def request(self, *args, **kwargs):
        self.data.append(("req", self._env.now, len(self.queue)))
        return super().request(*args, **kwargs)

    def release(self, *args, **kwargs):
        # self.data.append(("rel", self._env.now, len(self.queue)))
        return super().release(*args, **kwargs)


class SportelloPensioniC(simpy.Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []

    def request(self, *args, **kwargs):
        self.data.append(("req", self._env.now, len(self.queue)))
        return super().request(*args, **kwargs)

    def release(self, *args, **kwargs):
        # self.data.append(("rel", self._env.now, len(self.queue)))
        return super().release(*args, **kwargs)


class SportelloPacchiC(simpy.Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []

    def request(self, *args, **kwargs):
        self.data.append(("req", self._env.now, len(self.queue)))
        return super().request(*args, **kwargs)

    def release(self, *args, **kwargs):
        # self.data.append(("rel", self._env.now, len(self.queue)))
        return super().release(*args, **kwargs)
