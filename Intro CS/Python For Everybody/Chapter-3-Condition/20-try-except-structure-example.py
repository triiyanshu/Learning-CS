this = 'hello bro'
try:
    that = int(this)
except:
    that = -1
print('First', that)

this = '123'
try:
    that = int(this)
except:
    that = -1
    
print('second', that)