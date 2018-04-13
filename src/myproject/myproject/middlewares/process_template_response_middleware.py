class ProcessTemplateResponseDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[process_template_response] one-time configuration')

    def __call__(self, request):
        print('[process_template_response] before view')
        response = self.get_response(request)
        print('[process_template_response] after view')
        return response

    def process_template_response(self, request, response):
        print('[process_template_response] hook!')
        print(type(request))
        print(type(response))
        response.context_data['message'] = 'overwrite by middleware'
        return response
