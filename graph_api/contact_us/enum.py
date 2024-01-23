import graphene


class EnquiryTypeEnum(graphene.Enum):
    """
    The EnquiryType Enum defines the Enquiry Types during Submit Enquiries
    """
    GENERAL_ENQUIRY = "GENERAL ENQUIRY"
    OVERALL_PACKAGE = "OVERALL PACKAGE"
    BRAND_PARTNERS = "BRAND PARTNERS"
    OTHERS = "OTHERS"
