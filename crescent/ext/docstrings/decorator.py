from __future__ import annotations

from functools import partial
from typing import Callable, overload

from crescent.internal import AppCommandMeta, MetaStruct
from docstring_parser import DocstringStyle, parse
from hikari import CommandOption

from crescent import CommandCallbackT

from .classes import CLASS_DOCSTRINGS
from .exceptions import ParsingError
from .style import Style


def _lookup_arg(name: str, app: AppCommandMeta) -> CommandOption | None:
    if not app.app.options:
        return None
    for option in app.app.options:
        if option.name == name:
            return option
    return None


META_T = MetaStruct[CommandCallbackT, AppCommandMeta]


@overload
def parse_doc(meta: META_T, /) -> META_T:
    ...


@overload
def parse_doc(*, style: Style = ...) -> Callable[[META_T], META_T]:
    ...


def parse_doc(
    meta: META_T | None = None, style: Style = Style.AUTO
) -> META_T | Callable[[META_T], META_T]:

    if meta is None:
        return partial(parse_doc, style=style)

    docs = CLASS_DOCSTRINGS.get(id(meta)) or meta.callback.__doc__

    if not docs:
        return meta

    parsed_docs = parse(docs, style=DocstringStyle(style))

    for param in parsed_docs.params:
        app_option = _lookup_arg(param.arg_name, meta.metadata)
        if app_option is None:
            raise ParsingError(
                f"Parameter `{param.arg_name}` is not present in the signature of"
                f"`{meta.callback.__name__}`."
            )

        if param.description:
            app_option.description = param.description

    if parsed_docs.short_description:
        meta.metadata.app.description = parsed_docs.short_description

    return meta
