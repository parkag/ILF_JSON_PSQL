import json;
def is_json(json_string):
	try:
		obj = json.loads(json_string);
		return True
	except:
		return False



json_str = """{
		"betaArray": {"value": [0, 0, 0, 0, 1, 2], "pragma": "replace"},
		"whatever": {"value": [3.1415], "pragma": "append"},
		"experimentState": {"value": "Acquiring", "pragma": "transient"},
		"acquiring": {"value": "Acquiring", "pragma": "transient"}
		}"""
print json_str
print is_json(json_str)

json_str = "Im not a json!{}"
print json_str
print is_json(json_str)


