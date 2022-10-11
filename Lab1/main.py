# -*- coding: utf-8 -*-

from cache import LRUCache

if __name__ == '__main__':

    cache = LRUCache(100)
    cache.set('Jesse', 'James')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'Pinkman')
    print(cache.get('Jesse'))  # вернёт 'Pinkman'
    cache.rem('Walter')
    print(cache.get('Walter'))  # вернёт 'not found!'