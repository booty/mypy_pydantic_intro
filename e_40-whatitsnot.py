# ░░░░░░░█▄█░█░█░█▀█░█░█░░░█▀▄░█▀█░█▀▀░█▀▀░█▀█░▀░▀█▀░░░░░░░░░░░░░░░
# ░░░░░░░█░█░░█░░█▀▀░░█░░░░█░█░█░█░█▀▀░▀▀█░█░█░░░░█░░░░░░░░░░░░░░░░
# ░░░░░░░▀░▀░░▀░░▀░░░░▀░░░░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░░▀░░▀░░▀░░▀░░░░░░░


class Spaceship:
    def __init__(self, name: str, crew: str):
        self.name = name
        self.crew = crew

    def __str__(self):
        return f"Spaceship {self.name} with crew {self.crew}"


def launch_spaceship(thing_im_launching: Spaceship):
    return f"{thing_im_launching.name} launched with crew {thing_im_launching.crew}"


# Once you actually run your code, mypy doesn't do anything
print(launch_spaceship("Apollo 11"))
