import token
from typing import Any, Dict, Optional
import requests
from requests import Response
import os
import re
from utils.config_reader import ConfigReader

class ApiHelper:

    @staticmethod
    def base_api_url():
        if os.getenv("BASE_API_URL"):
            base_api_url = os.getenv("BASE_API_URL")
        else:
            base_api_url = ConfigReader.get_base_api_url()
        return base_api_url

    @staticmethod
    def get(endpoint: str,params: Optional[Dict[str, Any]] = None, **kwarg ):
        api_url = ApiHelper.base_api_url()+ endpoint
        return requests.get(api_url, params=params, **kwarg)

    @staticmethod
    def post(endpoint: str, payload: Optional[Dict[str, Any]] = None, **kwarg):
        api_url = ApiHelper.base_api_url() + endpoint
        return requests.post(api_url, json=payload, **kwarg)

    @staticmethod
    def put(endpoint: str, payload: Optional[Dict[str, Any]] = None, **kwarg):
        api_url = ApiHelper.base_api_url() + endpoint
        return requests.put(api_url, json=payload, **kwarg)

    @staticmethod
    def delete(endpoint: str, params: Optional[Dict[str, Any]] = None, **kwarg):
        api_url = ApiHelper.base_api_url() + endpoint
        return requests.delete(api_url, params=params, **kwarg)






    

    
    
  