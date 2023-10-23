from typing import Any


class Field:
    def __init__(self) -> None:
        self._list = {}
    
    
    def __getitem__(self, key):
        vkey = self._verification(key)
        return self._list.get(vkey)
    
    
    def __setitem__(self, key, value):
        vkey = self._verification(key)
        self._list[vkey] = value
    
    
    def __delitem__(self, key):
        self._list.pop(self._verification(key), None)

    
    def __contains__(self, key):
        return self._verification(key) in self._list
    
    
    def __iter__(self):
        return iter(self._list.values())
    
    
    def __getattr__(self, key):
        vkey = self._verification(key)
        return self[vkey]
    
    
    def __setattr__(self, key, value):
        try:
            vkey = self._verification(key)
            self[vkey] = value
        except:
            if type(key) is str:
                super().__setattr__(key, value)
            else:
                raise TypeError


    def __delattr__(self, key):
        if key in self.__dict__:
            super().__delattr__(key)
        else:
            vkey = self._verification(key)
            del self[key]
            
    
    @staticmethod
    def _verification(keys: str | tuple):
        char, num = None, None
        if type(keys) is str:
            if keys[0].isalpha() and keys[1:].isdigit():
                char, num = keys[0].casefold(), int(keys[1:])
            elif keys[-1].isalpha() and keys[:-1].isdigit():
                char, num = keys[-1].casefold(), int(keys[:-1])
        elif type(keys) is tuple:
            if len(keys) != 2:
                raise ValueError
            for key in keys:
                if type(key) is int and num is None:
                    num = key
                elif type(key) is str:
                    if key.isdigit() and num is None:
                        num = int(key)
                    elif key.isalpha() and len(key) == 1 and char is None:
                        char = key.casefold()
        else:
            raise TypeError
        
        if char is None or num is None:
            raise ValueError
        
        return char, num


