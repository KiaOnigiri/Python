class Vector:
    MIN_COORD = 0
    MAX_COORD = 100
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD
res = Vector.validate(5)
print(res)
