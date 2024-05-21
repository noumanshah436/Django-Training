def my_middleware(get_response):
    print("One Time Initialization")

    def my_function(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response
    return my_function


# The get_response callable might be the actual view (if this is the last listed middleware) or 
# it might be the next middleware in the chain.

# The current middleware doesn’t need to know or care what exactly it is, just that it represents whatever comes next.