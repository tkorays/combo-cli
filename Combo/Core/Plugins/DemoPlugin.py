import click

@click.command('demo', help='this is a demo plugin')
def demo():
    click.echo('hello demo')


plugin = {
    'name': 'demo',
    'description': 'demo plugin',
    'author': 'tkorays',
    'email': 'tkorays@hotmail.com',
    'functions': {
        'demo': demo
    },
    'deps': []
}
