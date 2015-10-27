#!/usr/bin/python

def print_title(title):
    print
    print '-' * 50
    print '=> {}'.format(title)
    print


print_title('new dictionary')
print dict(a=1, b=2)
print dict({'a': 1, 'b': 2})
print dict(zip(('a', 'b'), (1, 2)))
print dict([['b', 2], ['a', 1]])

print_title('map two list into dictionary')
key = ['Joe', 'Tom', 'Clare']
data = [128, 1024, 2048]
dict1 = dict(zip(key, data))
print dict1

# dictionary to list
print_title('get key list')
print dict1.keys()

print_title('get value list')
print dict1.values()

# iterate value
print_title('iterate all keys')
for k in dict1:
    print k

print_title('iterate all key, values')
for k, v in dict1.items():
    print '{}: {}'.format(k, v)

# sort
print_title('sorted key pair')
print sorted(dict1)

print_title('sorted dict tuple by key')
print sorted(dict1.items())

print_title('sorted dict tuple by value')
print sorted(dict1.items(), key=lambda x: x[1])

print_title('iterate by sorted key')
for k, v in sorted(dict1.items()):
    print '{}: {}'.format(k, v)

print_title('get value or return default value')
print dict1.get('Clare', 0)
print dict1.get('Mary', None)

print_title('set default value when key not existed')
print dict1.setdefault('Clare', 5)
print dict1
print dict1.setdefault('Mary', 5)
print dict1

print_title('update value or add new dict')
print dict1.update(dict(Clare=5))
print dict1
print dict1.update(dict(David=5))
print dict1
