# Заголовок
## Подзаголовок

**жииииирный текст**
*курсив*

ссылка: [Github](https://github.com)

$$
x^2 = x * x
$$

![Picture](imgs/4.png)


# Этапы выполнения

## 1) Создание интерфейса с помощью Qt creator

![Untitled](imgs/back)

> Перед вами стартовое окно. При открытии программы пользователь видит следующие виджеты:
> 
- Name of image:	поле для ввода и кнопка Load. Сюда пользователь вводит имя файла и	путь к нему и нажимает кнопку для загрузки изображения.
- High of surface и Width of surface: два поля для ввода размеров основной поверхности
- Color of surface: Кнопки, меняющие цвет основной поверхности (изначально – «Green»)
- Quantity:	поле для ввода числа: количества дублирований заданного изображения	на основной поверхности

## 2) Загрузка изображения. Подсчет площади фигуры на изображении в пикселях

> В представленном фрагменте кода идет наложение фигуры на фон определенного цвета с помощью библиотеки Pillow. Далее идет подсчет количества пикселей, чей цвет не совпадает с фоновым. Количество пикселей и есть площадь фигуры.
> 

![Untitled](imgs/kod1)

## 3) Подсчет максимального количества фигур, которые можно разместить на основной поверхности

> Для расчёта используется формула:
> 

> $$
> \frac{Sповерхности}{S фигуры}
> $$
> 

## 4) Создание матриц для основной поверхности и для фигуры

> Матрицы создаются по принципу:
> 
1. Инициализация списка, включающего в себя вложенные	списки, количество которых = высоте поверхности или фигуры. В каждом вложенном списке содержатся «0»,	количество которых = ширине поверхности или фигуры. Так получается пока пустая	матрица.
2. Замена «0» на «1» в местах, где альфа канал пикселя > 0. По принципу, схожему с	тем, что использовался для подсчета	площади.

![Untitled](imgs/kod2)

> Перед вами фрагмент кода, отвечающий за заполнение единицами матрицы фигуры.
> 

> Если мы загрузим в программу следующее изображение:
> 

![Image.png](imgs/Image.png)

> То его матрица будет выглядеть так:
> 

![Untitled](imgs/im.png)

## 5) Размещение фигуры на основной поверхности с использованием циклов

> В цикле для размещения каждый раз заданная фигура должна получать две характеристики: угол поворота и кортеж с координатами.
> 

> Наиболее простым в реализации способом будет задание этих параметров с помощью методов рандома. После получения параметров в цикле, матрица фигуры меняется (если угол поворота неравен 0) и «накладывается» на основну. В процессе наложения «1» из матрицы фигуры копируются в матрицу основной поверхности с учетом заданных координат.
> 

> Ниже представлен фрагмент кода, в котором идет процесс наложения. Стоит также отметить, что автор предусмотрел возможность наложения фигур, поэтому при обнаружении таковых цикл переноса матрицы останавливается и начинается заново уже с другими параметрами поворота и координат.
> 

![Untitled](imgs/kod3.png)

> По завершению работы цикла программа выводит получившееся изображение, в котором количество фигур = максимально допустимому, определенном в начале:
> 

#картинка

# **Вывод**

> В работе автором была реализована программа, решающая задачу раскроя с произвольными фигурами, а так же реализована возможность пользователя самостоятельно задавать основные параметры для создания необходимого раскроя.
>