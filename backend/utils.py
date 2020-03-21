from django.utils import timezone


# Utility functions
def get_this_time_tomorrow():
    return timezone.now() + timezone.timedelta(days=1)


def get_priority_choices():
    return [0, 1, 2, 3, 4, 5]
