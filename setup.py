from cx_Freeze import setup, Executable

setup(
    name="Guessing Game",
    version="1.0",
    description="A simple guessing game",
    author="YOUR_NAME", # ENTER YOUR NAME AT THE PLACE OF YOUR_NAME.
    executables=[
        Executable("PATH_TO_PYTHON_FILE", # ENTER YOUR PATH TO YOUR PYTHON FILE.
            icon="PATH_TO_ICON_IMAGE", # ENTER YOUR PATH TO ICON IMAGE(IT SHOULD BE IN .ICO). 
            shortcut_name="Guessing Game",
            shortcut_dir="DestktopFolder")
        ]
)
