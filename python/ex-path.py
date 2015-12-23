
import os

# pwd
print os.getcwd()

# expand path
print os.path.abspath(os.path.expanduser('~/pwd/../'))

# check path exists
path = './dir1/dir2'
if os.path.exists(path):
    print '%s exists!'%(path)
else:
    os.makedirs('./dir1/dir2')
