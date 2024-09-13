from cx_Freeze import setup, Executable

setup(
    name="Guessing Game",
    version="1.0",
    description="A simple guessing game",
    author="Vishal Pandey",
    executables=[
        Executable("guessing_game.py",
            icon="project.ico",
            shortcut_name="Guessing Game",
            shortcut_dir="DestktopFolder")
        ]
)
