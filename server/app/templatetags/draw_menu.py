from django import template

from app.models import Post

from .draw_menu_func import additional_menu, child, filter_post_id_list

register = template.Library()


@register.inclusion_tag('menu/menus.html', takes_context=True)
def draw_menu(context, menu):
    """
    Тэг для построения древовидного меню.
    """
    try:
        filter_post_id = int(context['request'].GET[menu])
        posts = Post.objects.filter(menu__title=menu)
        posts_values = posts.values()
        main_post = [post for post in posts_values.filter(parent=None)]
        filter_posts_id_list = filter_post_id_list(
            posts.get(id=filter_post_id),
            main_post,
            filter_post_id
        )

        for post in main_post:
            if post['id'] in filter_posts_id_list:
                post['childrens'] = child(
                    posts_values,
                    post['id'],
                    filter_posts_id_list
                )
        post_dict = {'posts': main_post}

    except Post.DoesNotExist:
        post_dict = {
            'posts': [
                post for post in Post.objects.filter(
                    menu__title=menu, parent=None).values()
                ]
            }

    post_dict['menu'] = menu
    post_dict['additional_menu'] = additional_menu(context, menu, [])
    return post_dict
