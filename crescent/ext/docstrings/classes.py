from __future__ import annotations

from typing import Any

from crescent.commands import decorators

CLASS_DOCSTRINGS: dict[Any, str | None] = {}


cmd_dec = decorators.command


def cursed_command_dec(cls_or_func: Any, *args: Any, **kwargs: Any) -> Any:

    meta = cmd_dec(cls_or_func, *args, **kwargs)

    if isinstance(cls_or_func, type):
        CLASS_DOCSTRINGS[id(meta)] = cls_or_func.__doc__

    return meta


decorators.command = cursed_command_dec  # type: ignore
