import sys
def val(tree, i):
    if i < len(tree) and tree[i] != 'None':
        return int(tree[i])
    return None
def righttree(tree, num, min, max):
    if val(tree, num) is None:
        return True
    value = val(tree, num)
    if not (min < value < max):
        return False
    left = righttree(tree, 2 * num + 1, min, value)
    right = righttree(tree, 2 * num + 2, value, max)
    return left and right
tree = input().split()
if tree[0] == 'None':
    print('YES')
    sys.exit()
if righttree(tree, 0, float('-inf'), float('inf')):
    print('YES')
else:
    print('NO')