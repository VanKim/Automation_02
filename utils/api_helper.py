# ...existing code...
import logging
from typing import Any, Dict, Optional
import requests
#from requests.adapters import HTTPAdapter
#from urllib3.util.retry import Retry
from utils.config_reader import ConfigReader

class ApiHelper:
    
    @staticmethod
    def get(self,path: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, timeout: int = 10) -> Dict[str, Any]:
        url = ConfigReader.get_api_url() + path + str(params["id"])
        print(url)
        return requests.get(url)
    






    

    
    
  