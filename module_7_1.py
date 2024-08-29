import os.path


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        s = f'{self.name}, {self.weight}, {self.category}'
        return s


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        if os.path.exists(self.__file_name):
            file = open(self.__file_name, 'r')
            text = file.read()
            file.close()
        else:
            text = ''
        return text

    def add(self, *products):
        text = self.get_products()
        for product in products:
            if not (product.name in text):
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                file.close()
            else:
                print(f'Продукт {product} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)
print(s1.get_products())
