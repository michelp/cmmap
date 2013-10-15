import tempfile
import cmmap


def test_file():
    fd, filename = tempfile.mkstemp()
    f = open(filename, 'w')
    data = 'foobarbing'
    f.write(data)
    f.close()
    f = open(filename, 'r+')
    m = cmmap.mmap(prot=cmmap.PROT_READ, length=len(data), flags=cmmap.MAP_SHARED, fd=f.fileno())
    assert m[:] == data


def test_anonymous():
    data = 'foobarding'
    m = cmmap.mmap(prot=cmmap.PROT_READ|cmmap.PROT_WRITE,
                   length=10, 
                   flags=cmmap.MAP_ANONYMOUS|cmmap.MAP_PRIVATE)
    m[:] = data
    assert m[:] == data

