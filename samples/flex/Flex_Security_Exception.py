# Customized Exception class
class FlexSecurityException(Exception):

    def __init__(self, reason=None):
        super(FlexSecurityException, self).__init__(reason)
