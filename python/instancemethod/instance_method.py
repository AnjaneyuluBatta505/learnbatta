class User(object):

    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

u1 = User(1, 'Anji', 'B')
print(u1.get_full_name())
# Output: Anji B
u2 = User(2, 'Shiva', 'D')
print(u2.get_full_name())
# Output: Shiva D
