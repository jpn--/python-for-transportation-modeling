
from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_lexer_for_filename
from pygments.formatters import HtmlFormatter
from IPython.display import display, HTML
from os import PathLike

template = """<style>
{}
</style>
{}
"""


def show_file(filename, lexer=None):
	"""
	Display the contents of a file or module in a Jupyter notebook.

	Parameters
	----------
	filename : str, bytes, PathLike, or module
	lexer : lexer or str, optional
		The pygments lexer

	"""


	if not isinstance(filename, (str, bytes, PathLike)):
		filename = getattr(filename, '__file__', None)

	if isinstance(lexer, str):
		lexer = get_lexer_by_name(lexer)
	elif lexer is None:
		lexer = get_lexer_for_filename(filename)
	formatter = HtmlFormatter(cssclass='pygments')

	with open(filename) as f:
		code = f.read()

	html_code = highlight(code, lexer, formatter)
	css = formatter.get_style_defs('.pygments')

	html = template.format(css, html_code)

	display(HTML(html))


