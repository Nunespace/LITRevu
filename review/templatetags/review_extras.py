from django import template

register = template.Library()

@register.filter
def stars(number, max_stars=5):
    """Tranforme un nombre en une chaîne d'étoiles"""
    if number > max_stars:
        return "★" * max_stars
    elif number < 1:
        return "☆" * max_stars
    return "★" * number + "☆" * (max_stars - number)


@register.filter
def model_type(value):
    return type(value).__name__


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'Vous avez'
    else:
        auteur = f'{user.username} a'
    return auteur
