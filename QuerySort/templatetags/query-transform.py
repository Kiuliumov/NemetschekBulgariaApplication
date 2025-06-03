from django import template

register = template.Library()


@register.simple_tag
def query_transform(request, **kwargs):
    updated = request.GET.copy()
    for k, v in kwargs.items():
        updated[k] = v
    if 'page' in updated and updated['page'] == '':
        del updated['page']
    return updated.urlencode()
