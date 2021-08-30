from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from django.shortcuts import redirect, render
from django.http import JsonResponse


class MainGlassView(TemplateView):
    """
    Start page
    """
    template_name = 'test/glass_start_link.html'

    # template_name = 'test/indee_main.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        response = TemplateResponse(request, self.template_name, {}, status=HTTP_200_OK)
        response.set_cookie("csrftoken", "8888888888888888888")
        response.set_cookie("mid", "333333333333333333333333333")
        response.set_cookie("rur", "Alex-4000")
        response.set_cookie("_csrftoken", "8888888888888888888")
        response.set_cookie("__csrftoken", "8888888888888888888")
        response.set_cookie("___csrftoken", "8888888888888888888")

        return response


class JobGlassView(TemplateView):
    """
    Job page(click Easy Apply button)
    """
    template_name = 'test/glass_job_link1.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        response = TemplateResponse(request, self.template_name, {}, status=HTTP_200_OK)
        response.set_cookie("csrftoken", "8888888888888888888")
        response.set_cookie("mid", "333333333333333333333333333")
        response.set_cookie("rur", "Alex-4000")
        response.set_cookie("_csrftoken", "8888888888888888888")
        response.set_cookie("__csrftoken", "8888888888888888888")
        response.set_cookie("___csrftoken", "8888888888888888888")

        return response


class FormJobGlassView(TemplateView):
    """
    GET Form page
    """
    template_name = 'test/glass_form_link.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        response = TemplateResponse(request, self.template_name, {}, status=HTTP_200_OK)
        response.set_cookie("csrftoken", "8888888888888888888")
        response.set_cookie("mid", "333333333333333333333333333")
        response.set_cookie("rur", "Alex-4000")
        response.set_cookie("_csrftoken", "8888888888888888888")
        response.set_cookie("__csrftoken", "8888888888888888888")
        response.set_cookie("___csrftoken", "8888888888888888888")

        return response


class TestDataSaveGlass(CreateView):
    template_name = 'test/glass_form_link1.html'

    def post(self, request, *args, **kwargs):
        print(4000)
        print(request.FILES)
        return render(request, self.template_name)


