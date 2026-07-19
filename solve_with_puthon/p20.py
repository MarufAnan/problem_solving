# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield


class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate(self):
        for i in range(0, self.n, 7):
            yield i

obj = DivisibleBySeven(100)

for num in obj.generate():
    print(num)