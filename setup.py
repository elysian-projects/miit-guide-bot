from setuptools import find_packages, setup

# Setting up the application

setup(
    name = "bot",
    version = "0.1.0",
    packages = find_packages(exclude = ["tests", "tests.*", "docs"]),
    url = 'https://github.com/miit-projects/miit-guide-bot.git',
    python_requires='>=3.9',
    entry_points = {
        "console_scripts": [
            "bot = src.bot.index:main"
        ]
    },
)
