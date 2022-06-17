from __future__ import annotations

from crescent import CommandCallbackT
from crescent.internal import MetaStruct, AppCommandMeta
from docstring_parser import DocstringStyle, parse
from hikari import CommandOption
from .style import Style
from .exceptions import ParsingException
from .classes import CLASS_DOCSTRINGS


def _lookup_arg(name: str, app: AppCommandMeta) -> CommandOption | None:
    if not app.app.options:
        return None
    for option in app.app.options:
        if option.name == name:
            return option
    return None


def parse_doc(
    meta: MetaStruct[CommandCallbackT, AppCommandMeta], *, style: Style = Style.AUTO
) -> MetaStruct[CommandCallbackT, AppCommandMeta]:

    docs = CLASS_DOCSTRINGS.get(id(meta)) or meta.callback.__doc__

    if not docs:
        return meta

    parsed_docs = parse(docs, style=DocstringStyle(style))

    for param in parsed_docs.params:
        app_option = _lookup_arg(param.arg_name, meta.metadata)
        if app_option is None:
            raise ParsingException(
                f"Parameter `{param.arg_name}` is not present in the signature of `{meta.callback.__name__}`."
            )

        if param.description:
            app_option.description = param.description

    if parsed_docs.short_description:
        meta.metadata.app.description = parsed_docs.short_description

    return meta
