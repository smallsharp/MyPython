def fn(y, *args, x=5):
    print('x={}, y={}'.format(x, y))
    print(args)


# fn()
fn(5)
# fn(x=6)  # TypeError: fn() missing 1 required positional argument: 'y'
fn(1, 2, 3, x=10)
# fn(y=17,2,3,x=10) # SyntaxError
fn(1, 2, y=3, x=10)  # TypeError: fn() got multiple values for argument 'y'
