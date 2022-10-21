Классы в Python
====

[ссылка на шпаргалку](https://texterra.ru/blog/ischerpyvayushchaya-shpargalka-po-sintaksisu-razmetki-markdown-na-zametku-avtoram-veb-razrabotchikam.html)

* Создание класса

    ```py
    class MyFirstClass(ParentClass):
        ...

        def __init__(self):
            ...
    ```

    >Этот класс не делает ничего конкретного, тем не менее, это очень хороший инструмент для изучения. Например, чтобы создать класс, мы используем ключевое слово `class`, за которым следует наименование класса. В Пайтоне, конвенция указывает на то, что наименование класса должно начинаться с заглавной буквы. Далее нам нужно открыть круглые скобки, за которыми следует слово `ParentClass` и закрытые скобки. `«ParentClass»` — то, на чем основан класс, или наследуется от него. Это называется базовым классом или родительским классом. Большая часть классов в Пайтоне основаны на объекте. У классов есть особый метод, под названием `__init__`.

    >Давайте немного расширим наше определение класса и дадим ему некоторые атрибуты и методы.

    ```py
        class MyFirstClass(ParentClass):
            pass
            def __init__(self):
                self.name = 'Author'
                self.color = 'red'
            
            def change_color(self, new_color):
                self.color = new_color
            
            def get_color(self):
                return self.color
    ```

    >Здесь мы добавили 2 метода и 2 атрибута. Метод `change_color` принимает аргумент `new_color`, после чего мы присваиваем атрибуту  `self.color` значение нового цвета. Метод же `get_color` возвращает значение атрибута `color`.
