# crescent-ext-docstrings

A docstring parser for [hikari-crescent](https://github.com/magpie-dev/hikari-crescent).

## Installation
```
pip install crescent-ext-docstrings
```

## Usage

This extension works for both class commands and function commands.

```python
import crescent
from crescent.ext import docstrings

bot = crescent.Bot("...")

@bot.include
@docstrings.parse_doc
@crescent.command
async def example(ctx: crescent.Context, a: str, b: str) -> None:
    """
    This is the command's description.
    
    :param a:
        This is the first param's description.
    :param b:
        This is the first param's description.
    """
    await ctx.respond(f"{a=},{b=}")

@bot.include
@docstrings.parse_doc
@crescent.command(name="class_example")
class ClassExample:
    """
    Other doc styles are supported. This is google doc style.
    
    Args:
        a: This is the first param's description.
        b: This is the first param's description.
    """

    a = crescent.option(str)
    b = crescent.option(str)

    async def callback(self, ctx: crescent.Context) -> None:
        await ctx.respond(f"{self.a=},{self.b=}")

bot.run()

```

### Doc Styles
Since this library relies on [docstring-parser](https://github.com/rr-/docstring_parser), the styles Rest, Google, Numpy, and Epydoc are supported. If no style is specified, the style will be inferred.

```python
import docstrings

@bot.include
@docstrings.parse_doc(style=docstrings.Style.REST)
@crescent.command
async def example(ctx: crescent.Command, a: str) -> None:
    """
    Rest style description.

    :param a:
        The parameter.
    """
    ...

```
