from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView
from mainsystem.forms.test_form import TestForm
from django.http import HttpResponse
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect,
                         HttpResponsePermanentRedirect)
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(TemplateView):
    template_name = "test/test1.html"

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        return super(TestView, self).get(self, request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        response = super(TestView, self).render_to_response(context, **response_kwargs)
        response.set_cookie("BID", "3500")
        response.set_cookie("VID", "3500")
        response.set_cookie("activity", "3500")
        response.set_cookie("ast_visit_at", "3500")
        response.set_cookie("last_jdp_search_rails", "3500")
        return response
    # def get(self, request, *args, **kwargs):
    #     return HttpResponseForbidden()


class TestFormView(TemplateView):
    template_name = "test/test_form.html"

    def get(self, request, *args, **kwargs):
        return super(TestFormView, self).get(self, request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        response = super(TestFormView, self).render_to_response(context, **response_kwargs)
        response.set_cookie("BID", "13500")
        response.set_cookie("VID", "13500")
        response.set_cookie("activity", "13500")
        response.set_cookie("ast_visit_at", "13500")
        response.set_cookie("last_jdp_search_rails", "13500")
        return response

    #
    # def get(self, request, *args, **kwargs):
    #     return HttpResponseBadRequest(content="Fail")


# class TestDataSave(CreateView):
#     def post(self, request, *args, **kwargs):
#         print(request.FILES)
#         order_form = TestForm(request.POST, request.FILES)
#         if order_form.is_valid():
#             order_form.save()
#             return HttpResponseRedirect("http://127.0.0.1:8001/mainsystem/oneform/")
#         else:
#             print(order_form.errors)
#             return HttpResponseBadRequest(content="DFail")

class TestDataSave(CreateView):
    def post(self, request, *args, **kwargs):
        print(request.FILES)
        order_form = TestForm(request.POST, request.FILES)
        return HttpResponseRedirect("http://127.0.0.1:8001/mainsystem/oneform/")


class OneRedirect(View):
    def post(self, request, *args, **kwargs):
        return HttpResponsePermanentRedirect("http://127.0.0.1:8001/mainsystem/twoform/")

    def get(self, request, *args, **kwargs):
        return HttpResponsePermanentRedirect("http://127.0.0.1:8001/mainsystem/twoform/")


class TwoRedirect(TemplateView):
    template_name = "test/test_form.html"


class PaginateLink(APIView):
    def get(self, request, *args, **kwargs):
        data_response = '$("<div class="new-job-collection bg-fade"></div>").appendTo($("#jobs_collection")).append(' \
                        '"\n<div class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3m6st67wd4w5pp6p17\" aria-label=\"Save this Director of International Operations ' \
                        '- Global Logistics job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J3M6ST67WD4W5PP6P17?save_job_did=J3M6ST67WD4W5PP6P17\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Director of International Operations - Global ' \
                        'Logistics Job at city of Seattle\" ' \
                        'data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/3dabde98f63158b56a75cc2895e2c528.png\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">13 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Director of International ' \
                        'Operations - Global Logistics<\/div>\n<div class=\"data-details\">\n<span>Randstad ' \
                        'USA<\/span>\n<span>WA - Seattle<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div ' \
                        'class=\"data-snapshot commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"block show-mobile\">job summary: TITLE: Director of International Operations - ' \
                        'Global Logistics LOCATION: Seattle, Washington Exceptional opportunity for a business driver ' \
                        'who has a solid background in international l...<\/div>\n<div class=\"block\">\$95k - ' \
                        '\$120k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of ' \
                        'International Operations - Global Logistics jobs in Seattle\" class=\"data-results-content ' \
                        'block job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|51\" ' \
                        'data-job-did=\"J3M6ST67WD4W5PP6P17\" data-company-did=\"CHL84J767C68N4L4X46\" ' \
                        'data-ipath=\"CRJR51\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J3M6ST67WD4W5PP6P17\" ' \
                        'href=\"/job/J3M6ST67WD4W5PP6P17\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j4r06t6jn8hh29nyymy\" aria-label=\"Save this Director of Customer Success job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J4R06T6JN8HH29NYYMY?save_job_did=J4R06T6JN8HH29NYYMY\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Director of Customer Success Job at city of San ' \
                        'Francisco\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/207918253b665f4d76bc5d8b20fe2cc2.jpg\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">13 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Director of Customer ' \
                        'Success<\/div>\n<div class=\"data-details\">\n<span>International Search ' \
                        'Consultants<\/span>\n<span>CA - San Francisco<\/span>\n<span>Full ' \
                        'Time<\/span>\n<\/div>\n<div class=\"data-snapshot commute-info\">\n<\/div>\n<div ' \
                        'class=\"data-snapshot\">\n<div class=\"block show-mobile\">Director of Customer Success ' \
                        'Austin or San Francisco ISC’s team of Software Recruiters is partnering with an innovative ' \
                        'and growing retail analytics SaaS company to identify a Director of Customer ' \
                        '...<\/div>\n<div class=\"block\"><\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"data-results-bubble bubble-green\">Easy ' \
                        'Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Customer Success jobs ' \
                        'in San Francisco\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|52\" data-job-did=\"J4R06T6JN8HH29NYYMY\" ' \
                        'data-company-did=\"CHS2ZJ7031Y9KD3C0SG\" data-ipath=\"CRJR52\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/job/J4R06T6JN8HH29NYYMY\" ' \
                        'href=\"/job/J4R06T6JN8HH29NYYMY\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3t4bh5y5zv0w5kdp9j\" aria-label=\"Save this Assistant Area Director job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J3T4BH5Y5ZV0W5KDP9J?save_job_did=J3T4BH5Y5ZV0W5KDP9J\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Assistant Area Director Job at city of DeSoto\" ' \
                        'data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/63a9f3b02f0277ad4fb0bc8bc376fa12.jpg\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">21 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Assistant Area ' \
                        'Director<\/div>\n<div class=\"data-details\">\n<span>Frontline Source ' \
                        'Group<\/span>\n<span>TX - DeSoto<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div ' \
                        'class=\"data-snapshot commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"block show-mobile\">Our growing client in Desoto, TX has a need for an Assistant ' \
                        'Area Director with operations experience and people skills on a direct hire basis. Company ' \
                        'Profile: Successful Healthcare organization P...<\/div>\n<div class=\"block\">\$50k - ' \
                        '\$60k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Assistant ' \
                        'Area Director jobs in DeSoto\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|53\" data-job-did=\"J3T4BH5Y5ZV0W5KDP9J\" ' \
                        'data-company-did=\"C8H82Y5XWD66MF2W3Y5\" data-ipath=\"CRJR53\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/job/J3T4BH5Y5ZV0W5KDP9J\" ' \
                        'href=\"/job/J3T4BH5Y5ZV0W5KDP9J\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3g64w75ytn8r042qvj\" aria-label=\"Save this Medical Director job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J3G64W75YTN8R042QVJ?save_job_did=J3G64W75YTN8R042QVJ\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Medical Director Job at city of Rochester\" ' \
                        'data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/8e092807251a30b83b1272969050e274.jpg\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">23 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Medical Director<\/div>\n<div ' \
                        'class=\"data-details\">\n<span>Medical Staffing Services<\/span>\n<span>NY - ' \
                        'Rochester<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\"data-snapshot ' \
                        'commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"block ' \
                        'show-mobile\">Medical Director We are looking to hire a Medical Director in Rochester, ' \
                        'NY area for a rapidly growing national company that provides leading-edge healthcare ' \
                        'solutions for chronically ill patients ...<\/div>\n<div class=\"block\">\$260k - ' \
                        '\$280k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Medical ' \
                        'Director jobs in Rochester\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|54\" data-job-did=\"J3G64W75YTN8R042QVJ\" ' \
                        'data-company-did=\"CHM67460B4NP1QMVW72\" data-ipath=\"CRJR54\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/job/J3G64W75YTN8R042QVJ\" ' \
                        'href=\"/job/J3G64W75YTN8R042QVJ\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j2y4fd6trknsv5c4rv8\" aria-label=\"Save this Senior Account Director job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J2Y4FD6TRKNSV5C4RV8?save_job_did=J2Y4FD6TRKNSV5C4RV8\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Senior Account Director Job at city of Chicago\" ' \
                        'data-src=\"\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" ' \
                        'src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" ' \
                        '/><\/div>\n<\/div>\n<div class=\"col big col-mobile-inline\">\n<div ' \
                        'class=\"data-results-publish-time\">27 days ago<\/div>\n<div class=\"data-results-title ' \
                        'dark-blue-text b\">Senior Account Director<\/div>\n<div ' \
                        'class=\"data-details\">\n<span>Catalyx<\/span>\n<span>IL - Chicago<\/span>\n<span>Full ' \
                        'Time<\/span>\n<\/div>\n<div class=\"data-snapshot commute-info\">\n<\/div>\n<div ' \
                        'class=\"data-snapshot\">\n<div class=\"block show-mobile\">Senior Account Director Company ' \
                        'Overview Catalyx is a fast-growing, multi award-winning, tech enabled insight agency. We ' \
                        'work with some of the world\"s most respected companies across 45 countries ' \
                        'a...<\/div>\n<div class=\"block\"><\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"data-results-bubble bubble-green\">Easy ' \
                        'Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Senior Account Director jobs in ' \
                        'Chicago\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|55\" data-job-did=\"J2Y4FD6TRKNSV5C4RV8\" ' \
                        'data-company-did=\"\" data-ipath=\"CRJR55\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J2Y4FD6TRKNSV5C4RV8\" ' \
                        'href=\"/job/J2Y4FD6TRKNSV5C4RV8\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j2n0zb5xh2btk5w6q46\" aria-label=\"Save this Aquatics Director job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J2N0ZB5XH2BTK5W6Q46?save_job_did=J2N0ZB5XH2BTK5W6Q46\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Aquatics Director Job at city of Broward County\" ' \
                        'data-src=\"\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" ' \
                        'src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" ' \
                        '/><\/div>\n<\/div>\n<div class=\"col big col-mobile-inline\">\n<div ' \
                        'class=\"data-results-publish-time\">27 days ago<\/div>\n<div class=\"data-results-title ' \
                        'dark-blue-text b\">Aquatics Director<\/div>\n<div class=\"data-details\">\n<span>YMCA of ' \
                        'South Florida<\/span>\n<span>FL - Fort Lauderdale<\/span>\n<span>Full ' \
                        'Time<\/span>\n<\/div>\n<div class=\"data-snapshot commute-info\">\n<\/div>\n<div ' \
                        'class=\"data-snapshot\">\n<div class=\"block show-mobile\">The YMCA of South Florida is ' \
                        'looking for an individual with aquatics programming and supervisory experience to join our ' \
                        'team as an Aquatics Director. The Aquatics Director is responsible for ' \
                        'prepar...<\/div>\n<div class=\"block\">\$36,' \
                        '327 - \$45k/year<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Aquatics Director jobs ' \
                        'in Fort Lauderdale\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|56\" data-job-did=\"J2N0ZB5XH2BTK5W6Q46\" ' \
                        'data-company-did=\"\" data-ipath=\"CRJR56\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J2N0ZB5XH2BTK5W6Q46\" ' \
                        'href=\"/job/J2N0ZB5XH2BTK5W6Q46\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3q41f7440xvq7fvpf0\" aria-label=\"Save this Director of Decision Support job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J3Q41F7440XVQ7FVPF0?save_job_did=J3Q41F7440XVQ7FVPF0\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Director of Decision Support Job at city of Chester\" ' \
                        'data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">9 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Director of Decision ' \
                        'Support<\/div>\n<div class=\"data-details\">\n<span>Robert Half<\/span>\n<span>PA - ' \
                        'Chester<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\"data-snapshot ' \
                        'commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"block ' \
                        'show-mobile\">Ref ID: 03720-0011907276 Classification: Director of Accounting Compensation: ' \
                        '\$130000.00 to \$145000.00 yearly Are you an experienced professional looking for a career ' \
                        'transition? There is an impera...<\/div>\n<div class=\"block\">\$130k - ' \
                        '\$145k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of ' \
                        'Decision Support jobs in Chester\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|57\" data-job-did=\"J3Q41F7440XVQ7FVPF0\" ' \
                        'data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR57\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/job/J3Q41F7440XVQ7FVPF0\" ' \
                        'href=\"/job/J3Q41F7440XVQ7FVPF0\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3343m6lx6s4mwx0xp6\" aria-label=\"Save this Physical Therapist Assistant Program ' \
                        'Director job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https' \
                        '://www.careerbuilder.com/job/J3343M6LX6S4MWX0XP6?save_job_did=J3343M6LX6S4MWX0XP6\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Physical Therapist Assistant Program Director Job at ' \
                        'city of Miami\" data-src=\"\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(' \
                        'this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">14 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Physical Therapist Assistant ' \
                        'Program Director<\/div>\n<div class=\"data-details\">\n<span>The Praxis ' \
                        'Institute<\/span>\n<span>FL - Miami<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div ' \
                        'class=\"data-snapshot commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"block show-mobile\">Job description Praxis Institute seeks a program ' \
                        'director/faculty member for its CAPTE accredited PTA program delivered in a hybrid education ' \
                        'format. The Program Director (PD) for the PTA program p...<\/div>\n<div ' \
                        'class=\"block\"><\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"data-results-bubble bubble-green\">Easy ' \
                        'Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Physical Therapist Assistant ' \
                        'Program Director jobs in Miami\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|58\" data-job-did=\"J3343M6LX6S4MWX0XP6\" ' \
                        'data-company-did=\"\" data-ipath=\"CRJR58\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J3343M6LX6S4MWX0XP6\" ' \
                        'href=\"/job/J3343M6LX6S4MWX0XP6\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j4r3mf6vmdb8kwwq2hf\" aria-label=\"Save this Sales Director - SaaS job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J4R3MF6VMDB8KWWQ2HF?save_job_did=J4R3MF6VMDB8KWWQ2HF\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Sales Director - SaaS Job at city of San Mateo\" ' \
                        'data-src=\"\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" ' \
                        'src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" ' \
                        '/><\/div>\n<\/div>\n<div class=\"col big col-mobile-inline\">\n<div ' \
                        'class=\"data-results-publish-time\">29 days ago<\/div>\n<div class=\"data-results-title ' \
                        'dark-blue-text b\">Sales Director - SaaS<\/div>\n<div ' \
                        'class=\"data-details\">\n<span>Certus<\/span>\n<span>CA - San Mateo<\/span>\n<span>Full ' \
                        'Time<\/span>\n<\/div>\n<div class=\"data-snapshot commute-info\">\n<\/div>\n<div ' \
                        'class=\"data-snapshot\">\n<div class=\"block show-mobile\">Sales Director - SaaS Bay Area ' \
                        '125-135k Base, 250-275k OTE + Executive Benefits As a leading provider of enterprise-class ' \
                        'cloud-based software, our client has grown to become the SaaS solution of c...<\/div>\n<div ' \
                        'class=\"block\">\$125k - \$135k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"data-results-bubble bubble-green\">Easy ' \
                        'Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Sales Director - SaaS jobs in San ' \
                        'Mateo\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|59\" data-job-did=\"J4R3MF6VMDB8KWWQ2HF\" ' \
                        'data-company-did=\"\" data-ipath=\"CRJR59\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J4R3MF6VMDB8KWWQ2HF\" ' \
                        'href=\"/job/J4R3MF6VMDB8KWWQ2HF\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j4r82z698nvg6t0splt\" aria-label=\"Save this Sales Director - SaaS job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J4R82Z698NVG6T0SPLT?save_job_did=J4R82Z698NVG6T0SPLT\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Sales Director - SaaS Job at city of Palo Alto\" ' \
                        'data-src=\"\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" ' \
                        'src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" ' \
                        '/><\/div>\n<\/div>\n<div class=\"col big col-mobile-inline\">\n<div ' \
                        'class=\"data-results-publish-time\">29 days ago<\/div>\n<div class=\"data-results-title ' \
                        'dark-blue-text b\">Sales Director - SaaS<\/div>\n<div ' \
                        'class=\"data-details\">\n<span>Certus<\/span>\n<span>CA - Palo Alto<\/span>\n<span>Full ' \
                        'Time<\/span>\n<\/div>\n<div class=\"data-snapshot commute-info\">\n<\/div>\n<div ' \
                        'class=\"data-snapshot\">\n<div class=\"block show-mobile\">Sales Director - SaaS Bay Area ' \
                        '125-135k Base, 250-275k OTE + Executive Benefits As a leading provider of enterprise-class ' \
                        'cloud-based software, our client has grown to become the SaaS solution of c...<\/div>\n<div ' \
                        'class=\"block\">\$125k - \$135k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"data-results-bubble bubble-green\">Easy ' \
                        'Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Sales Director - SaaS jobs in ' \
                        'Palo Alto\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|60\" data-job-did=\"J4R82Z698NVG6T0SPLT\" ' \
                        'data-company-did=\"\" data-ipath=\"CRJR60\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J4R82Z698NVG6T0SPLT\" ' \
                        'href=\"/job/J4R82Z698NVG6T0SPLT\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3q50564cbzz18y0dx6\" aria-label=\"Save this Director - Home Services &amp; ' \
                        'Renovations job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https' \
                        '://www.careerbuilder.com/job/J3Q50564CBZZ18Y0DX6?save_job_did=J3Q50564CBZZ18Y0DX6\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Director - Home Services & Renovations Job at city of ' \
                        'Concord\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/1bba307f98daf06c74e4b14a5a575f54.jpg\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">30 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Director - Home Services & ' \
                        'Renovations<\/div>\n<div class=\"data-details\">\n<span>Michael Page<\/span>\n<span>MA - ' \
                        'Concord<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\"data-snapshot ' \
                        'commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"block ' \
                        'show-mobile\">MPI does not discriminate on the basis of race, color, religion, sex, ' \
                        'sexual orientation, gender identity or expression, national origin, age, disability, ' \
                        'veteran status, marital status, or based o...<\/div>\n<div class=\"block\">\$85k - ' \
                        '\$100k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director - ' \
                        'Home Services &amp; Renovations jobs in Concord\" class=\"data-results-content block ' \
                        'job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|61\" ' \
                        'data-job-did=\"J3Q50564CBZZ18Y0DX6\" data-company-did=\"CHR7G16TZQFMFJCFP4C\" ' \
                        'data-ipath=\"CRJR61\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J3Q50564CBZZ18Y0DX6\" ' \
                        'href=\"/job/J3Q50564CBZZ18Y0DX6\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j2y7376fr0tzxcbj1f1\" aria-label=\"Save this Director of Marketing job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J2Y7376FR0TZXCBJ1F1?save_job_did=J2Y7376FR0TZXCBJ1F1\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Director of Marketing Job at city of Hicksville, ' \
                        'NY\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/284edeb80a186174950f05aa2e6fc819.jpg\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">21 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Director of ' \
                        'Marketing<\/div>\n<div class=\"data-details\">\n<span>NY State Solar<\/span>\n<span>NY - ' \
                        'Hicksville<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\"data-snapshot ' \
                        'commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"block ' \
                        'show-mobile\">New York State Solar is seeking a hands-on Director of Marketing with ' \
                        'experience in B2C industries. In the Director of Marketing role you will design, ' \
                        'implement and monitor effective marketing stra...<\/div>\n<div class=\"block\">\$120k - ' \
                        '\$140k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of ' \
                        'Marketing jobs in Hicksville\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|62\" data-job-did=\"J2Y7376FR0TZXCBJ1F1\" ' \
                        'data-company-did=\"CDF4S56PLSXY25VR27H\" data-ipath=\"CRJR62\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/job/J2Y7376FR0TZXCBJ1F1\" ' \
                        'href=\"/job/J2Y7376FR0TZXCBJ1F1\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-jd94jc79bdqfkzs3dxj\" aria-label=\"Save this Director, ICU,  Med Surg job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/JD94JC79BDQFKZS3DXJ?save_job_did=JD94JC79BDQFKZS3DXJ\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Director, ICU,  Med Surg Job at city of Gainesville, ' \
                        'Texas\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/aa006229343199ae85d27ba6a391c42d.jpg\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">7 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Director, ICU,  ' \
                        'Med Surg<\/div>\n<div class=\"data-details\">\n<span>North Texas Medical ' \
                        'Center<\/span>\n<span>TX - Gainesville<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div ' \
                        'class=\"data-snapshot commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"block show-mobile\">Director, ICU, Med Surg North Texas Medical Center (NTMC), ' \
                        'a 60 bed acute care hospital located in Gainesville, Texas, seeks an experienced Director, ' \
                        'ICU and Med/Surg services. The Director is a Re...<\/div>\n<div class=\"block\">\$50k - ' \
                        '\$108,750/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"data-results-bubble bubble-green\">Easy ' \
                        'Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director, ICU,  Med Surg jobs in ' \
                        'Gainesville\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|63\" data-job-did=\"JD94JC79BDQFKZS3DXJ\" ' \
                        'data-company-did=\"CCM67B6XYSWG62G79XC\" data-ipath=\"CRJR63\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/job/JD94JC79BDQFKZS3DXJ\" ' \
                        'href=\"/job/JD94JC79BDQFKZS3DXJ\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-jd87s15x95st1pfkmq7\" aria-label=\"Save this Assistant Director of Public Policy ' \
                        'job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/JD87S15X95ST1PFKMQ7?save_job_did=JD87S15X95ST1PFKMQ7\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Assistant Director of Public Policy Job at city of ' \
                        'Washington DC\" data-src=\"\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(' \
                        'this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">8 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Assistant Director of Public ' \
                        'Policy<\/div>\n<div class=\"data-details\">\n<span>The American Academy of ' \
                        'Actuaries<\/span>\n<span>DC - Washington<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div ' \
                        'class=\"data-snapshot commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"block show-mobile\">Assistant Director of Public Policy Many of today\"s most ' \
                        'pressing public policy issues across a wide spectrum of concerns, such as climate change, ' \
                        'retirement security, health equity, and so many ot...<\/div>\n<div ' \
                        'class=\"block\"><\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Assistant Director of ' \
                        'Public Policy jobs in Washington\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|64\" data-job-did=\"JD87S15X95ST1PFKMQ7\" ' \
                        'data-company-did=\"\" data-ipath=\"CRJR64\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/JD87S15X95ST1PFKMQ7\" ' \
                        'href=\"/job/JD87S15X95ST1PFKMQ7\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3r13v75x2nhf9wz53m\" aria-label=\"Save this Director of Accounting job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J3R13V75X2NHF9WZ53M?save_job_did=J3R13V75X2NHF9WZ53M\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Director of Accounting Job at city of Philadelphia\" ' \
                        'data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">16 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Director of ' \
                        'Accounting<\/div>\n<div class=\"data-details\">\n<span>Robert Half<\/span>\n<span>PA - ' \
                        'Philadelphia<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\"data-snapshot ' \
                        'commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"block ' \
                        'show-mobile\">Ref ID: 03720-0011804778 Classification: Director of Accounting Compensation: ' \
                        '\$120000.00 to \$140000.00 yearly Available for an immediate hire, Robert Half Finance is ' \
                        'searching for a skilled, eager,...<\/div>\n<div class=\"block\">\$120k - ' \
                        '\$140k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of ' \
                        'Accounting jobs in Philadelphia\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|65\" data-job-did=\"J3R13V75X2NHF9WZ53M\" ' \
                        'data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR65\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/job/J3R13V75X2NHF9WZ53M\" ' \
                        'href=\"/job/J3R13V75X2NHF9WZ53M\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3r5rw71vj4l5mnx6r9\" aria-label=\"Save this Manager / Director Transaction ' \
                        'Services (M&amp;A) job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J3R5RW71VJ4L5MNX6R9?save_job_did=J3R5RW71VJ4L5MNX6R9\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Manager / Director Transaction Services (M&A) Job at ' \
                        'city of New York\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/617bd9d0443f0a787d76067fdd7dd4e7.jpg\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">17 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Manager / Director ' \
                        'Transaction Services (M&A)<\/div>\n<div class=\"data-details\">\n<span>Kforce Finance and ' \
                        'Accounting<\/span>\n<span>NY - New York<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div ' \
                        'class=\"data-snapshot commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"block show-mobile\">RESPONSIBILITIES: Kforce\"s client, a leading New York, ' \
                        'NY based regional CPA firm is seeking a Manager/Director Transactions Services (M&A). Duties ' \
                        'of the Manager/Director Transactions Services (M&...<\/div>\n<div class=\"block\">\$125k - ' \
                        '\$200k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Manager / ' \
                        'Director Transaction Services (M&amp;A) jobs in New York\" class=\"data-results-content ' \
                        'block job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|66\" ' \
                        'data-job-did=\"J3R5RW71VJ4L5MNX6R9\" data-company-did=\"CHQ5TZ6RDY4S9WXX6DH\" ' \
                        'data-ipath=\"CRJR66\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J3R5RW71VJ4L5MNX6R9\" ' \
                        'href=\"/job/J3R5RW71VJ4L5MNX6R9\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-jdd43b6yx7df94r73lk\" aria-label=\"Save this Director of Customer Success job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/JDD43B6YX7DF94R73LK?save_job_did=JDD43B6YX7DF94R73LK\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Director of Customer Success Job at city of Austin\" ' \
                        'data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/207918253b665f4d76bc5d8b20fe2cc2.jpg\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">13 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Director of Customer ' \
                        'Success<\/div>\n<div class=\"data-details\">\n<span>International Search ' \
                        'Consultants<\/span>\n<span>TX - Austin<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div ' \
                        'class=\"data-snapshot commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"block show-mobile\">Director of Customer Success Austin or San Francisco ISC’s team ' \
                        'of Software Recruiters is partnering with an innovative and growing retail analytics SaaS ' \
                        'company to identify a Director of Customer ...<\/div>\n<div ' \
                        'class=\"block\"><\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"data-results-bubble bubble-green\">Easy ' \
                        'Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Customer Success jobs ' \
                        'in Austin\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|67\" data-job-did=\"JDD43B6YX7DF94R73LK\" ' \
                        'data-company-did=\"CHS2ZJ7031Y9KD3C0SG\" data-ipath=\"CRJR67\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/job/JDD43B6YX7DF94R73LK\" ' \
                        'href=\"/job/JDD43B6YX7DF94R73LK\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3p7mj60jyly2kh79v6\" aria-label=\"Save this Regional Director of Staffing ' \
                        'Services job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https' \
                        '://www.careerbuilder.com/job/J3P7MJ60JYLY2KH79V6?save_job_did=J3P7MJ60JYLY2KH79V6\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Regional Director of Staffing Services Job at city of ' \
                        'Indianapolis\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/04160e3574214da11b4b0828569169af.jpg\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">16 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Regional Director of Staffing ' \
                        'Services<\/div>\n<div class=\"data-details\">\n<span>Diverse Staffing, Inc<\/span>\n<span>IN ' \
                        '- Indianapolis<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\"data-snapshot ' \
                        'commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"block ' \
                        'show-mobile\">IN01CORP Diverse Staffing, recently named a Glassdoor Best Places to Work in ' \
                        '2021, is currently interviewing professionals for the position of Regional Director of ' \
                        'Staffing Services. The base salar...<\/div>\n<div class=\"block\">\$90k - ' \
                        '\$100k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Regional ' \
                        'Director of Staffing Services jobs in Indianapolis\" class=\"data-results-content block ' \
                        'job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|68\" ' \
                        'data-job-did=\"J3P7MJ60JYLY2KH79V6\" data-company-did=\"CHL6976MZK4TYGFFBK6\" ' \
                        'data-ipath=\"CRJR68\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J3P7MJ60JYLY2KH79V6\" ' \
                        'href=\"/job/J3P7MJ60JYLY2KH79V6\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3n7nj703cjt2lxwhf8\" aria-label=\"Save this Director of Operations job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J3N7NJ703CJT2LXWHF8?save_job_did=J3N7NJ703CJT2LXWHF8\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Director of Operations Job at city of West Lafayette\" ' \
                        'data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/fb60cfc0d12019500e953f9540c16b45.jpg\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">26 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Director of ' \
                        'Operations<\/div>\n<div class=\"data-details\">\n<span>Staffmark<\/span>\n<span>IN - West ' \
                        'Lafayette<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\"data-snapshot ' \
                        'commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"block ' \
                        'show-mobile\">Our client, a leading manufacturer of components supplying the industrial, ' \
                        'off-highway, and railroad industries, is seeking a Director of Operations for their West ' \
                        'Lafayette, IN plant! Unique oppor...<\/div>\n<div class=\"block\">\$110k - ' \
                        '\$120k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of ' \
                        'Operations jobs in West Lafayette\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|69\" data-job-did=\"J3N7NJ703CJT2LXWHF8\" ' \
                        'data-company-did=\"CCL1HS72WGPP69828C9\" data-ipath=\"CRJR69\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/job/J3N7NJ703CJT2LXWHF8\" ' \
                        'href=\"/job/J3N7NJ703CJT2LXWHF8\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j4r39g66b80yqm9z008\" aria-label=\"Save this Sales Director - SaaS job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J4R39G66B80YQM9Z008?save_job_did=J4R39G66B80YQM9Z008\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Sales Director - SaaS Job at city of Oakland\" ' \
                        'data-src=\"\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" ' \
                        'src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" ' \
                        '/><\/div>\n<\/div>\n<div class=\"col big col-mobile-inline\">\n<div ' \
                        'class=\"data-results-publish-time\">29 days ago<\/div>\n<div class=\"data-results-title ' \
                        'dark-blue-text b\">Sales Director - SaaS<\/div>\n<div ' \
                        'class=\"data-details\">\n<span>Certus<\/span>\n<span>CA - Oakland<\/span>\n<span>Full ' \
                        'Time<\/span>\n<\/div>\n<div class=\"data-snapshot commute-info\">\n<\/div>\n<div ' \
                        'class=\"data-snapshot\">\n<div class=\"block show-mobile\">Sales Director - SaaS Bay Area ' \
                        '125-135k Base, 250-275k OTE + Executive Benefits As a leading provider of enterprise-class ' \
                        'cloud-based software, our client has grown to become the SaaS solution of c...<\/div>\n<div ' \
                        'class=\"block\">\$125k - \$135k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"data-results-bubble bubble-green\">Easy ' \
                        'Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Sales Director - SaaS jobs in ' \
                        'Oakland\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|70\" data-job-did=\"J4R39G66B80YQM9Z008\" ' \
                        'data-company-did=\"\" data-ipath=\"CRJR70\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J4R39G66B80YQM9Z008\" ' \
                        'href=\"/job/J4R39G66B80YQM9Z008\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-jdf3kj6qn0kk28yxcf8\" aria-label=\"Save this Director of Admissions job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/JDF3KJ6QN0KK28YXCF8?save_job_did=JDF3KJ6QN0KK28YXCF8\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Director of Admissions Job at city of Tampa\" ' \
                        'data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/0c9028119f634c08312969a176971fc4.jpg\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">3 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Director of ' \
                        'Admissions<\/div>\n<div class=\"data-details\">\n<span>Ultimate Medical ' \
                        'Academy<\/span>\n<span>FL - Tampa<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div ' \
                        'class=\"data-snapshot commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"block show-mobile\">Purpose of the Position: The Director, Admissions (DOA) is ' \
                        'responsible for directing a team of advisors who interface with prospective students and ' \
                        'those influencing the student’s decision to atten...<\/div>\n<div ' \
                        'class=\"block\"><\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Admissions ' \
                        'jobs in Tampa\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|71\" data-job-did=\"JDF3KJ6QN0KK28YXCF8\" ' \
                        'data-company-did=\"C8A3ZL61P2FLMYDH1KS\" data-ipath=\"CRJR71\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/job/JDF3KJ6QN0KK28YXCF8\" ' \
                        'href=\"/job/JDF3KJ6QN0KK28YXCF8\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j2s5zh76f2lr339jlmq\" aria-label=\"Save this Medical Director - Addiction Medicine ' \
                        'job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J2S5ZH76F2LR339JLMQ?save_job_did=J2S5ZH76F2LR339JLMQ\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Medical Director - Addiction Medicine Job at city of ' \
                        'Hanover\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/bec9f34c88893e3e71b7e0d696491def.png\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">4 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Medical Director - Addiction ' \
                        'Medicine<\/div>\n<div class=\"data-details\">\n<span>HRselect<\/span>\n<span>PA - ' \
                        'Hanover<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\"data-snapshot ' \
                        'commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"block show-mobile\">We ' \
                        'are working with a Full Continuum, Evidenced Based, Residential Substance Abuse Facility ' \
                        'that is in search of an Addiction Medical Director to join their team. This is an exciting ' \
                        'opportunity to...<\/div>\n<div class=\"block\">\$210k - \$255k/year<\/div>\n<\/div>\n<div ' \
                        'class=\"data-snapshot\">\n<div class=\"data-results-bubble bubble-green\">Easy ' \
                        'Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Medical Director - Addiction ' \
                        'Medicine jobs in Hanover\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|72\" data-job-did=\"J2S5ZH76F2LR339JLMQ\" ' \
                        'data-company-did=\"CHP6NY622CT7ST36ZVW\" data-ipath=\"CRJR72\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/job/J2S5ZH76F2LR339JLMQ\" ' \
                        'href=\"/job/J2S5ZH76F2LR339JLMQ\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3w73778fqpwk6dzbg2\" aria-label=\"Save this Assistant Director of Nursing job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J3W73778FQPWK6DZBG2?save_job_did=J3W73778FQPWK6DZBG2\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Assistant Director of Nursing Job at city of Orchard ' \
                        'City\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/3f493e6249dd7b2037415702bda6204b.png\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">6 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Assistant Director of ' \
                        'Nursing<\/div>\n<div class=\"data-details\">\n<span>Volunteers of America National ' \
                        'Services<\/span>\n<span>CO - Orchard City<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div ' \
                        'class=\"data-snapshot commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div ' \
                        'class=\"block show-mobile\">Volunteers of America is looking for a compassionate and ' \
                        'experienced leader to join our team as ADON at Horizons care center in beautiful Eckert, ' \
                        'CO! JOB DESCRIPTION The primary purpose of the Assi...<\/div>\n<div class=\"block\">\$77k - ' \
                        '\$83k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Assistant ' \
                        'Director of Nursing jobs in Orchard City\" class=\"data-results-content block ' \
                        'job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|73\" ' \
                        'data-job-did=\"J3W73778FQPWK6DZBG2\" data-company-did=\"C7X53J6D175T84C6LKP\" ' \
                        'data-ipath=\"CRJR73\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J3W73778FQPWK6DZBG2\" ' \
                        'href=\"/job/J3W73778FQPWK6DZBG2\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3w79g63y2s84zdkkq7\" aria-label=\"Save this Human Resources (HR)Director job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J3W79G63Y2S84ZDKKQ7?save_job_did=J3W79G63Y2S84ZDKKQ7\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Human Resources (HR)Director Job at city of ' \
                        'Parsippany\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">7 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Human Resources (' \
                        'HR)Director<\/div>\n<div class=\"data-details\">\n<span>Robert Half<\/span>\n<span>NJ - ' \
                        'Parsippany<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\"data-snapshot ' \
                        'commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"block ' \
                        'show-mobile\">Ref ID: 02750-0011910956 Classification: Human Resources (HR) Manager ' \
                        'Compensation: \$130000.00 to \$160000.00 yearly A busy company in the Livignston area is ' \
                        'seeking a Human Resources Director to jo...<\/div>\n<div class=\"block\">\$130k - ' \
                        '\$160k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Human ' \
                        'Resources (HR)Director jobs in Parsippany\" class=\"data-results-content block ' \
                        'job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|74\" ' \
                        'data-job-did=\"J3W79G63Y2S84ZDKKQ7\" data-company-did=\"CCM2J66N3HFX0NR4479\" ' \
                        'data-ipath=\"CRJR74\" data-external-company-link=\"\" ' \
                        'data-jdp-joblink=\"/job/J3W79G63Y2S84ZDKKQ7\" ' \
                        'href=\"/mainsystem/testpage/"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n\n<div ' \
                        'class=\"data-results-content-parent relative\">\n<a class=\"data-results-save-job ' \
                        'saved-job-j3m5ss725q7wyf8psz1\" aria-label=\"Save this Director of Human Resources job\" ' \
                        'data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www' \
                        '.careerbuilder.com/job/J3M5SS725Q7WYF8PSZ1?save_job_did=J3M5SS725Q7WYF8PSZ1\" ' \
                        'data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i ' \
                        'aria-label=\"Saved Job\" class=\"fa fa-heart-o\"><\/i>\n<\/a>\n<div class=\"col-2 ' \
                        'layout-results\">\n<div class=\"col small col-mobile-inline\">\n<div ' \
                        'class=\"data-results-img\"><img alt=\"Director of Human Resources Job at city of Sanford\" ' \
                        'data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production' \
                        '/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" ' \
                        'onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64,' \
                        'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div ' \
                        'class=\"col big col-mobile-inline\">\n<div class=\"data-results-publish-time\">28 days ' \
                        'ago<\/div>\n<div class=\"data-results-title dark-blue-text b\">Director of Human ' \
                        'Resources<\/div>\n<div class=\"data-details\">\n<span>Robert Half<\/span>\n<span>FL - ' \
                        'Sanford<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\"data-snapshot ' \
                        'commute-info\">\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"block ' \
                        'show-mobile\">Ref ID: 01030-0011884869 Classification: Human Resources (HR) Manager ' \
                        'Compensation: \$120000.00 to \$140000.00 yearly Human Resources Director opening for a ' \
                        'Private-Equity owned operation in Sanford....<\/div>\n<div class=\"block\">\$120k - ' \
                        '\$140k/year<\/div>\n<\/div>\n<div class=\"data-snapshot\">\n<div class=\"data-results-bubble ' \
                        'bubble-green\">Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of ' \
                        'Human Resources jobs in Sanford\" class=\"data-results-content block job-listing-item\" ' \
                        'data-gtm=\"jrp-job-list|job-title-click|75\" data-job-did=\"J3M5SS725Q7WYF8PSZ1\" ' \
                        'data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR75\" ' \
                        'data-external-company-link=\"\" data-jdp-joblink=\"/mainsystem/testpage/" ' \
                        'href=\"/mainsystem/testpage/\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(' \
                        '\"false\" === \"true\") {\n      \$(\".data-results-content-parent\").off().on(\"click\", ' \
                        'function(){\n        if (\$(this).children(' \
                        '\"a.data-results-content.block.job-listing-item\").context.innerText.toLowerCase().includes(' \
                        '\"hiring event\")) {\n          window.dataLayer.push({ \"event\": \"JobSearchClicks\" });\n ' \
                        '       }\n      })\n    }\n    if(\$(document).find(\".partner-label\").length == 0){\n      ' \
                        'var partnerContainer = \$(document).find(\".data-results-content-parent.partner-job\")[0]\n  ' \
                        '    \$(\"<div class=\"pt10 pb10 partner-label\">Partner Jobs<\/div>\").insertBefore(' \
                        'partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n");$("#load_more_jobs button").attr(' \
                        '"data-load-more", ' \
                        '"/jobs?cb_apply=false&cb_workhome=false&emp=jtft%2Cjtfp&keywords=Director&location' \
                        '=&page_number=4&pay=20&posted=30&radius=");$.rails.enableElement($("#load_more_jobs ' \
                        'button"));if (false) {  $("#load_more_jobs button").hide()}if($(window).width() <= 1029){  ' \
                        '$("body").scrollTo($(".new-job-collection").last(), 1000);} else {  $(' \
                        '".fix-elem-parent").scrollTo($(".new-job-collection").last(), 1000);}if($(document).find(' \
                        '".partner-label").length == 0){  var partnerContainer = $(document).find(' \
                        '".data-results-content-parent.partner-job")[0]  $("<div class="pt10 pb10 ' \
                        'partner-label">Partner Jobs</div>").insertBefore(partnerContainer)}window.history.pushState(' \
                        '"{&quot;cb_apply&quot;=&gt;&quot;false&quot;, &quot;cb_workhome&quot;=&gt;&quot;false&quot;, ' \
                        '&quot;emp&quot;=&gt;&quot;jtft,jtfp&quot;, &quot;keywords&quot;=&gt;&quot;Director&quot;, ' \
                        '&quot;location&quot;=&gt;&quot;&quot;, &quot;page_number&quot;=&gt;&quot;3&quot;, ' \
                        '&quot;pay&quot;=&gt;&quot;20&quot;, &quot;posted&quot;=&gt;&quot;30&quot;, ' \
                        '&quot;radius&quot;=&gt;&quot;&quot;, &quot;jrp_mode&quot;=&gt;:simple, ' \
                        '&quot;locale&quot;=&gt;&quot;en-US&quot;, ' \
                        '&quot;controller&quot;=&gt;&quot;eu_consumer_core/hybrid_jobs&quot;, ' \
                        '&quot;action&quot;=&gt;&quot;index&quot;, &quot;format&quot;=&gt;&quot;js&quot;, ' \
                        '&quot;session_id&quot;=&gt;&quot;a62317e1426f4bedd411d1a6f657bbd8&quot;}", null, ' \
                        '"/jobs?cb_apply=false&cb_workhome=false&emp=jtft%2Cjtfp&keywords=Director&location' \
                        '=&page_number=3&pay=20&posted=30&radius="); '

        return Response(data_response, content_type="text/javascript")

