# ░░░░░░░█▀▄░█▀▀░█▀█░█░░░░░█░█░█▀█░█▀▄░█░░░█▀▄░░░░░░░█▀▀░▀█▀░█░█░█▀▀░█▀▄░░░░░░
# ░░░░░░░█▀▄░█▀▀░█▀█░█░░░░░█▄█░█░█░█▀▄░█░░░█░█░░░░░░░█▀▀░░█░░▄▀▄░█▀▀░█░█░░░░░░
# ░░░░░░░▀░▀░▀▀▀░▀░▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀░░▄▀░░░░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀░░░░░░░

from lib.e_20 import User


# See how we've annotated the function
def say_hello(user: User):
    return f"Hello, {user.name}!"


print(say_hello("John"))  # error, highlighted by vscode


print(say_hello(User("John")))  # works
