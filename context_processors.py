SECTIONS = ['feedback', 'blog', ]


def section(request):
    path = request.META.get('PATH_INFO','').strip('/')
    if path:
        path = path.split('/')[0]
    return {'section': path}
    
