# -*- coding: utf-8 -*-

class Element:
    def __init__(self, value, key, prev, next) -> None:
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, value) -> None:
        self.next = value

    def set_prev(self, value) -> None:
        self.prev = value

        
class LRUCache:
    _DLLMap = {}
    first_item = None

    def __init__(self, capacity: int = 10) -> None:
        if capacity is None or not isinstance(capacity, int):
            raise TypeError('Expected maxsize to be an integer or None')
        self.capacity = capacity

    def add(self, key, value) -> None:
        n_item = self.first_item

        while True:
            if n_item.get_next() is None:
                break
            n_item = n_item.get_next()

        new_item = Element(value, key, n_item, None)
        self._DLLMap[key] = new_item
        n_item.set_next(new_item)

    def rem(self, key) -> None:
        if key not in self._DLLMap:
            print("ключ не найден")
            return

        current = self._DLLMap[key]
        prev = current.get_prev()
        next = current.get_next()

        if prev is None or next is None:

            if prev is None and next is None:
                self.first_item = None
            else:
                if prev is None:
                    next.set_prev(None)
                    self.first_item = next
                if next is None:
                    prev.set_next(None)
        else:
            prev.set_next(next)
            next.set_prev(prev)

        self._DLLMap.pop(key, None)

    def set(self, key, value) -> None:
        if self.first_item is None:
            self.first_item = Element(value, key, None, None)
            self._DLLMap[key] = self.first_item
        else:
            # Обновляем существующий и сдвигаем позицию в кэше
            if key in self._DLLMap:
                self._DLLMap[key].value = value
                self.rem(key)
                self.set(key, value)
                return

            # Достигнут лимит кеша
            if self.capacity <= len(self._DLLMap.keys()):
                self.rem(self.first_item.key)

            self.add(key, value)

    def get(self, key: str) -> str:
        if key not in self._DLLMap:
            return "not found!"
        return self._DLLMap[key].value