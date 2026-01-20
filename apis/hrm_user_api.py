from utils.api_helper import ApiHelper

class HRMUserApi:
    @staticmethod
    def get_all_users(driver):
        params ={
            "limit":50,
            "offset": 0,
            "userRoleId": 1,
            "sortField": "u.username",
            "sortOrder": "ASC" }
        cookies = {c["name"]: c["value"] for c in driver.get_cookies()}
        cookies = f"{cookies.keys()}={cookies.values()}"

        headers = {
                "Accept": "application/json",
                "Accept-Encoding":  "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "no-store, no-cache, must-revalidate, post-check=0, pre-check=0",
                "Connection": "keep-alive",
                "cookie": cookies,
                "Host": "opensource-demo.orangehrmlive.com",
                "Referer": "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
        }

        return ApiHelper.get('admin/users', params, headers)


