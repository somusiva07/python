# make properties private by using a double underscore __ prefix
# protected properties using a single underscore _ prefix
class Fruit:
    def __init__(self, color, shape):
        self.color = color
        self.__shape = shape

    def get_shape(self):
        return self.__shape

    def set_shape(self, shape):
        self.__shape = shape

mango = Fruit('Yellow', 'irregular')
print(mango.color)
# print(mango.__shape) ## throw error

print(mango.get_shape()) 

lemon = Fruit('Yellow', 'round')
print(lemon.color)
lemon.set_shape('round')
print(lemon.get_shape())