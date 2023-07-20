def session_tracking_middleware(get_response):
    def middleware(request):
        if not request.session.session_key:
            request.session.save()
        return get_response(request)
    return middleware
