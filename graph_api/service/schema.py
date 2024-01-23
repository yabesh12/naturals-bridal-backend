import graphene
from apps.service.models import Service
from graph_api.service.type import ServiceType


class ServicesQuery(graphene.ObjectType):
    get_services = graphene.List(ServiceType, description="Returns a list of Services")
    get_service = graphene.relay.Node.Field(ServiceType, description="Get specific Service and it's Items")

    def resolve_get_services(self, root):
        """
        :return: All the Active Services
        """
        return Service.objects.filter(is_active=True)
