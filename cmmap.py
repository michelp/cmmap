from cffi import FFI

ffi = FFI()
ffi.cdef("""
#define PROT_EXEC ...
#define PROT_READ ...
#define PROT_WRITE ...
#define PROT_NONE ...

#define MAP_SHARED ...
#define MAP_PRIVATE ...
#define MAP_ANONYMOUS ...
#define MAP_FIXED ...
#define MAP_GROWSDOWN ...
#define MAP_HUGETLB ...
#define MAP_LOCKED ...
#define MAP_NONBLOCK ...
#define MAP_NORESERVE ...
#define MAP_POPULATE ...
#define MAP_STACK ...

void *mmap(void *addr, size_t length, int prot, int flags, int fd, size_t offset);
""")

C = ffi.verify("""
#include <sys/mman.h>
""")


globals().update({n: getattr(C, n) for n in dir(C)})


def mmap(addr=ffi.NULL, length=0, prot=PROT_NONE, flags=MAP_PRIVATE, fd=0, offset=0):
    m = C.mmap(addr, length, prot, flags, fd, offset)
    if m == -1:
        return None
    return ffi.buffer(m, length)

