# ...existing code...
import logging
from typing import Any, Dict, Optional
import requests
from utils.config_reader import ConfigReader

class ApiHelper:
    
    @staticmethod
    def get(self,path: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, timeout: int = 10):
        url = ConfigReader.get_api_host() + path
        if params:
            url = url + str(params["id"])
        return requests.get(url)
    






    

    
    
  