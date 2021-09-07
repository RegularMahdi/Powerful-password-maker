from random import choice
import pyperclip

abc = list("abcdefghijklmnopqrstuvwxyz")
ABC = list("abcdefghijklmnopqrstuvwxyz".upper())
numbers = list("0123456789")
symbols = list("!@#$%^&*()_+=-\\|{}[]~`/.,<>\"';:")
all_ = abc.copy()  # abc + ABC + number + symbols
all_.extend(ABC)
all_.extend(numbers)
all_.extend(symbols)


def password():
    abc_exist = 1
    ABC_exist = 2
    num_exist = 4
    sym_exist = 8
    _password = ""  # returned password
    while True:
        for n in range(choice(range(20, 30))):
            _password = _password + choice(all_)  # update password

        # checking power of password
        pas_exist = 0
        for i in _password:
            if i in abc:
                pas_exist = pas_exist & abc_exist
            if i in ABC:
                pas_exist = pas_exist & ABC_exist
            if i in numbers:
                pas_exist = pas_exist & num_exist
            if i in symbols:
                pas_exist = pas_exist & sym_exist

        if pas_exist | 15:
            return _password


if __name__ == "__main__":
    password_ = password()  # get a password
    pyperclip.copy(password_)  # copy a password
    print("password: " + password_)  # show a password
    print("password copied")
    input("Press Enter To Quit : ")