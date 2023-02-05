from __future__ import annotations

from functools import partial
from typing import Callable, overload

from crescent.internal import AppCommand, AppCommandMeta, Includable
from docstring_parser import DocstringStyle, parse
from hikari import CommandOption

from .exceptions import ParsingError
from .style import Style


def _lookup_arg(name: str, app_command: AppCommand) -> CommandOption | None:
    if not app_command.options:
        return None
    for option in app_command.options:
        if option.name == name:
            return option
    return None


IncludableT = Includable[AppCommandMeta]


@overload
def parse_doc(includable: IncludableT, /) -> IncludableT:
    ...


@overload
def parse_doc(*, style: Style = ...) -> Callable[[IncludableT], IncludableT]:
    ...


def parse_doc(
    includable: IncludableT | None = None, style: Style = Style.AUTO
) -> IncludableT | Callable[[IncludableT], IncludableT]:

    if includable is None:
        return partial(parse_doc, style=style)

    docs = includable.metadata.owner.__doc__

    if not docs:
        return includable.metadata.owner  # type: ignore

    parsed_docs = parse(docs, style=DocstringStyle(style))

    for param in parsed_docs.params:
        app_option = _lookup_arg(param.arg_name, includable.metadata.app_command)
        if app_option is None:
            raise ParsingError(
                f"Parameter `{param.arg_name}` is not present in the signature of"
                f"`{includable.metadata.callback.__name__}`."
            )

        if param.description:
            app_option.description = param.description

    if parsed_docs.short_description:
        includable.metadata.app_command.description = parsed_docs.short_description

    return includable
