class TimeMap:
    time_map = dict()
    def add(self, name, time):
        self.time_map[name] = time

    def get(self, name):
        if name in self.time_map:
            return self.time_map[name]

    def clear(self, name):
        if name in self.time_map:
            self.time_map[name] = 0.0

    def clearAll(self):
        for e in self.time_map:
            self.time_map[e] = 0.0

    def delete(self, name):
        if name in self.time_map:
            self.time_map.pop(name)

    def deleteAll(self):
        for e in self.time_map:
            self.time_map.pop(e)

    def print(self):
        for e in self.time_map:
            print(e, self.time_map[e])

