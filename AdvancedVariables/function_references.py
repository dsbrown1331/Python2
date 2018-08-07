def foo(bar):
    bar.append(42)
    print(bar)
    # >> [42]

def foo2(bar):
    bar = 'new value'
    print (bar)
    # >> 'new value'

#############
answer_list = []
foo(answer_list)
print(answer_list)

answer_list = 'old value'
foo2(answer_list)
print(answer_list)
