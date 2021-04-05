from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('myapp', 'views'),
    autoescape=select_autoescape(['html', 'xml'])
)
