
def create_seed_data():
    import random
    from datetime import datetime
    from django.contrib.auth.models import User
    from my_views.models import Car, CAR_COLOR_CHOICES

    # Retrieve users by their IDs
    user1 = User.objects.get(pk=1)
    user2 = User.objects.get(pk=2)

    # List of car models and names
    car_data = [
        {"name": "Toyota Camry", "model": "2022-01-01"},
        {"name": "Honda Civic", "model": "2023-02-15"},
        {"name": "Ford Mustang", "model": "2021-10-05"},
        {"name": "Chevrolet Corvette", "model": "2023-05-20"},
        {"name": "Tesla Model 3", "model": "2022-08-10"},
        # Add more car data as needed
    ]

    # Create seed data for each car
    for car_info in car_data:
        car = Car.objects.create(
            user=random.choice([user1, user2]),
            name=car_info["name"],
            model=datetime.strptime(car_info["model"], "%Y-%m-%d").date(),
            color=random.choice(CAR_COLOR_CHOICES)[0]
        )
        print(
            f"Created car: {car.name} Color: {car.color}, Model: {car.model})")


if __name__ == '__main__':
    create_seed_data()
