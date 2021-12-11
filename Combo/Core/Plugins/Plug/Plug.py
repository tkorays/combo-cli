import click
from Combo.Core.Configurations import Configuration


@click.group(help='plug plugin')
def plug():
    pass


@click.command('add', help='add plugin')
@click.option('--local', default=False, is_flag=True, help='add plugin in local directory!')
@click.option('--name', type=str, required=True, help='local plugin name')
def plug_add(local, name):
    cfg = Configuration()
    if local:
        cfg.add_plugin(name)
        click.echo('add local plugin success!')


@click.command('remove', help='remove plugin')
@click.option('--name', type=str, required=True, help='plugin name to be removed')
def plug_remove(name):
    Configuration().remove_plugin(name)
    click.echo('remove plugin success!')


@click.command('update', help='update plugin')
def plug_update():
    click.echo('update plugin')


@click.command('version', help='plugin version')
def plug_version():
    click.echo('plugin version')


@click.command('list', help='list plugin')
@click.option('--local', default=False, is_flag=True, help='list local plugins!')
def plug_list(local):
    if local:
        plg = Configuration().plugins()
        click.echo('list local plugins: {}'.format(plg))
    else:
        click.echo('remote plugin is not supported!')


@click.command('auto-update', help='auto-update plugin')
@click.option('--on', is_flag=True, default=None, help='switch auto update')
@click.option('--off', is_flag=True, default=None, help='switch auto update')
def plug_auto_update(on, off):
    if on is not None:
        Configuration().plugin_auto_update(on)
    if off is not None:
        Configuration().plugin_auto_update(not off)


@click.command('server', help='plugin server')
def plug_server():
    click.echo('plugin server')


plug.add_command(plug_add)
plug.add_command(plug_remove)
plug.add_command(plug_update)
plug.add_command(plug_version)
plug.add_command(plug_list)
plug.add_command(plug_auto_update)
plug.add_command(plug_server)

