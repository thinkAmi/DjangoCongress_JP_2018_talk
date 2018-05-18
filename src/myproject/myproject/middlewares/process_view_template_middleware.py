from myapp.views import HelloTemplateView


class ProcessViewTemplateDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[process_view] one-time configuration')

    def __call__(self, request):
        print('[process_view] before view')
        response = self.get_response(request)
        print('[process_view] after view')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[process_view] hook!')
        print(type(request))
        print(type(view_func))
        print(type(view_args))
        print(type(view_kwargs))
        return HelloTemplateView(request=request).render_to_response(
            {'message': 'TemplateResponse by process_view\n'})

    def process_template_response(self, request, response):
        print('[process_template_response] hook!')
        print(type(request))
        print(type(response))
        response.context_data['message'] += 'overwrite by process_template_response'
        return response
