import graphene

from apps.contact_us.models import Address
from graph_api.contact_us.types import AddressType


class ContactUsQuery(graphene.ObjectType):
    get_contact_address = graphene.Field(AddressType, description="Return the Contact Address")

    def resolve_get_contact_address(self, root, **kwargs):
        """
        Returns Contact Address
        """
        return Address.objects.filter(is_active=True, is_default=True).first()
