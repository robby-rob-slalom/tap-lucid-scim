"""LucidSCIM tap class."""

from typing import List
from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_lucid_scim.streams import (
#    LucidSCIMStream,
    UsersStream,
    GroupsStream,
)

STREAM_TYPES = [
    UsersStream,
    GroupsStream,
]


class TapLucidSCIM(Tap):
    """LucidSCIM tap class."""
    name = 'tap-lucid-scim'

    config_jsonschema = th.PropertiesList(
        th.Property(
            'auth_token',
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description='The token to authenticate against the API service'
        ),
        th.Property(
            'max_results',
            th.IntegerType,
            default=100,
            description='Result limit for paginated streams'
        ),
        #th.Property(
        #    'start_date',
        #    th.DateTimeType,
        #    description='The earliest record date to sync'
        #),
        th.Property(
            'api_url',
            th.StringType,
            description='Override the API base URL'
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == '__main__':
    TapLucidSCIM.cli()
