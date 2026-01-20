# ...existing code...
import logging
from typing import Any, Dict, Optional
import requests
from requests import Response

from utils.config_reader import ConfigReader

class ApiHelper:
    
    @staticmethod
    def get(path: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, timeout: int = 10):
        api_url = ConfigReader.get_base_api_url() + path
        return requests.get(api_url, params = params, headers=headers, timeout=timeout)

    @staticmethod
    def post(path: str, payload: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None,
            timeout: int = 10):
        url = ConfigReader.get_base_api_url() + path
        return requests.post(url, json=payload, headers=headers, timeout=timeout)

    @staticmethod
    def put(path: str, payload: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None,
             timeout: int = 10):
        url = ConfigReader.get_base_api_url() + path
        return requests.put(url, json=payload, headers=headers, timeout=timeout)

    @staticmethod
    def delete(path: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None,
            timeout: int = 10):
        api_url = ConfigReader.get_base_api_url() + path
        return requests.delete(api_url, params=params, headers=headers, timeout=timeout)

    #patch method viết sau




    

    
    
  