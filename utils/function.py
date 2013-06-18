def singleton(className):
    def wrapped():
        it =  className.__dict__.get('__it__')
        if it is not None:
            return it

        className.__it__=className()
        return className.__it__
    return wrapped