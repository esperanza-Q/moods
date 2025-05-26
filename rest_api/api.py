import requests, json
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()

kakaoapi=os.getenv('REST_API')

def get_location(address):
    url="https://dapi.kakao.com/v2/local/search/address.json?query="+address
    headers={"Authorization": f"KakaoAK {kakaoapi}"}
    
    try:
        response = requests.get(url, headers=headers)
        json_result = response.json()
        print(json.dumps(json_result, indent = 4, ensure_ascii = False))
        
        address_xy = json_result['documents'][0]['address']
                
        return float(address_xy['x']), float(address_xy['y'])
    
    except Exception as e:
        print(e)
        return 0, 0