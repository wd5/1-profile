SECTIONS = ['feedback', 'blog', ]


def section(request):
    path = request.path.strip('/')
    if path:
        path = path.split('/')[0]
    return {'section': path}
    
