

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity

# '''
# Fill this in.
# '''


def hash(string, max):
    hash = 5381
    for i in string:
        hash = ((hash << 5) + hash) + ord(i)

    return hash % max

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''


def hash_table_insert(hash_table, key, value):
    i = hash(key, hash_table.capacity)

    if hash_table.storage[i] is not None:
        print("Overwriting a value")
        return None
    else:
        hash_table.storage[i] = value


# '''
# Fill this in.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        print('No value at that index')
        return None
    hash_table.storage[index] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is None:
        print('Key not found')
        return None
    else:
        return hash_table.storage[index]


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()


# Test Terminal returns

# python3 b_hashtables_tests.py
# Key not found
# ...gone tomorrow (success!)
# ..Key not found
# .Key not found
# .
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s

# OK
