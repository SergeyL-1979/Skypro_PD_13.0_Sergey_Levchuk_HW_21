#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Storage(ABC): # Нужно ли сюда делать наследование от ABC?
    """
    Создайте абстрактный класс Storage
    **Поля:**
    `items` (словарь название:количество)
    `capacity` (целое число)
    **Методы:**
    `add`(<название>, <количество>)  - увеличивает запас items
    `remove`(<название>, <количество>) - уменьшает запас items
    `get_free_space()` - вернуть количество свободных мест
    `get_items()` - возвращает содержание склада в словаре {товар: количество}
    `get_unique_items_count()` - возвращает количество уникальных товаров.
    """
    @abstractmethod
    def add(self, name, qnt):
        pass

    @abstractmethod
    def remove(self, name, qnt):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
