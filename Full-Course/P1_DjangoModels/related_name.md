
# related_name

In Django, the `related_name` attribute is used in model field definitions to specify the name of the reverse relation from the related model back to the model that defines the relation. This is particularly useful for creating clear and unambiguous reverse relationships, especially when dealing with multiple relationships between models.

### Understanding `related_name`

When you define a ForeignKey, OneToOneField, or ManyToManyField, Django automatically creates a reverse relation that allows you to access related objects from the related model. By default, this reverse relation is named using the lowercase name of the related model followed by `_set`. For example, if you have a `Song` model with a ForeignKey to a `Singer` model, you can access all songs of a singer using `singer.song_set.all()`.

The `related_name` attribute allows you to customize this reverse relation name. This is particularly helpful in the following scenarios:

- **Clarity**: Providing a more meaningful name for the reverse relation.
- **Avoiding Name Conflicts**:  When a model has multiple relationships to the same model, related_name helps to avoid naming conflicts by providing unique names for each reverse relationship.

### Example Usage of `related_name`

Consider the following models where a `Song` has a foreign key to a `Singer`.

```python
from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="songs")
    duration = models.IntegerField()

    def __str__(self):
        return self.title
```

In this example, the `related_name="songs"` specifies that the reverse relation from `Singer` to `Song` should be called `songs` instead of the default `song_set`. This allows you to access all songs of a singer using `singer.songs.all()`.

### Using `related_name` in Multiple Relationships

If you have multiple foreign keys to the same model, using `related_name` becomes essential to avoid name conflicts.

```python
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    main_singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="main_albums")
    featured_singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="featured_albums")

    def __str__(self):
        return self.title
```

In this example, there are two foreign keys to the `Singer` model: `main_singer` and `featured_singer`. By setting `related_name="main_albums"` and `related_name="featured_albums"`, you avoid conflicts and clearly distinguish between the two sets of albums in which a singer is involved.

### Accessing Reverse Relationships

With the models defined above, you can access the related objects as follows:

```python
# Assuming you have some instances created
singer = Singer.objects.get(id=1)

# Access songs related to this singer
singer_songs = singer.songs.all()

# Access albums where the singer is the main singer
main_albums = singer.main_albums.all()

# Access albums where the singer is the featured singer
featured_albums = singer.featured_albums.all()
```

### Conclusion

Using `related_name` in Django models is a powerful way to customize and clarify reverse relationships. It helps keep your code clean and avoids conflicts, especially when dealing with multiple relationships to the same model. By using `related_name`, you ensure that the relationships in your models are easy to understand and use.