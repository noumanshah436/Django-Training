To use custom template filters in Django, you need to follow these steps:

### 1. Create a Template Tags Directory:

First, create a directory named `templatetags` within your Django app directory. If it doesn't exist, create one.

```plaintext
your_app/
    templatetags/
        __init__.py
```

### 2. Create a Python Module for Custom Filters:

Inside the `templatetags` directory, create a Python module (`.py` file) to define your custom filters.

For example, let's create a module named `custom_filters.py`.

### 3. Define Custom Filters in the Python Module:

In the `custom_filters.py` module, define your custom template filters using the `@register.filter` decorator.

Here's an example of how you can define a custom filter to convert a string to uppercase:

```python
# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='uppercase')
def uppercase(value):
    return value.upper()
```

### 4. Load Custom Filters in Templates:

In your template where you want to use the custom filter, load the custom template tags at the beginning of the template using the `{% load %}` tag.

```html
{% load custom_filters %}
```

### 5. Use Custom Filters in Templates:

Now, you can use the custom filter you defined in your template by specifying its name inside template tags.

For example, to use the `uppercase` filter:

```html
{{ some_variable|uppercase }}
```

### 6. Restart Development Server (if necessary):

If you created a new Python module or made changes to existing modules, make sure to restart the development server for the changes to take effect.

### 7. Ensure Directory Structure:

Ensure that your app's directory structure and files are properly organized. For example:

```plaintext
your_app/
    templatetags/
        __init__.py
        custom_filters.py
    ...
```

### Example Usage:

Let's say you've defined a custom filter named `uppercase` as shown above. You can use it in your templates to convert a string to uppercase:

```html
{% load custom_filters %}

{{ "hello world"|uppercase }}
```

This would output "HELLO WORLD" in the rendered HTML.

By following these steps, you can define and use custom template filters in your Django project to perform various transformations or operations on template variables.