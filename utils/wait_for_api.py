import json
import time

def wait_for_get_api(driver, keyword, timeout=10):
    start_time = time.time()
    request_id = None

    while time.time() - start_time < timeout:
        logs = driver.get_log("performance")

        for log in logs:
            message = json.loads(log["message"])["message"]
            #print(f'\n\n\nMESSSAGE LOGGGS:   {log}\n\n\n')
            if message["method"] == "Network.requestWillBeSent" and message["params"]["type"] in ["XHR", "Fetch"] and message["params"]["timestamp"] < start_time*1000:
                if keyword in message["params"]["request"]["url"]:
                    #print(f'\n\n\nMESSAGE1: \n{message}\n\n\n')
                    request_id = message["params"]["requestId"]
            if message["method"] == "Network.responseReceived" and message["params"]["type"]  in ["XHR", "Fetch"] and message["params"]["timestamp"] < start_time*1000:
                if message["params"]["requestId"] == request_id:
                    #print(f'\n\n\nMESSAGE2: \n{message}\n\n\n')
                    response_body = driver.execute_cdp_cmd(
                        "Network.getResponseBody",
                        {"requestId": request_id}
                    )
                    return json.loads(response_body["body"])
        time.sleep(0.3)
    raise TimeoutError(f"API '{keyword}' not found")
