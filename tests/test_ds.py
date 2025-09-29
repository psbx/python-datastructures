from ds import Stack, Queue

def test_stack():
    s = Stack(); s.push(1); s.push(2)
    assert s.pop() == 2 and s.peek() == 1

def test_queue():
    q = Queue()
    for i in range(5): q.push(i)
    out = [q.pop() for _ in range(5)]
    assert out == [0,1,2,3,4]
