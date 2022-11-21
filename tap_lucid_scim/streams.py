"""Stream type classes for tap-lucid-scim."""

from pathlib import Path
from tap_lucid_scim.client import LucidSCIMStream


SCHEMAS_DIR = Path(__file__).parent / Path('./schemas')


class UsersStream(LucidSCIMStream):
    """Define custom stream."""
    name = 'users'
    path = '/Users'
    primary_keys = ['id']
    replication_key = None
    records_jsonpath = '$.Resources[*]'
    schema_filepath = SCHEMAS_DIR / 'users.json'


class GroupsStream(LucidSCIMStream):
    """Define custom stream."""
    name = 'groups'
    path = '/Groups'
    primary_keys = ['id']
    replication_key = None
    records_jsonpath = '$.Resources[*]'
    schema_filepath = SCHEMAS_DIR / 'groups.json'
