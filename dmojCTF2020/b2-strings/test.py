import requests
url = "https://hashingroll.free.beeceptor.com"
requests.post(url, json={
    'recv': 'Hello from ACTUAL dmoj'
})
