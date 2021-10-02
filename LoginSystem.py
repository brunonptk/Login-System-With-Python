class User:

    def __init__(self, name, email, password, login):
        self.name = name
        self.email = email
        self.password = password
        self.login = login


    def Login(self):
        email = input('Enter Email: ')
        password = input('Enter Password: ')

        if self.email == email and self.password == password:
            print('Login Sucess \n', self.name, '\n', self.email)

        else:
            print('Login Failed!')

user1 = User('Bruno Oliveira', 'bruno@gmail.com', '123', False)
user2 = User('Henrique Morais', 'henrique@gmail.com', '789', False)
user1.Login()
