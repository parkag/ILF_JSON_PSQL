import json;

obj = json.loads("""{
 "betaArray": {"value": [0, 0, 0, 0, 1, 2], "pragma": "replace"},
 "whatever": {"value": [3.1415], "pragma": "append"},
 "experimentState": {"value": "Acquiring", "pragma": "transient"},
 "acquiring": {"value": "Acquiring", "pragma": "transient"}
}""");

print 'Przykladowy obiekt json jako obiekt pythona:'
print obj
print '\nZ powrotem json.dumps(obj)'
print json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
