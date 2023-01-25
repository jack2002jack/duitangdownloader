import json

import requests
header={'user-agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        }
kw="笑容"
num=10
url=f"https://www.duitang.com/napi/blogv2/list/by_search/?kw={kw}after_id={num}"
content = requests.get(headers=header,
                       url=url)
data=json.loads(content.text)["data"]["object_list"]
print(len(data),data)