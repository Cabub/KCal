# coding: utf-8
import requests
from requests.auth import HTTPBasicAuth

class NALClient:

    def __init__(self, api_key):
        self._base_url = 'https://api.nal.usda.gov'
        self._auth = HTTPBasicAuth(api_key, None)
        self._search_path = '/ndb/search'
        self._report_path = '/ndb/V2/reports'
        self._headers = {'Content-Type': 'application/json'}
    
    def search(self, query, ds='Standard Reference', max_results=500, offset=0):
        response = requests.get(
            self._base_url + self._search_path,
            auth=self._auth,
            headers=self._headers,
            json={
                'q': str(query),
                'max': str(max_results),
                'offset': str(offset),
                'ds': str(ds)
            }
        )
        response.raise_for_status()
        return response.json()

    def report(self, ndbno, q_type='b'):
        response = requests.get(
            self._base_url + self._report_path,
            auth=self._auth,
            headers=self._headers,
            params={
                'ndbno': [ndbno],
                'type': q_type
            }
        )
        response.raise_for_status()
        return response.json()
