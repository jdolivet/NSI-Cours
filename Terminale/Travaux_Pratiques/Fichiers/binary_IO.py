#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'FIL - Faculté des Sciences et Technologies -  Univ. Lille <http://portail.fil.univ-lille1.fr>_'
__date_creation__ = 'Thu Jun  6 18:36:09 2019'
__doc__ = """
:mod:`binary_IO` module
:author: {:s} 
:creation date: {:s}
:last revision:

Provides two classes

- Reader : for reading bytes from a file
- Writer : for writing bytes in a file

>>> writer = Writer('foo')
>>> writer.write_bytes([100, 90, 32, 10])
4
>>> writer.close()
>>> reader = Reader('foo')
>>> reader.get_bytes(3)
[100, 90, 32]
>>> reader.get_bytes(3)
[10]
>>> reader.get_bytes(3)
[]
>>> reader.reset()
>>> reader.get_bytes(4)
[100, 90, 32, 10]
>>> reader.close()
>>> import os
>>> os.system('rm foo')
0
""".format(__author__, __date_creation__)

class BinaryIOError(Exception):
    '''
    Exception for Binary_IO classes
    '''
    def __init__(self, msg):
        self.message = msg
        
class Reader():
    '''
    a class for creating readers in binary files
    Reader objects have methods

    * close() : close the channel
    * reset() : reset the lecture at the beginning of the file
    * get_bytes(n) : gives a sequence of the (at most) n next bytes. If the number of bytes
         obtained is strictly less than n, the end of file is reached.
    '''
    def __init__(self, filename):
        try:
            self._instream = open(filename, 'rb')
        except FileNotFoundError:
            raise BinaryIOError('file {:s} not found'.format(filename))

    def close(self):
        self._instream.close()

    def reset(self):
        try:
            self._instream.seek(0)
        except ValueError:
            raise BinaryIOError('no possible reset on closed reader')
        
    def get_bytes(self, n=None):
        try:
            if n is None:
                read_bytes = self._instream.read()
            else:
                read_bytes = self._instream.read(n)
        except ValueError:
            raise BinaryIOError('no read operation possible on closed reader')
        return [byte for byte in read_bytes]

class Writer():
    '''
    a class for creating readers in binary files
    Reader objects have methods

    * close() : close the output channel
    * write_bytes(seq_of_bytes) : write the bytes of seq_of_bytes in the file. This method return 
           the number of bytes written in the file.
    '''
    def __init__(self, filename):
        try:
            self._outstream = open(filename, 'xb')
        except FileExistsError:
            if input('Le fichier {:s} existe. L\'écraser ? [O/N]'.format(filename)).upper() == 'O':
                self._outstream = open(filename, 'wb')
            else:
                raise BinaryIOError('file {:s} exists.'.format(filename))

    def write_bytes(self, seq_of_bytes):
        return self._outstream.write(bytes(byte for byte in seq_of_bytes))
        
    def close(self):
        self._outstream.close()

    
            
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)


