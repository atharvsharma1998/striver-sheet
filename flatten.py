# recursive approach
def flatten(*args):
    result = []

    for arg in args:
        if isinstance(arg, (list, tuple)):
            result.extend(flatten(*arg))
        else:
            result.append(arg)

    return result

# iterative approach
def flatten(*args):
    result = []
    stack = list(args)

    while stack:
        item = stack.pop()
        if isinstance(item, (list, tuple)):
            stack.extend(item)
        else:
            result.append(item)

    return result[::-1]