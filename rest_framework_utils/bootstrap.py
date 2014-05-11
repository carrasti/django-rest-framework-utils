from rest_framework import renderers


def RestFrameworkJsonBootstrapData(view,
                               request,
                               view_args=[],
                               view_kwargs={},
                               data={}):
    """
    This method provides a way to bootstrap the data from django-rest-framework
    generic views to json encoded text.

    It is a bit hackish since it has to use the request to have access to the
    current user accessing the api, and check the permissions for it.

    If possible fix this function in favor of a cleaner one.

    Arguments
    vuew -- the view from rest_framework GenericApiView, pass the result of 
            the .as_view() call
    request -- the Django HttpRequest object

    Keyword Arguments
    view_args -- *args to be passed when defining the view
    view_kwargs -- *kwargs to be passed when defining the view,
    data -- dictionary which will be transformed to get paramters
            for the request
    """
    old_get = request.GET
    request.GET = data
    items_view = view(request, *view_args, **view_kwargs)
    setattr(items_view, 'accepted_renderer', renderers.JSONRenderer())
    setattr(items_view, 'accepted_media_type', 'application/json')
    ret = items_view.render().content
    request.GET = old_get
    return ret