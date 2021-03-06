import mmap
import shutil
import contextlib

# Copy the original file
shutil.copyfile('lorem.txt', 'lorem_copy.txt')

word = 'consectetuer'
reversed = word[::-1]

with open('lorem_copy.txt', 'r+') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0,
                                      access=mmap.ACCESS_COPY)) as m:
        print 'Memory Before:', m.readline().rstrip()
        print 'File Before:', f.readline().rstrip()
        print

        m.seek(0)  # rewind
        loc = m.find(word)
        m[loc:loc + len(word)] = reversed

        m.seek(0)  # rewind
        print 'Memory After:', m.readline().rstrip()

        f.seek(0)
        print 'File After :', f.readline().rstrip()
