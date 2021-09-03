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



