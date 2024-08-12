# Goal: to create a class which can get a person's name
# How: Create a class called PersonName and a method called full_name that takes two arguments, first_name and last_name, and returns the full name of the person


class PersonName:
    def __init__(self):
        pass 

    def full_name(self, first_name, last_name):
        """
        This function returns the full name of the person
        :param first_name: This is the first name of the person
        :param last_name: This is the last name of the person
        :type first_name: str
        :type last_name: str
        :return: name of the person
        :rtype: str
        """
        name = first_name + " " + last_name
        return name # return the full name of the person
