# Goal: Create a dummy function that is then called and executed successfully


class Person(object):
    def __init__(self, name, age, job):
        """


        Initializes new object of class Person based on user inputs when created


        :param name: name of the person in class
        :param age: age of the person in class
        :param job: job of the person in class


        """
        self.name = name
        self.age = age
        self.job = job

    def person_info(self):
        """

        Checks if each input type is valid, based on the if statement


        """
        if (
            (type(self.name) == str)
            and (type(self.age) == int)
            and (type(self.job) == str)
        ):
            return f"Hello, my name is {self.name}. I am {self.age} years old. My job is a(n) {self.job}."


Person1 = Person("Chris", 20, "Intern")

print(Person1.person_info())
