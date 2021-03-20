from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    banned_words = ['негатив', 'депрессия', 'обзывательство']
    b = value.split(' ')
    for c in banned_words:
        for a in b:
            if a == c:
                b.remove(a)
    return ' '.join(b)
