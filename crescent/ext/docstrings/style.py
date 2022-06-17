from enum import IntEnum

from docstring_parser import DocstringStyle


class Style(IntEnum):
    REST = DocstringStyle.REST.value
    GOOGLE = DocstringStyle.GOOGLE.value
    NUMPYDOC = DocstringStyle.NUMPYDOC.value
    EPYDOC = DocstringStyle.EPYDOC.value
    AUTO = DocstringStyle.AUTO.value
