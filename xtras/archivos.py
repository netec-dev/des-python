# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# 7.2. Reading and Writing Files
# open() returns a file object, and is most commonly used with two arguments: open(filename, mode).
f = open('workfile', 'w')
# The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

# Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding. If encoding is not specified, the default is platform dependent (see open()). 'b' appended to the mode opens the file in binary mode: now the data is read and written in the form of bytes objects. This mode should be used for all files that don’t contain text.

# In text mode, the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to just \n. When writing in text mode, the default is to convert occurrences of \n back to platform-specific line endings. This behind-the-scenes modification to file data is fine for text files, but will corrupt binary data like that in JPEG or EXE files. Be very careful to use binary mode when reading and writing such files.

# It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:
with open('workfile') as f:
    read_data = f.read()
# We can check that the file has been automatically closed.
print(f.closed) # True
# If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it. If you don’t explicitly close a file, Python’s garbage collector will eventually destroy the object and close the open file for you, but the file may stay open for a while. Another risk is that different Python implementations will do this clean-up at different times.

# After a file object is closed, either by a with statement or by calling f.close(), attempts to use the file object will automatically fail.
f.close()
f.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.
##
# 7.2.1. Methods of File Objects
# The rest of the examples in this section will assume that a file object called f has already been created.

# To read a file’s contents, call f.read(size), which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode). size is an optional numeric argument. When size is omitted or negative, the entire contents of the file will be read and returned; it’s your problem if the file is twice as large as your machine’s memory. Otherwise, at most size characters (in text mode) or size bytes (in binary mode) are read and returned. If the end of the file has been reached, f.read() will return an empty string ('').
print(f.read()) # 'This is the entire file.\n'
print(f.read()) # ''

# f.readline()
# reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. This makes the return value unambiguous; if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.
print(f.readline()) # 'This is the first line of the file.\n'
print(f.readline()) # 'Second line of the file\n'
print(f.readline()) # ''

# For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:
for line in f:
    print(line, end='')
# This is the first line of the file.
# Second line of the file

# If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

# f.write(string) writes the contents of string to the file, returning the number of characters written.
print(f.write('This is a test\n')) # 15

# Other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode) – before writing them:
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
print(f.write(s)) # 18

# f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.
# To change the file object’s position, use f.seek(offset, whence). The position is computed from adding offset to a reference point; the reference point is selected by the whence argument. A whence value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. whence can be omitted and defaults to 0, using the beginning of the file as the reference point.

f = open('workfile', 'rb+')
print(f.write(b'0123456789abcdef')) # 16

# Go to the 6th byte in the file
f.seek(5) # 5
print(f.read(1)) # b'5'

# Go to the 3rd byte before the end
print(f.seek(-3, 2)) # 13
print(f.read(1)) # b'd'

# In text files (those opened without a b in the mode string), only seeks relative to the beginning of the file are allowed (the exception being seeking to the very file end with seek(0, 2)) and the only valid offset values are those returned from the f.tell(), or zero. Any other offset value produces undefined behaviour.

# File objects have some additional methods, such as isatty() and truncate() which are less frequently used; consult the Library Reference for a complete guide to file objects.