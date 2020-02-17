import tempfile

# NamedTemporaryFile: This function operates exactly as TemporaryFile() does, except that the file is guaranteed to have a visible name in the file system.
# https://docs.python.org/3/library/tempfile.html

# create a temporary file and write some data to it
fp = tempfile.NamedTemporaryFile()
fp.write(b'Hello world!')
# read data from file
fp.seek(0)
fp.read()
# close the file, it will be removed
fp.close()

# create a temporary file using a context manager
with tempfile.NamedTemporaryFile() as fp:
	fp.write(b'Hello world!')
	fp.seek(0)
	fp.read()