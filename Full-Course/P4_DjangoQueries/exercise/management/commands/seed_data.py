import random
from faker import Faker
from django.core.management.base import BaseCommand
from exercise.models import Author, Books, Publisher, User

fake = Faker()


class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))

        # Clear existing data
        Author.objects.all().delete()
        Books.objects.all().delete()
        Publisher.objects.all().delete()
        User.objects.all().delete()

        # Create Users
        users = []
        for _ in range(100):
            user = User(
                username=fake.user_name(),
                email=fake.email()
            )
            user.save()
            users.append(user)

        # Create Publishers
        publishers = []
        for _ in range(20):  # Fewer publishers to keep it realistic
            publisher = Publisher(
                firstname=fake.first_name(),
                lastname=fake.last_name(),
                recommendedby=None,  # Will update this later
                joindate=fake.date(),
                popularity_score=random.randint(1, 100)
            )
            publisher.save()
            publishers.append(publisher)

        # Update publisher's recommendedby field
        for publisher in publishers:
            publisher.recommendedby = random.choice(publishers)
            publisher.save()

        # Create Authors
        authors = []
        for _ in range(100):
            author = Author(
                firstname=fake.first_name(),
                lastname=fake.last_name(),
                address=fake.address(),
                zipcode=fake.zipcode(),
                telephone=fake.phone_number(),
                recommendedby=None,  # Will update this later
                joindate=fake.date(),
                popularity_score=random.randint(1, 100)
            )
            author.save()
            authors.append(author)

        # Update author's recommendedby field
        for author in authors:
            author.recommendedby = random.choice(authors)
            author.save()

        # Create Books
        for _ in range(100):
            book = Books(
                title=fake.sentence(nb_words=3),
                genre=fake.word(),
                price=random.randint(10, 500),
                published_date=fake.date(),
                author=random.choice(authors),
                publisher=random.choice(publishers)
            )
            book.save()

        # Update author followers
        for author in authors:
            author.followers.set(random.sample(users, k=random.randint(1, 10)))

        self.stdout.write(self.style.SUCCESS(
            'Successfully seeded the database'))
