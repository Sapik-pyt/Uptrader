def filter_post_id_list(parent, main_post: list, filter_post_id: list):
    """
    Функция вовзращает список id "родителей".
    """
    lst_id_post = []
    while parent:
        lst_id_post.append(parent.id)
        parent = parent.parent
    else:
        for post in main_post:
            if post['id'] == filter_post_id:
                lst_id_post.append(filter_post_id)
    return lst_id_post


def child(posts_values: dict, cur_id: int, filter_posts_id_list: list):
    """
    Функция возвращает список "детей" - вложенные элементы в меню.
    """
    lst_post = [item for item in posts_values.filter(parent_id=cur_id)]
    for post in lst_post:
        if post['id'] in filter_posts_id_list:
            post['childrens'] = child(
                posts_values,
                post['id'],
                filter_posts_id_list
            )
    return lst_post


def additional_menu(context, menu: str, querystring_args: list):
    """
    Получение дополнительного меню,
    для выводы нескольких меню на одной странице.
    """
    for key_menu in context['request'].GET:
        if key_menu != menu:
            querystring_args.append(
                key_menu + '=' + context['request'].GET[key_menu]
            )
    query = ('&').join(querystring_args)
    return query
