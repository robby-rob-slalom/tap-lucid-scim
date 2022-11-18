"""REST client handling, including LucidSCIMStream base class."""

from typing import Any, Dict, Optional
from memoization import cached
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import BearerTokenAuthenticator
from tap_lucid_scim.pagination import LucidScimPaginator


API_URL = 'https://users.lucid.app/scim/v2'
PAGINATION_INDEX = 1


class LucidSCIMStream(RESTStream):
    """LucidSCIM stream class."""

    @property
    def url_base(self) -> str:
        return self.config.get('api_url', API_URL)

    records_jsonpath = '$[*]'

    @property
    @cached
    def authenticator(self) -> BearerTokenAuthenticator:
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token = self.config.get('api_key')
        )

    @property
    def http_headers(self) -> dict:
        headers = {}
        
        if self.congig.get('user_agent'):
            headers['User-Agent'] = self.config.get('user_agent')

        return headers

    def get_new_paginator(self) -> LucidScimPaginator:
        limit = self.config.get('max_results')
        return LucidScimPaginator(start_value=PAGINATION_INDEX, page_size=limit)

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        return {
            'startIndex': next_page_token or PAGINATION_INDEX,
            'count': self.config.get('max_results')
        }   

