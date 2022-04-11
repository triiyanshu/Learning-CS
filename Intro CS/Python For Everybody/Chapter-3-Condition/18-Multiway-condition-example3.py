x = int(input('put the value of x : '))
if x < 2:
    print('tiny')
# elif x > 3:
#     print('what is this')
elif x < 10:
    print('small')
elif x < 20:
    print('medium')
elif x < 50:
    print('large')
elif x < 100:
    print('huge')