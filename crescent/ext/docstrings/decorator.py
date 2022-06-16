from crescent.internal import MetaStruct


def docstring(meta: MetaStruct):
    docs = meta.callback.__doc__

    print(docs)
