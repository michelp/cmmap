import tempfile
import cmmap
from multiprocessing import Process


def test_file():
    fd, filename = tempfile.mkstemp()
    f = open(filename, 'w')
    data = 'foobarbing'
    f.write(data)
    f.close()
    f = open(filename, 'r+')
    m = cmmap.mmap(prot=cmmap.PROT_READ, length=len(data), flags=cmmap.MAP_SHARED, fd=f.fileno())
    assert m[:] == data


def test_anonymous_private():
    data = 'foobarding'
    m = cmmap.mmap(length=10, 
                   prot=cmmap.PROT_READ|cmmap.PROT_WRITE,
                   flags=cmmap.MAP_ANONYMOUS|cmmap.MAP_PRIVATE)
    m[:] = data
    assert m[:] == data


def test_anonymous_shared():
    data = 'foobarding'
    m = cmmap.mmap(length=10, 
                   prot=cmmap.PROT_READ|cmmap.PROT_WRITE,
                   flags=cmmap.MAP_ANONYMOUS|cmmap.MAP_SHARED)
    m[:] = data
    assert m[:] == data
    def f():
        assert m[:] == data
        m[0] = 'd'
    proc = Process(target=f)
    proc.start()
    proc.join()
    assert m[:] == 'doobarding'

def test_anonymous_private():
    data = 'foobarding'
    m = cmmap.mmap(length=10, 
                   prot=cmmap.PROT_READ|cmmap.PROT_WRITE,
                   flags=cmmap.MAP_ANONYMOUS|cmmap.MAP_PRIVATE,
                   buffer=False)
    m[:] = data
    assert m[:] == data
