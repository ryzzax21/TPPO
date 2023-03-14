import sys


def add_node(tree: dict, node: dict, ancestors: list | str):
    if ancestors:
        for ancestor in ancestors:
            if tree['name'] == ancestor and node not in tree['children']:
                tree['children'].append(node)
            else:
                for child in tree['children']:
                    # TODO: refactor cringe #1
                    tmp = [ancestor]
                    add_node(child, node, tmp)
    else:
        tree['children'].append(node)


def build_tree(data: list[str]) -> dict[str, list]:
    t = {'name': 'all-father', 'children': []}
    for i in data:
        if ':' in i:
            tmp = i.split(':')
            successor = tmp[0].rstrip()
            ancestors = tmp[1].split()
        else:
            successor = i.strip()
            ancestors = None
        node = {'name': successor, 'children': []}
        add_node(t, node, ancestors)
    return t


def print_tree(tree):
    if len(tree['children']) == 0:
        print(tree['name'])
    else:
        print(tree['name'])
        for child in tree['children']:
            print_tree(child)


def find_relative(tree: dict[str, list], name: str) -> dict[str, list]:
    if tree['name'] == name:
        return tree
    else:
        for child_tree in tree['children']:
            relative = find_relative(child_tree, name)
            if relative:
                return relative


def validate(val_str: str, tree) -> bool:
    """
    Checks if p is ancestor of c is equal to result
    """
    ancestor, successor, result = val_str.split(' ')
    # Cyrillic booleans
    match result:
        case 'Да':
            result = True
        case 'Нет':
            result = False
    # Finding if ancestor exists
    parent_tree = find_relative(tree, ancestor)
    # Finding if successor is relative of ancestor
    is_successor = True if find_relative(
        parent_tree, successor) is not None else False
    if is_successor == result:
        print('Проверка прошла успешно')
        return True
    else:
        print(f'Ошибка в отношении: {ancestor} предок {successor}', file=sys.stderr)
        return False


def main():
    with open('input', 'r', encoding='utf8') as f:
        contents = f.read().strip().split('\n')
    n = int(contents[0])
    # Family members and their relations
    data = [i for i in contents[1:n + 1]]
    validations = [i for i in contents[n + 2:]]
    tree = build_tree(data)
    for validation in validations:
        validate(validation, tree)


if __name__ == '__main__':
    main()
