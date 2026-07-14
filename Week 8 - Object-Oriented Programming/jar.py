class Jar:
    def __init__(self, capacity=12):
        if isinstance(capacity, int) and capacity >= 0:
            self._capacity = capacity
            self.cookie = 0
        else:
            raise ValueError

    def __str__(self):

            return "🍪" * self.cookie

    def deposit(self, n):
        if self.cookie + n > self._capacity:
            raise ValueError
        self.cookie += n
    def withdraw(self, n):
        if n > self.cookie:
            raise ValueError
        self.cookie -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookie

