from zope.schema import Bytes
from zope.interface import Interface
from Products.PloneFormGen import PloneFormGenMessageFactory as _

class IImportSchema(Interface):
    """Schema for form import.
    """
    upload = Bytes(
        title=_(u'Upload'),
        required=False)

class IImportForm(Interface):
    """Interface for import form
    """
