import json

objs = []

objs.append(json.loads("""{
     "betaArray": {"value": [0, 0, 0, 0, 1, 2], "pragma": "replace"},
     "whatever": {"value": [3.1415], "pragma": "append"},
     "experimentState": {"value": "Acquiring", "pragma": "transient"},
     "acquiring": {"value": "Acquiring", "pragma": "transient"}
}"""));

objs.append(json.loads("""{
	"betaArray": {"value": [3,4,5,6], "pragma": "append"},
	"whatever": {"value": [5.0], "pragma": "replace"},
	"experimentState": {"value": "Completed", "pragma": "transient"}
}"""));

#just stubs
for obj in objs:
	for x in obj.keys():
		if obj[x]["pragma"]=="append":
			print "appending to '%s': %s" %(x, obj[x]["value"])
		elif obj[x]["pragma"]=="replace":
			print "replacing prev '%s' val with: %s" %(x, obj[x]["value"])
		elif obj[x]["pragma"]=="transient":
			pass

