from authenticationsdk.payloaddigest.PayLoadDigest import *
import authenticationsdk.util.ExceptionAuth
from authenticationsdk.core.ExceptionHandling import *
from authenticationsdk.util.GlobalLabelParameters import *
import json


def json_file_data(path, mconfig):
    logger = mconfig.log
    try:
        if path == "" or path is None:
            raise ApiException(0, GlobalLabelParameters.REQUEST_JSON_EMPTY)

        else:
            digest_obj = DigestAndPayload()
            return digest_obj.string_payload_generation(path)
    except IOError as e:

        authenticationsdk.util.ExceptionAuth.log_exception(logger,
                                                           GlobalLabelParameters.REQUEST_JSON_ERROR + str(e.filename),
                                                           mconfig)

