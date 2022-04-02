import requests
import zipfile
import io

def get_qualtrics_survey(dir_save_survey, survey_id):
    """ automatically query the qualtrics survey data
    taken from: https://gist.github.com/FedericoTartarini/9496282b4b2f508c0ab2da96f4955397
    guide: https://community.alteryx.com/t5/Alteryx-Designer-Discussions/Python-Tool-Downloading-Qualtrics-Survey-Data-using-Python-API/td-p/304898
    api: https://api.qualtrics.com/api-reference/b3A6NjA5OTQ-legacy-create-response-export """

    """ at some point this API might no longer work. this is the link to the updated API. I'm not doing this now, but at some point if I need to here it is:
    new api: https://api.qualtrics.com/api-reference/YXBpOjYwOTI5-surveys-response-import-export-api """

    # Setting user Parameters
    api_token = "wrsAVkCacuCXdr4T4ytrg7GaycHOPiWYjou4D2wZ"
    file_format = "csv"
    data_center = 'usu.co1' # "<Organization ID>.<Datacenter ID>"
    recode_value = "0"
    ## Response ID Parameter
    file = open("../data/response_id.txt")
    response_ID = file.read() # '","lastResponseId":"' + response_ID  +
    file.close()

    # Setting static parameters
    request_check_progress = 0
    progress_status = "in progress"
    base_url = "https://{0}.qualtrics.com/API/v3/responseexports/".format(data_center)
    headers = {
        "content-type": "application/json",
        "x-api-token": api_token,
    }

    # Step 1: Creating Data Export
    download_request_url = base_url
    download_request_payload = '{"format":"' + file_format + '","surveyId":"' + survey_id + '","seenUnansweredRecode":"' + recode_value + '","lastResponseId":"' + response_ID + '"}' # you can set useLabels:True to get responses in text format
    download_request_response = requests.request("POST", download_request_url, data=download_request_payload, headers=headers)
    progress_id = download_request_response.json()["result"]["id"]
    # print(download_request_response.text)

    # Step 2: Checking on Data Export Progress and waiting until export is ready
    while request_check_progress < 100 and progress_status != "complete":
        request_check_url = base_url + progress_id
        request_check_response = requests.request("GET", request_check_url, headers=headers)
        request_check_progress = request_check_response.json()["result"]["percentComplete"]

    # Step 3: Downloading file
    request_download_url = base_url + progress_id + '/file'
    request_download = requests.request("GET", request_download_url, headers=headers, stream=True)

    # Step 4: Unzipping the file
    zipfile.ZipFile(io.BytesIO(request_download.content)).extractall(dir_save_survey)
    print('Downloaded qualtrics survey')

if __name__ == "__main__":

    path = "../data/"

    get_qualtrics_survey(dir_save_survey = path, survey_id = "SV_3fxVsxTkGZde6bk")