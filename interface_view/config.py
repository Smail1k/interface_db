import pyautogui

width = pyautogui.size()[0]

width_70 = pyautogui.size()[0] * 0.7
height_80 = pyautogui.size()[1] * 0.8

aws_endpoint_url = "https://s3.us-east-005.example.com"
aws_bucket_key_id = "your_awd_bucket_key_id"
aws_application_key = "your_application_key"
server_endpoint = "http://your.address.server.host"

token = None
type_field = None
status = False
