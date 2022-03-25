# First, import click dependency
import click


# Decorate the method that will be the command name with `click.command`
@click.command()
# You can define custom parameters as defined in `click`: https://click.palletsprojects.com/en/7.x/options/
def greet():
    # Help message to show with the command
    """
    Subcommand plugin that does something.
    """
    # Done! Now implement your custom functionality in the command
    click.echo("Hello! I'm a Nile plugin")
