import requests

url = "https://live-traffic-images.p.rapidapi.com/get_image"

querystring = {"country":"us","key":"655"}

headers = {
	"X-RapidAPI-Key": "f77f0b1749mshd25c48ccfe40b04p1b6b57jsna5e1f05fe13f",
	"X-RapidAPI-Host": "live-traffic-images.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

url_1 = "https://live-traffic-images.p.rapidapi.com/get_camera_list"

querystring_1 = {"country":"us"}

headers_1 = {
	"X-RapidAPI-Key": "f77f0b1749mshd25c48ccfe40b04p1b6b57jsna5e1f05fe13f",
	"X-RapidAPI-Host": "live-traffic-images.p.rapidapi.com"
}

response_1 = requests.request("GET", url_1, headers=headers_1, params=querystring_1)