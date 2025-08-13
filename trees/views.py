from django.shortcuts import render

from trees.models import MenuItem

# Create your views here.

class MenuNode:
    """Menu node for render
    """
    name: str = ''
    has_childs: bool = False
    childs: list
    ref_name: str = ''
    is_active: bool = False

    def __init__(self, name, is_active = False) -> None:
        self.name = name
        self.childs = []
        self.is_active = is_active


def recursive_items_create(item: MenuItem, name_list: list, ref_name: str = ''):
    """Recursivly creating menu items

    Args:
        item (MenuItem): current menu item
        name_list (list): list of url names in menu
        ref_name (str, optional): referal name for href in button. Defaults to ''.

    Returns:
        MenuNode: current menu node
    """
    node = MenuNode(item.name)
    node.ref_name += ref_name + '/' + item.name
    if len(name_list) and item.name == name_list[0]:
        print(name_list)
        node.is_active = True
        for child_item in item.childs.all():
            node.has_childs = True
            node.childs.append(recursive_items_create(child_item, name_list[1:], node.ref_name))
    return node


def index(request, url: str = ''):
    """Create menu

    Args:
        request (_type_): http request
        p (str, optional): url given to current menu node. Defaults to ''.

    Returns:
        _type_: menu node template
    """
    lst =  url.lstrip('/').split('/')
    context = {'item': MenuNode('Home', True)}
    root_items = MenuItem.objects.filter(parent=None).all()
    for item in root_items:
        context['item'].has_childs = True
        context['item'].childs.append(recursive_items_create(item, lst))
    return render(request, 'menu_template.html', context)
