import datetime
class Worker:
    def __init__(self, id: int, first_name: str, last_name: str, hire_date: datetime):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hire_date = hire_date

    def set_first_name(self, first_name: str):
        self.__first_name = first_name
    def set_last_name(self, last_name: str):
        self.__last_name = last_name
    def set_hire_date(self, hire_date: datetime):
        self.__hire_date = hire_date
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def set_hire_date(self):
        return self.__hire_date


class Employee(Worker):
    def __init__(self, id: int, first_name: str, last_name: str, hire_date: datetime, salary: float):
        self.__salary = salary
        super().__init__(id, first_name, last_name, hire_date)
    def get_salary(self, salary: float):
        self.__salary = salary
    def set_salary(self):
        return self.__salary
    def get_hourly_rate(self):
        return self.__salary / 261 / 8


class Contractor(Worker):
    def __init__(self, id: int, first_name: str, last_name: str, hire_date: datetime, hourly_rate: float):
        self.__hourly_rate = hourly_rate
        super().__init__(id, first_name, last_name, hire_date)
    def get_hourly_rate(self, hourly_rate: float):
        self.__hourly_rate = hourly_rate
    def set_hourly_rate(self):
        return self.__hourly_rate

class Task:
    def __init__(self, id: int, name: str, description: str, assign_to: Worker, duration_hour: float):
        self.__id = id
        self.__name = name
        self. __description = description
        self.__assign_to = assign_to
        self.__duration_hour = duration_hour
        self.__hours_completed = 0.0

    def set_name(self, name: str):
        self.__name = name
    def set_description(self, description: str):
        self.__description = description
    def set_assigned_to(self, assign_to = Worker):
        self.__assign_to = assign_to
    def set_duration_hour(self, duration_hour: float):
        self.__duration_hour = duration_hour


    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_description(self):
        return self.__description
    def get_assigned_to(self):
        return self.__assign_to
    def get_duration_hour(self):
        return self.__duration_hour
    def hours_completed(self):
        return self.__hours_completed
    def add_time(self, num_hours: float):
        self.__hours_complete += num_hours

class Project:
    def __init__(self, id: int, name: str, hour_estimated: float):
        self.__id = id
        self.__name = name
        self.__hour_estimated = hour_estimated
        self.__tasks = []

    def set_name(self, name: str):
        self.__name = name
    def set_hour_estimated(self, hour_estimated: float):
        self.__hour_estimated = hour_estimated

    def get_id(self):
        return self.__id
    def get__name(self):
        return self.__name
    def get_hour_estimated(self):
        return self.__hour_estimated
    def add_task(self, task: Task):
        # has to specify task as object, not a string
        self.__tasks.append(task)