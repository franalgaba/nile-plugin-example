# Nile plugin example :boat:

This project is an example plugin for extending functionality in Nile.

## Installation

`pip install nile-greet`

## Usage

After installing you should already have the command available for usage. Run `nile --help` for checking the `nile greet` availability.

## Development

For creating new plugins follow this instructions below.

1. Install Poetry:

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

2. Install dependencies:

`poetry install`

After having the environment setted up we can start developing. We will use `click` for extending Nile commands. All new commands must be implemented as `click.commands`. Find below an implementation design template:

```python
# First, import click dependency
import click

# Decorate the method that will be the command name with `click.command` 
@click.command()
# You can define custom parameters as defined in `click`: https://click.palletsprojects.com/en/7.x/options/
def my_command():
    # Help message to show with the command
    """
    Subcommand plugin that does something.
    """
    # Done! Now implement your custom functionality in the command
    click.echo("I'm a plugin overiding a command!")
```

Great! Now our new Nile command is ready to be used. For Nile to detect it make sure at least version `0.6.0` is installed. Then modify the `pyproject.toml` file as follows:

```
# We need to specify that click commands are Poetry entrypoints of type `nile_plugins`. Do not modify this
[tool.poetry.plugins."nile_plugins"]
# Here you specify you command name and location <command_name> = <package_method_location>
"greet" = "nile_greet.main.greet"
```

## Testing

`poetry run pytest tests`