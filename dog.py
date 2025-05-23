class dog:
    animal = 'dog'

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color


blu = dog('Golden Retriever', 'Golden')
woo = dog('Rotweiler', 'Black')

print('Golden Retriever is a {}'. format(blu.animal))
print('Rotweiler is also a {}'. format(woo.animal))

print('{} is {} in color'.format(blu.breed, blu.color))
print('{} is {} in color'.format(woo.breed, woo.color))
