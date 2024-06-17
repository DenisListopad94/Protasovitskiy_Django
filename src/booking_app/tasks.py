from celery import shared_task


@shared_task
def debug_task_1(seconds: int):
    from time import sleep
    sleep(seconds)
    return f'we sleep {seconds} seconds'


@shared_task
def debug_task_2(seconds: int):
    from time import sleep
    sleep(seconds)
    return f'we sleep {seconds} seconds'


@shared_task
def task_every_3m40s():
    print("Task running every 3 minutes 40 seconds")


@shared_task
def task_three_times_hourly():
    print("Task running every hour from 19 to 21, for a total of 3 times")
