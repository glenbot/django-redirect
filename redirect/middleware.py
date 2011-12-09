from django.core.urlresolvers import resolve


class RedirectMiddleware(object):
    """
        Process the redirect patterns from redirects.dynamic_urls.
    """
    def process_response(self, request, response):
        if response.status_code != 404:
            # No need to check for a redirect for non-404 responses.
            return response

        path = request.get_full_path()

        try:
            urlconf = 'redirect.dynamic_urls'
            redirect, args, kwargs = resolve(path, urlconf=urlconf)
            return redirect(request, **kwargs)
        except:
            # No redirect was found. Return the response.
            return response
