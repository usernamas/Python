class lokomotyvas:

    '''
    Lokomotyvas turi lokomotyvo mase ir maximalia tempiamaja mase.
    '''

    def __init__(self, lokomotyvo_mase, max_tempiamoji_mase):
        '''
        >>> lok = lokomotyvas(10,100)
        >>> print(lok.lokomotyvo_mase)
        10
        >>> print(lok.max_tempiamoji_mase)
        100
        '''
        self.lokomotyvo_mase = lokomotyvo_mase
        self.max_tempiamoji_mase = max_tempiamoji_mase

    if __name__ == "__main__":
        import doctest
        doctest.testmod()