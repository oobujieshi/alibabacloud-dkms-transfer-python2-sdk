# -*- coding: utf-8 -*-
from aliyunsdkcore.acs_exception.exceptions import ClientException, ServerException

INVALID_PARAM_ERROR_CODE = "InvalidParam"

UNAUTHORIZED_ERROR_CODE = "Unauthorized"

MISSING_PARAMETER_ERROR_CODE = "MissingParameter"

INVALID_PARAMETER_ERROR_CODE = "InvalidParameter"

FORBIDDEN_KEY_NOT_FOUND_ERROR_CODE = "Forbidden.KeyNotFound"

INVALID_PARAMETER_KEY_SPEC_ERROR_MESSAGE = "The specified parameter KeySpec is not valid."

INVALID_PARAM_DATE_ERROR_MESSAGE = "The Param Date is invalid."

INVALID_PARAM_AUTHORIZATION_ERROR_MESSAGE = "The Param Authorization is invalid."

error_code_dict = dict()
error_code_dict[FORBIDDEN_KEY_NOT_FOUND_ERROR_CODE] = "The specified Key is not found."
error_code_dict["Forbidden.NoPermission"] = "This operation is forbidden by permission system."
error_code_dict["InternalFailure"] = "Internal Failure"
error_code_dict["Rejected.Throttling"] = "QPS Limit Exceeded"


def transfer_error_message(error_code):
    return error_code_dict.get(error_code)


def transfer_invalid_date_exception():
    return ServerException("IllegalTimestamp",
                           "The input parameter \"Timestamp\" that is mandatory for processing this request is not supplied.")


def transfer_invalid_access_key_id_exception():
    return ServerException("InvalidAccessKeyId.NotFound", "The Access Key ID provided does not exist in our records.")


def transfer_incomplete_signature_exception():
    return ServerException("IncompleteSignature", "The request signature does not conform to Aliyun standards.")
