from zope.interface import implements
from zope import schema

from plone.dexterity.content import Container
from plone.supermodel import model
from plone.dexterity.schema import DexteritySchemaPolicy

from . import _


class IPosition(model.Schema):
    """ """

    position_type = schema.Choice(
        title=_("Type"),
        vocabulary="PositionTypes",
        )


class Position(Container):
    """ """
    implements(IPosition)


class PositionSchemaPolicy(DexteritySchemaPolicy):
    """ """

    def bases(self, schemaName, tree):
        return (IPosition,)