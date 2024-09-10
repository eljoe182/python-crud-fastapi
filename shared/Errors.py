class HandleError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)


class UseCaseError(Exception):
    pass


class RepositoryError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)


class ProductNotFoundError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)
