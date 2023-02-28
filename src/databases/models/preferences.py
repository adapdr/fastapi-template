"""
File contains preferences model
"""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin, UUIDPrimaryKeyMixin


class PreferencesModel(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    """
    Database ORM Model for 'preferences'
    """

    # __connection__ = 'NAME'
    __table__ = "preferences"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    __hidden__ = ["created_at", "updated_at", "deleted_at"]
