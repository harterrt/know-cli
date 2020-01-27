import click
from importlib.machinery import SourceFileLoader
from . import config
from . import zeit as zz


def settings_option(func):
    # Decorator to read a settings file
    def callback(ctx, param, settings_path):
        try:
            module = SourceFileLoader('lt_config', settings_path).load_module()
        except FileNotFoundError as e:
            module = None
            click.echo(
                "Couldn't load config file {}: {}"
                .format(settings_path, e.strerror)
            )

        return config.get_settings_from_module(module)

    return click.option('--settings', help='Path to settings file.',
                        type=click.Path(), callback=callback,
                        default=config.settings_path)(func)


@click.group()
@settings_option
@click.pass_context
def cli(ctx, settings):
    ctx.obj = settings


@cli.command()
@click.pass_obj
def zeit(settings):
    zz.new_note(settings)


if __name__ == "__main__":
    cli()