class PrevDataSaveGlass(CreateView):

    def post(self, request, *args, **kwargs):
        print(5000)
        print(request.FILES)
        res = {"attachmentHashes": [],
               "resumeFileHash": "256f9d0a99cf1854ab0124b14732de8a36a53a2e0ca88945c2b1ec3d06cc6335",
               "questionAttachmentHashes": [],
               "previewResponse": {"skipped": "false", "success": 'true', "hasApplied": 'false', "failed": 'false',
                                   "status": "SUCCESS", "validationResult": 'null',
                                   "previewData": {
                       "job": {"jobTitle": "Staffing Coordinator/Administrative Assistant",
                               "jobCompany": "Westminster Canterbury Richmond", "jobLocation": "Richmond, VA 23227",
                               "jobId": "35f4b38f6882380d7db2",
                               "jobUrl": "https://www.glassdoor.com/partner/jobListing.htm?pos=129&ao=1136043&s=58&guid=0000017b96bd1ca79dbbe774cb6e3f25&src=GD_JOB_AD&t=SR&vt=w&ea=1&cs=1_44df5a8e&cb=1630321615878&jobListingId=1007265226779&jrtk=2-0-1febbq76iu4km801-1febbq775u3rs800-e33681510317f2b7",
                               "jobKey": "e33681510317f2b7"},
                       "applicant": {"fullName": "Alex Tan", "email": "cruz-fl@bk.ru",
                                     "emailAlias": "alextan692_3w8@indeedemail.com",
                                     "phoneNumber": "4564564564",
                                     "location": {"country": "US", "city": "Nikolaev"},
                                     "verified": 'false'},
                       "questions": {"url": "iq://35f4b38f6882380d7db2?v=1", "retrievedOnMillis": 1630321619881,
                                     "questions": [
                                         {"id": "AAAAAQRFt8QRRN5-XcUuTX4YIXDpGHDPB9hS3rGgsnaskYFdPUz8hQ==",
                                          "question": "This is an employer-written question. You can report inappropriate questions to "
                                                      "Indeed through the \"Report Job\" link at the bottom of the job description. "
                                                      "<br><br> \"Have you received your COVID-19 vaccination?\"",
                                          "type": "textarea", "required": 'false', "condition": 'null', "options": [],
                                          "format": 'null',
                                          "min": 'null', "max": 'null', "limit": "1500", "text": 'null',
                                          "fontsize": 'null',
                                          "hierarchicalOptions": []}], "answers": [
                               {"id": "AAAAAQRFt8QRRN5-XcUuTX4YIXDpGHDPB9hS3rGgsnaskYFdPUz8hQ==", "value": "",
                                "values": 'null',
                                "hierarchicalAnswers": 'null', "files": 'null'}]},
                       "id": "3d30da0a5777fd5e98bfad5801611d25a2f7f44ac63c7c510cace3277f6b99df",
                       "analytics": {"referer": "", "ip": "46.33.244.27", "advNum": "5127157419703776",
                                     "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
                                     "device": "desktop", "sponsored": 'false',
                                     "proctorGroups": "acme_jobs_indeed_apply_tst0,crashtext10tst2,crashtext25tst3,crashtext50tst1,crashtext5tst16,hpblendedtst1,ia_sa_holdout_tst1,ia_saqualityapi_tst1,ia_smartapplyglobalnav_tst1,ia_viewform_jobsapi_tst1,iaapplyformglassdoortst3,iaapplyurllenlimittst1,iaconfirmationjanustst15,iadradismultiattachtst3,iaexpiresessiontst1,iaimprovepreviewscreentst1,iaja_smartapplyplacement_tst7,iajobalertsmosaictst1,iajsprofileapitst1,iapartnerkillswitch0,iapreviewapitst1,iapreviewreportissuetst5,iareuseautoshowiauidtst1,iascreenerquestionstst2,iashowaliastst1,iasmartapplycdntst1,iasmartapplym5tst1,iasmartapplypartnertst2,iasmartapplypreloadtst1,iasmartapplysqfirsttst2,iasuccesspageglassdoortst1,iatitlecompanyandlocationfieldstst1,jobclickpassadblobtoviewjoburl1,jsj_hp_csrftog2,jsj_hp_noqueryerror_0220_tst1,jsj_hp_rjp_matrix_tst1,jsj_jcs_tst1,jsj_mobhp_explainjob_0920_tst3,jsj_mobhp_feedtimeout_v1_1119_tst5,jsj_mobhp_frontendrqparsing_0630_tst1,mobpassadblobtosjapplystarturl1,mosaic_apptracker_platform_tog1,mosaic_click_tracking_body_tst1,mosaic_cmieuro_job_inquiry_ifl_tst1,mosaic_commonstatics_proto_jobsearch_tst0,mosaic_gs_session_manager_provider_tog1,mosaic_ita_apptracker_tog0,mosaic_ita_mobilehp_tog0,mosaic_jasx_jcs_tst1,mosaic_mobserp_acme_collection_tog2,mosaic_platform_page_state_tog1,mosaic_platform_phasedinit_tog1,mosaic_provider_company_info_mobvj_feedback_tst1,mosaic_provider_dislike_feedback_tog1,mosaic_provider_serpreportjob_tog1,sem_apply_starts_ga_tst1,subw_edit_redirect_tst1,#A7:acme_jobs_indeed_apply_tst0,#A1:crashtext10tst2,#A2:crashtext25tst3,#A1:crashtext50tst1,#A1:crashtext5tst16,#B6:hpblendedtst1,#A6:ia_sa_holdout_tst1,#E4:ia_saqualityapi_tst1,#B2:ia_smartapplyglobalnav_tst1,#A4:ia_viewform_jobsapi_tst1,#A13:iaapplyformglassdoortst3,#A13:iaapplyurllenlimittst1,#H5:iaconfirmationjanustst15,#A15:iadradismultiattachtst3,#A5:iaexpiresessiontst1,#B4:iaimprovepreviewscreentst1,#B3:iaja_smartapplyplacement_tst7,#A22:iajobalertsmosaictst1,#A4:iajsprofileapitst1,#A1:iapartnerkillswitch0,#B4:iapreviewapitst1,#A6:iapreviewreportissuetst5,#A5:iareuseautoshowiauidtst1,#B8:iascreenerquestionstst2,#B7:iashowaliastst1,#A3:iasmartapplycdntst1,#O17:iasmartapplym5tst1,#B2:iasmartapplypartnertst2,#A11:iasmartapplypreloadtst1,#A6:iasmartapplysqfirsttst2,#A7:iasuccesspageglassdoortst1,#B13:iatitlecompanyandlocationfieldstst1,#A9:jobclickpassadblobtoviewjoburl1,#A1:jsj_hp_csrftog2,#C2:jsj_hp_noqueryerror_0220_tst1,#B6:jsj_hp_rjp_matrix_tst1,#D3:jsj_jcs_tst1,#A5:jsj_mobhp_explainjob_0920_tst3,#A8:jsj_mobhp_feedtimeout_v1_1119_tst5,#B4:jsj_mobhp_frontendrqparsing_0630_tst1,#A8:mobpassadblobtosjapplystarturl1,#B2:mosaic_apptracker_platform_tog1,#B2:mosaic_click_tracking_body_tst1,#A4:mosaic_cmieuro_job_inquiry_ifl_tst1,#A1:mosaic_commonstatics_proto_jobsearch_tst0,#A2:mosaic_gs_session_manager_provider_tog1,#A3:mosaic_ita_apptracker_tog0,#A4:mosaic_ita_mobilehp_tog0,#C7:mosaic_jasx_jcs_tst1,#B7:mosaic_mobserp_acme_collection_tog2,#A4:mosaic_platform_page_state_tog1,#A7:mosaic_platform_phasedinit_tog1,#A3:mosaic_provider_company_info_mobvj_feedback_tst1,#A1:mosaic_provider_dislike_feedback_tog1,#A6:mosaic_provider_serpreportjob_tog1,#A3:sem_apply_starts_ga_tst1,#A6:subw_edit_redirect_tst1,iarezpromo,iatwopanetst-1,iatwopanevjtst-1"},
                       "appliedOnMillis": 1630321681830, "locale": "ru_UA"},
                                   "previewJson": "{\"id\":\"3d30da0a5777fd5e98bfad5801611d25a2f7f44ac63c7c510cace3277f6b99df\",\"job\":{\"jobTitle\":\"Staffing Coordinator/Administrative Assistant\",\"jobCompany\":\"Westminster Canterbury Richmond\",\"jobLocation\":\"Richmond, VA 23227\"},\"applicant\":{\"fullName\":\"Alex Tan\",\"email\":\"cruz-fl@bk.ru\",\"emailAlias\":\"alextan692_3w8@indeedemail.com\",\"phoneNumber\":\"4564564564\",\"location\":{\"country\":\"US\",\"city\":\"Nikolaev\"},\"resume\":{\"file\":{\"fileName\":\"resume (1).docx\",\"downloadUrl\":\"https://apply-preview.indeed.com/indeedapply/applicationpreview/attachment?apiToken=aa102235a5ccb18bd3668c0e14aa3ea7e2503cfac2a7a9bf3d6549899e125af4&iaUid=1febbr9mmtv2t802&previewUid=1febbt911qpes800&id=256f9d0a99cf1854ab0124b14732de8a36a53a2e0ca88945c2b1ec3d06cc6335&fileToken=epJMxg5NjnBIWVkMTabZtRMCvK8Y74pmgkNkv5W3M9LggmEIT7-aOaHYiHvjFOPi_0Vs6XxuvpIr-NJRY4L-f4Oelo9Vqd1XGHZdJXFwedG4v1EsOx53oOKFvmLTuV2jcR02pCCP78KGA1tMIwNDLzxhNV57rafQAEvzXjl3tmypPtftjPWBYiRwWCfSL0hguwq-S6RTuBKa9bzXjBzNiv2t23R1ZH5pVBpkgjFLyeC9FHOeRqfNj3foUESy1JshJ-TYpa4jEsoONepxpd6smZYOON2xOl1ofvBJlUkJjP_roHUSnWpRA0Ft9D-liTDLCKGto0tXLB0XJqyxRN1VQYk17enF2-8U2rRsUkAfKIat2lwoaOqfHqO6cAD-TKQjrcl34pLNQvcSKXpbzjX17OoXRUPKEJzZbvqh-2ejZaTynG-OxI4OHJuTNc5JORVXNQkXHyiVeK6dBvJzSFZEokjqn-B1bTnI\"}}},\"easternOrder\":false}",
                                   "hasAppliedPageUrl": 'null', "submitBaseUrl": "https://dubprod1.apply.indeed.com",
                                   "successPageUrl": "https://conv.indeed.com/pagead/conv/5127157419703776/?rand=1630321681855&ia=1&url=https%3A%2F%2Fapply.indeed.com%2Findeedapply%2Fsuccess%3FjobId%3D35f4b38f6882380d7db2%26jobTitle%3DStaffing%2BCoordinator%252FAdministrative%2BAssistant%26jobCompany%3DWestminster%2BCanterbury%2BRichmond%26jobLocation%3DRichmond%252C%2BVA%2B23227%26jobUrl%3Dhttps%253A%252F%252Fwww.glassdoor.com%252Fpartner%252FjobListing.htm%253Fpos%253D129%2526ao%253D1136043%2526s%253D58%2526guid%253D0000017b96bd1ca79dbbe774cb6e3f25%2526src%253DGD_JOB_AD%2526t%253DSR%2526vt%253Dw%2526ea%253D1%2526cs%253D1_44df5a8e%2526cb%253D1630321615878%2526jobListingId%253D1007265226779%2526jrtk%253D2-0-1febbq76iu4km801-1febbq775u3rs800-e33681510317f2b7%26jobMeta%3D%253CpartnerMeta%253E%2526jobListingId%253D1007265226779%2526adOrderId%253D1136043%2526purchaseAdOrderId%253D0%2526userId%253D0%2526userGuid%253Dddc5fcc4-8448-4787-8404-558b3dc72b44%2526pageGuid%253D0000017b96bda388930a7fe2b22fab11%2526ip%253D46.33.244.27%2526dt%253D1%2526pt%253D3%2526vt%253D4%2526locale%253Den-US%2526from%253Dglassdoor%2526partnerApiToken%253D7cc68c0d955e00fa10943c90dd4b7316f6c038bd1c0e36b666a064fb53aa9d01%2526asid%253Dddc5fcc4-8448-4787-8404-558b3dc72b44.1630321140.0%2526spn%253D0%2526%253C%252FpartnerMeta%253E%26jk%3De33681510317f2b7%26postUrl%3Dhttp%253A%252F%252Fmuffit%252Fprocess-indeedapply%26name%3Dfullname%26phone%3DOPTIONAL%26coverletter%3DOPTIONAL%26continueUrl%3Dhttps%253A%252F%252Fwww.glassdoor.com%252FJob%252Fhuman-resources-jobs-SRCH_KO0%252C15.htm%253FjobType%253Dfulltime%2526fromAge%253D3%2526sgocId%253D1001%26questions%3Diq%253A%252F%252F35f4b38f6882380d7db2%253Fv%253D1%26resume%3DOPTIONAL%26skipContinue%3Dfalse%26co%3DUA%26advNum%3D5127157419703776%26twoPaneGroup%3D-1%26twoPaneVjGroup%3D-1%26iaUid%3D1febbr9mmtv2t802%26apiToken%3Daa102235a5ccb18bd3668c0e14aa3ea7e2503cfac2a7a9bf3d6549899e125af4%26partnerApiToken%3D7cc68c0d955e00fa10943c90dd4b7316f6c038bd1c0e36b666a064fb53aa9d01%26partnerMeta%3D%2526jobListingId%253D1007265226779%2526adOrderId%253D1136043%2526purchaseAdOrderId%253D0%2526userId%253D0%2526userGuid%253Dddc5fcc4-8448-4787-8404-558b3dc72b44%2526pageGuid%253D0000017b96bda388930a7fe2b22fab11%2526ip%253D46.33.244.27%2526dt%253D1%2526pt%253D3%2526vt%253D4%2526locale%253Den-US%2526from%253Dglassdoor%2526asid%253Dddc5fcc4-8448-4787-8404-558b3dc72b44.1630321140.0%2526spn%253D0%2526%26hasOnApplied%3D1%26tk%3D1febbt911qpes800%26applicantName%3D0000000048204dc3cd41b4391a36510fd46993c6213208d3ba1c6d0be6aa50953e7a7fc6b4278f87%26resumeFN%3D0000000037797c92f4b839ecfc97536c20b0fb60ff30e6c44b10d925f566d0dfe37382db1481ebc52edb3e5d05b39a%26id%3D93cb7818b97ab3f9523212190a9ddf1e1f4c62cd468031397aca470a9d8dffd9a697d2de6e05dee191d571398295c629ce27c8e158b6f62b%26apptoken%3D93cb7818b97ab3f93a27a2852207b1a4944d693de2e83f122cdeb11a809907ef02e084d602d90ecabfb3c8b3ca67052d21d296f529a88a50a0570c4620f0d8fa11bec7907f79a1a718b0a1c13a862c18757ac5493055801e3171095caa34a536b06b18f26c73490079c67e5ca91b052201415b726376ba67ad3fc6d1c831a628111253b06ecf2577c50c258755bde332abeeaac441b6405a5689b5f4893cc2f7c162053f23a3ea08cb83a18652e57724ddc825b950488794fdf98daa9608d1e65dcbf1087b5cf6351ceee2e895c5eb9b05fbd20b26763482028ef0b26344f4f03b2fdf5b3071c8a55e300a5816bfadc46afa90e799b2c0b5b45b696ac4b23a372a54d33f3e28ae7b5c3b61dc8a5595fa4e52d2b8f0251df82034b7083c37b0940e187a52def69851f65283b4db5919802eaa729b91e5c2c7052f3a23f295e459f01045692fe3fdfdb165e5fa67a08de1d40e7b38e9422a9636337893bd4d73a58b23c5c7456bfdf09c1ad59f0a3ee3e5c4cd565f4a59f36219f9fcd9a588089f66f40a5b32089349a90eaea5e405ce24a6f80de46f1796abdebceb6907f24bdcacae9405d5d9c6e6a778e6cbc9509550c6c6e2ba95401478193bc1bbee5b396493a6507de316ba7221bf35e4467f9dd432575533da091b1ed0b7775a5134986f817ba3313a3da7401fc67d6a771c9436dca9980d552bbb55%26email%3D0000000004b43e22e00f43a49ed685271e1a2febd8f2095ea2fa0e50e581c138cdf5c25113e0df1f3b1fc8d22f%26contentType%3Dapplication%252Fvnd.openxmlformats-officedocument.wordprocessingml.document%26iip%3D0",
                                   "resumeType": "FILE_UPLOADED_RESUME",
                                   "previewUid": "1febbt911qpes800",
                                   "htmlResume": 'null',
                                   "nigmaResults": {},
                                   "jobTaxonomyEntities": [],
                                   "resumeIAAttachmentHash": {
                                         "id": "256f9d0a99cf1854ab0124b14732de8a36a53a2e0ca88945c2b1ec3d06cc6335",
                                         "fileToken": "epJMxg5NjnBIWVkMTabZtRMCvK8Y74pmgkNkv5W3M9LggmEIT7-aOaHYiHvjFOPi_0Vs6XxuvpIr-NJRY4L-f4Oelo9Vqd1XGHZdJXFwedG4v1EsOx53oOKFvmLTuV2jcR02pCCP78KGA1tMIwNDLzxhNV57rafQAEvzXjl3tmypPtftjPWBYiRwWCfSL0hguwq-S6RTuBKa9bzXjBzNiv2t23R1ZH5pVBpkgjFLyeC9FHOeRqfNj3foUESy1JshJ-TYpa4jEsoONepxpd6smZYOON2xOl1ofvBJlUkJjP_roHUSnWpRA0Ft9D-liTDLCKGto0tXLB0XJqyxRN1VQYk17enF2-8U2rRsUkAfKIat2lwoaOqfHqO6cAD-TKQjrcl34pLNQvcSKXpbzjX17OoXRUPKEJzZbvqh-2ejZaTynG-OxI4OHJuTNc5JORVXNQkXHyiVeK6dBvJzSFZEokjqn-B1bTnI"},
                                   "multiAttachmentIAAttachmentHashes": [], "questionIAAttachmentHashes": [],
                                   "indeedResumeDownloadLink": 'null',
                                   "uploadedResumeDownloadLink": {"fileName": "resume (1).docx",
                                                                  "downloadUrl": "https://dubprod1.apply.indeed.com"
                                                                                 "/indeedapply/applicationpreview/attachment"
                                                                                 "?iaUid=1febbr9mmtv2t802&previewUid"
                                                                                 "=1febbt911qpes800&apiToken"
                                                                                 "=aa102235a5ccb18bd3668c0e14aa3ea7e2503cfac2a7a9bf3d6549899e125af4&id=256f9d0a99cf1854ab0124b14732de8a36a53a2e0ca88945c2b1ec3d06cc6335&fileToken=epJMxg5NjnBIWVkMTabZtRMCvK8Y74pmgkNkv5W3M9LggmEIT7-aOaHYiHvjFOPi_0Vs6XxuvpIr-NJRY4L-f4Oelo9Vqd1XGHZdJXFwedG4v1EsOx53oOKFvmLTuV2jcR02pCCP78KGA1tMIwNDLzxhNV57rafQAEvzXjl3tmypPtftjPWBYiRwWCfSL0hguwq-S6RTuBKa9bzXjBzNiv2t23R1ZH5pVBpkgjFLyeC9FHOeRqfNj3foUESy1JshJ-TYpa4jEsoONepxpd6smZYOON2xOl1ofvBJlUkJjP_roHUSnWpRA0Ft9D-liTDLCKGto0tXLB0XJqyxRN1VQYk17enF2-8U2rRsUkAfKIat2lwoaOqfHqO6cAD-TKQjrcl34pLNQvcSKXpbzjX17OoXRUPKEJzZbvqh-2ejZaTynG-OxI4OHJuTNc5JORVXNQkXHyiVeK6dBvJzSFZEokjqn-B1bTnI"},
                                   "reportIssueLink": 'null', "aqScore": -1, "easternOrder": 'false'}}
        return JsonResponse(res)
