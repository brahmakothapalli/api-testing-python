from faker import Faker

fake = Faker(['en_US'])


def get_person_name():
    return fake.name()


def get_person_job():
    return fake.job()
