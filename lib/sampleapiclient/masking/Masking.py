import json
from authenticationsdk.util.GlobalLabelParameters import *


# This method reads the items to be masked and accordingly masks the response from the server
def masking(r):
    try:
        j = json.loads(r)

        maskdata = json.dumps(
            remove_key(j, "expirationMonth", "expirationYear", "email", "firstName", "lastName", "phoneNumber",
                       "number", "securityCode", "type"))

        return maskdata
    except ValueError as e:
        return r


# This function replaces the value of the items to be masked to "XXXXX"
def remove_key(obj, *keys):
    if type(obj) is dict:
        for k, v in list(obj.items()):
            if k not in keys:
                obj[k] = remove_key(v, *keys)
                obj[k] = v
            else:
                obj[k] = GlobalLabelParameters.MASKING_VALUE

        return obj
