import os
import validators
from django.core.exceptions import ValidationError
from graphql import GraphQLError


def validate_mobile_number(mobile_number):
    """
    Validates the mobile number.
    """
    if len(mobile_number) != 10 or not mobile_number.isdigit():
        raise GraphQLError("Please enter a valid phone number")
    if mobile_number[0] not in ['6', '7', '8', '9']:
        raise GraphQLError("Please enter a valid phone number")
    return mobile_number


def validate_url(url: str):
    """
    Used to Validate the URL while importing excel
    :params: url
    :returns: True if valid or Validation Error
    """
    if validators.url(url):
        return True
    raise ValidationError("Please enter a valid URL")


def validate_video(video_size: int):
    """
    used to validate the video's size
    """
    video_size_limit = os.environ.get("VIDEO_UPLOAD_SIZE", 60000000)
    if video_size > int(video_size_limit):
        raise ValidationError(f"Video file size should not exceed {round(int(video_size_limit) / 1000000)} MB")


def validate_image(image_sizes: list):
    """
    used to validate the image's size
    """

    def validate_image_size(image_size):
        image_size_limit = os.environ.get("IMAGE_UPLOAD_SIZE", 10000000)
        if image_size > int(image_size_limit):
            raise ValidationError(f"Image file size should not exceed {round(int(image_size_limit) / 1000000)} MB")

    list(map(validate_image_size, image_sizes))

    return None


def validate_video_upload(hosted_video, provider_url, provider):
    """
    :param hosted_video: optional
    :param provider_url: optional
    :param provider: optional
    :return: None
    :raise: Error when uploading the both provider url and hosted video
            or upload a provider url without provider info
    """

    if (provider and hosted_video) or (provider_url and hosted_video):
        raise ValidationError("please provide either provider or hosted video")
    if (not provider_url and provider) or (not provider and provider_url):
        raise ValidationError("please provide the Provider URL or Provider")

    return None
