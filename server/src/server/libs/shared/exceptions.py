from __future__ import print_function, absolute_import, unicode_literals

from traceback import format_tb


class ServiceException(Exception):
    """requests returned an error
    """
    def __init__(self, message=None, cause=None, traceback=None):
        """[summary]

        Args:
            message ([type], optional): [description]. Defaults to None.
            cause ([type], optional): [description]. Defaults to None.
            traceback ([type], optional): [description]. Defaults to None.
        """
        if message is None and cause is not None:
            message = str(cause)

        super(ServiceException, self).__init__(message)
        self.message = message
        self.cause = cause
        self.traceback = traceback

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if self.cause and self.traceback and not hasattr(self, '__context__'):
            return ("%s\n\n" % self.message +
                    "Original traceback (most recent call last):\n" +
                    "".join(format_tb(self.traceback)) +
                    "%r" % self.cause)
        else:
            return super(ServiceException, self).__str__()

    def __repr__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if self.cause and not hasattr(self, '__context__'):
            return "ServiceException: %s (from %r)" % (self.message, self.cause)
        else:
            return super(ServiceException, self).__repr__()


class ServiceNetworkException(ServiceException):
    """requests returned an error
    """
    def __init__(self, url, message, status_code, *args, **kwargs):
        """[summary]

        Args:
            url ([type]): [description]
            message ([type]): [description]
            status_code ([type]): [description]
        """
        super(ServiceNetworkException, self).__init__("(%s) %s" % (status_code,
                                                                message),
                                                   *args, **kwargs)
        self.url = url
        self.status_code = status_code
