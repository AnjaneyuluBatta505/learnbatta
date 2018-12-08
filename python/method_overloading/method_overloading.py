class SayHello:

    def hello(self, first_name=None, last_name=None):
        if first_name and last_name:
            print("Hello {0} {1} !".format(first_name, last_name))
        elif first_name:
            print("Hello {0} !".format(first_name))
        else:
            print("Hello !")

obj = SayHello()
obj.hello("Anjaneyulu", "Batta")
# Output: Hello Anjaneyulu Batta ! 
obj.hello("Anjaneyulu")
# Output: Hello Anjaneyulu !
obj.hello()
# Output: Hello !
