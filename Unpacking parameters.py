def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [7, 'string', False]
values_dict = {'a': 7, 'b': 'string', 'c': 365}


def fun(a, b, c = 1):
    print(a, b, c)


fun(*values_list)
fun(**values_dict)

values_list2 = ['world', True]
def fun2(a, b, c=5):
    print(a, b, c)

fun2(*values_list2)