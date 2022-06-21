from saagieapi import SaagieApi

SAAGIE_USER_NAME = "ESTIAM_G14_elie-denis.dechasse"
SAAGIE_USER_PASSWORD = "Hackathon2022"
URL_SAAGIE_PLATFORM = "https://demo-workspace.a4.saagie.io/projects/platform/2/"

API = SaagieApi.easy_connect(url_saagie_platform=URL_SAAGIE_PLATFORM,
                user=SAAGIE_USER_NAME,
                password=SAAGIE_USER_PASSWORD)