import tempfile
import cmmap

def test():
    fd, filename = tempfile.mkstemp()
    f = open(filename, 'w')
    f.write('foobarbing')
    f.close()
    f = open(filename, 'r+')
    m = cmmap.mmap(prot=cmmap.PROT_READ, length=10, flags=cmmap.MAP_SHARED, fd=f.fileno())
    assert cmmap.ffi.buffer(m)[:] == 'foobarding'
