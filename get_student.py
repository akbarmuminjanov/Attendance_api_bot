import requests
import json

def get_student_info(id):
    # url = "https://de93-185-196-216-38.ngrok-free.app/student_api/{}/"
    # url = "https://ffbe-94-158-59-37.ngrok-free.app/student_api/{}/"
    # url = "https://b321-94-158-59-37.ngrok-free.app/student_api/{}/"
    url = "https://dc6d-185-139-138-6.ngrok-free.app/student_api/{}/"


    response = requests.get(url=url.format(id))

    data = json.loads(response.text)
    
    return data
