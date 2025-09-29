class Stack:
    def __init__(self): self._s = []
    def push(self, x): self._s.append(x)
    def pop(self): return self._s.pop()
    def peek(self): return self._s[-1]
    def __len__(self): return len(self._s)

class Queue:
    def __init__(self): self._l = []; self._r = []
    def push(self, x): self._r.append(x)
    def pop(self):
        if not self._l:
            self._l = self._r[::-1]; self._r = []
        return self._l.pop()
    def __len__(self): return len(self._l) + len(self._r)
