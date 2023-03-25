from .models import Menu


def get_tree(menu: Menu, prev: Menu = None, prev_tree=None):

    tree = []

    cur = []
    if menu.parent:
        for child in menu.parent.children.all():
            print(menu.parent)
            if child == prev:
                cur.append(prev_tree)
            else:
                cur.append(child)
        tree.append(get_tree(menu.parent, prev=menu, prev_tree=cur))

    return tree
