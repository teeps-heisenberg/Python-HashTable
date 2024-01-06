from hash_table import HashTable
my_hash_table = HashTable()
my_hash_table.print_table()

my_hash_table.set_item("bolts",1400)
my_hash_table.set_item("washers",50)
my_hash_table.set_item("lumber",70)

my_hash_table.print_table()

result = my_hash_table.get_item('washers')
print(result)

allKeys = my_hash_table.keys()
print(allKeys)