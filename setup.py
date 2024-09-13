from cx_Freeze import setup, Executable

setup(
    name="Guessing Game",
    version="1.0",
    description="A simple guessing game",
    author="Vishal Pandey",
    executables=[
        Executable("C:/Users/Vishal Pandey/OneDrive/Desktop/Guessing Game/guessing_game.py",
            icon="C:/Users/Vishal Pandey/OneDrive/Desktop/Guessing Game/project.ico",
            shortcut_name="Guessing Game",
            shortcut_dir="DestktopFolder")
        ]
)
