In Django templates, you can't directly call instance methods on objects passed from views regardless of whether they are related to `request.user` or other model objects. This limitation is due to Django's design principle of keeping templates simple and focused on presentation logic rather than business logic.

When passing objects to templates, it's best practice to include any necessary data or logic in the view before passing it to the template. This ensures that the template remains clean and focused on rendering.

If you need to perform any complex logic or calculations based on model instances in your template, it's recommended to pre-process that data in your view and pass the result to the template for rendering. This could involve using properties or attributes of model instances rather than calling methods directly.

For example, if you have a `Post` model with a method `get_comments_count()` that returns the number of comments for a post, you could create a property or attribute `comments_count` in your view and then access it in the template:

```python
# views.py
from django.shortcuts import render
from myapp.models import Post

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    post.comments_count = post.get_comments_count()  # Pre-process data
    return render(request, 'post_detail.html', {'post': post})
```

```html
<!-- post_detail.html -->
<h1>{{ post.title }}</h1>
<p>Comments: {{ post.comments_count }}</p>
```

By following this approach, you maintain separation of concerns and keep your templates focused on presentation while handling any necessary logic in the views.