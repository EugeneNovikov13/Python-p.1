# Аннотация типов

# price: int = 5
# title: str
#
#
# def indent_right(s: str, width: int) -> str:
#     return " " * (max(0, width - len(s))) + s
#
#
# class Book:
#     title: str
#     author: str
#
#     def __init__(self, title: str, author: str) -> None:
#         self.title = title
#         self.author = author
#
#
# b: Book = Book(title='Fahrenheit 451', author="Bradbury")

# ////////////////////////////////////////////////////////

from typing import Optional, Any, Union, List, Callable


# amount: int
# amount = None
#
# price: Optional[int]
# price = None

# ////////////////////////////////////////////////////////

# unknown_item: Any = 1
# print(unknown_item)
# print(unknown_item // 0)

# ////////////////////////////////////////////////////////

# def hundreds(x: Union[int, float]) -> int:
#     return (int(x) // 100) % 10
#
#
# hundreds(100.0)
# hundreds(100)
# hundreds('100')

# ////////////////////////////////////////////////////////

# titles: List[str] = ['hello', 'world']
#
# titles.append(100500)  #Expected type 'str' (matched generic type '_T'), got 'int' instead
#
# titles = ['hello', 2]  #
#
# items: List = ['hello', 1]

# ////////////////////////////////////////////////////////


# def nothing(a: int) -> None:
#     if a == 1:
#         return
#     elif a == 2:
#         return None
#     elif a == 3:
#         return ''  #Expected type 'None', got 'str' instead
#     else:
#         pass
#
#
# x = int(input('Enter string'))
# nothing(x)

# ////////////////////////////////////////////////////////

# def help() -> None:
#     print('Somebody')
#
#
# def render(num: int) -> str:
#     return str(num // 100)
#
#
# def app(helper: Callable[..., None], renderer: Callable[[int], str]):
#     helper()
#     num = 12334
#     print(renderer(num))
#
#
# app(help, render)
# app(help, help)  #Expected type '(int) -> str', got '() -> None' instead

# ////////////////////////////////////////////////////////

# def search(lst: List[int], el: int) -> int:
#     for i in lst:
#         if i == el:
#             return lst.index(el)
#     return -1
#
#
# print(search([1, 2, 3, 4, 5, 6], 5))

# ////////////////////////////////////////////////////////


# def search_nearest(lst: List[int], x: int) -> int:
#     nearest = lst[0]
#     for i in range(1, len(lst)):
#         if abs(nearest - x) > abs(lst[i] - x):
#             nearest = lst[i]
#     return nearest
#
#
# print(search_nearest([1, 3, 2, 9, -5, 4, 0], -3))
# ////////////////////////////////////////////////////////
# Бинарный поиск
def binary_search(lst: List[int], val: int) -> int:
    first: int = 0
    last: int = len(lst) - 1
    index: int = -1
    while first <= last and index == -1:
        mid = (first + last) // 2
        if lst[mid] == val:
            index = mid
        else:
            if val < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index
# ////////////////////////////////////////////////////////


def binary_search_rec(lst: List[int], val: int) -> int:
    first = 0
    last = len(lst)-1
    if (first + last) // 2 == val:
        return lst.index(val)
    else:
        if val < (first + last) // 2:
            last = lst.index(val) - 1
        else:
            first = lst.index(val) + 1
        binary_search_rec(lst[first:last], val)


print(binary_search_rec([10,20,30,40,50], 20))

