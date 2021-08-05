import re
import requests
slovo = "\n<div class=\'data-results-content-parent relative\'>\n<a class=\"data-results-save-job " \
        "saved-job-j2n6cn78lyd6vqhh5tr\" aria-label=\"Save this Executive Director job\" " \
        "data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder.com/job" \
        "/J2N6CN78LYD6VQHH5TR?save_job_did=J2N6CN78LYD6VQHH5TR\" data-gtm=\"jrp-job-list|save-link-modal-prompt\" " \
        "href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div " \
        "class=\'col-2 layout-results\'>\n<div class=\'col small col-mobile-inline\'>\n<div " \
        "class=\'data-results-img\'><img alt=\"Executive Director Job at city of Fort Collins, " \
        "CO\" data-src=\"https://secure.icbdr.comID62KH5XB0472B5LYV6.png\" class=\"lazy intl-company-logo\" " \
        "onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64," \
        "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div class=\'col big " \
        "col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>Today<\/div>\n<div class=\'data-results-title " \
        "dark-blue-text b\'>Executive Director<\/div>\n<div class=\'data-details\'>\n<span>CASA of Larimer " \
        "County<\/span>\n<span>CO - Fort Collins<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div " \
        "class=\'data-snapshot commute-info\'>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'block " \
        "show-mobile\'>EXECUTIVE DIRECTOR JOB DESCRIPTION CASA of Larimer County (CLC) is a nonprofit organization " \
        "comprised of two programs: Court Appointed Special Advocates (CASA) and Family Connections (FC). CASA " \
        "pro...<\/div>\n<div class=\'block\'>\$68,500 - \$94,250/year<\/div>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'data-results-bubble bubble-green\'>Easy " \
        "Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Executive Director jobs in Fort Collins\" " \
        "class=\"data-results-content block job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|26\" " \
        "data-job-did=\"J2N6CN78LYD6VQHH5TR\" data-company-did=\"\" data-ipath=\"CRJR26\" " \
        "data-external-company-link=\"\" data-jdp-joblink=\"/job/J2N6CN78LYD6VQHH5TR\" " \
        "href=\"/job/J2N6CN78LYD6VQHH5TR\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(\"false\" === " \
        "\"true\") {\n      \$(\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(" \
        "this).children(\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(" \
        "\"hiring event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      " \
        "})\n    }\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3t0kf6jyk66lwq5s8f\" aria-label=\"Save this VP/Director of Finance " \
        "job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder.com/job" \
        "/J3T0KF6JYK66LWQ5S8F?save_job_did=J3T0KF6JYK66LWQ5S8F\" data-gtm=\"jrp-job-list|save-link-modal-prompt\" " \
        "href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div " \
        "class=\'col-2 layout-results\'>\n<div class=\'col small col-mobile-inline\'>\n<div " \
        "class=\'data-results-img\'><img alt=\"VP/Director of Finance Job at city of Shreveport\" " \
        "data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production/296a1e03358f1aa11a66440d406f61a2.png\" " \
        "class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64," \
        "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div class=\'col big " \
        "col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>5 days ago<\/div>\n<div " \
        "class=\'data-results-title dark-blue-text b\'>VP/Director of Finance<\/div>\n<div " \
        "class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>LA - Shreveport<\/span>\n<span>Full " \
        "Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: 04640-0011913262 Classification: " \
        "VP/Director of Finance Compensation: \$80000.00 to \$110000.00 yearly Our Shreveport client is searching for " \
        "a Vice President of Operations to join their team...<\/div>\n<div class=\'block\'>\$80k - " \
        "\$110k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"VP/Director of Finance jobs " \
        "in Shreveport\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|27\" data-job-did=\"J3T0KF6JYK66LWQ5S8F\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR27\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3T0KF6JYK66LWQ5S8F\" href=\"/job/J3T0KF6JYK66LWQ5S8F\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-jcm3037719yd70m7dmz\" aria-label=\"Save this Director - Risk " \
        "Management job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www" \
        ".careerbuilder.com/job/JCM3037719YD70M7DMZ?save_job_did=JCM3037719YD70M7DMZ\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Director - Risk Management Job at city of " \
        "Ann Arbor\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/eb75066c0cbbf4ab44815d704a81b430.jpg\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>28 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Director - Risk Management<\/div>\n<div " \
        "class=\'data-details\'>\n<span>IHA<\/span>\n<span>MI - Ann Arbor<\/span>\n<span>Full " \
        "Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>POSITION DESCRIPTION: The Director - Risk " \
        "Management has leadership responsibility over IHA’s enterprise risk management activities in both the " \
        "inpatient and outpatient settings for IHA employed ph...<\/div>\n<div " \
        "class=\'block\'><\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director - Risk Management jobs in Ann " \
        "Arbor\" class=\"data-results-content block job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|28\" " \
        "data-job-did=\"JCM3037719YD70M7DMZ\" data-company-did=\"CD67DM79QQCWVVV3SN0\" data-ipath=\"CRJR28\" " \
        "data-external-company-link=\"\" data-jdp-joblink=\"/job/JCM3037719YD70M7DMZ\" " \
        "href=\"/job/JCM3037719YD70M7DMZ\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(\"false\" === " \
        "\"true\") {\n      \$(\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(" \
        "this).children(\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(" \
        "\"hiring event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      " \
        "})\n    }\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3p203629lnd82zx189\" aria-label=\"Save this Business Development " \
        "Director - Digital Transformation job\" " \
        "data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder.com/job" \
        "/J3P203629LND82ZX189?save_job_did=J3P203629LND82ZX189\" data-gtm=\"jrp-job-list|save-link-modal-prompt\" " \
        "href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div " \
        "class=\'col-2 layout-results\'>\n<div class=\'col small col-mobile-inline\'>\n<div " \
        "class=\'data-results-img\'><img alt=\"Business Development Director - Digital Transformation Job at city of " \
        "New York\" data-src=\"\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div " \
        "class=\'data-results-publish-time\'>Today<\/div>\n<div class=\'data-results-title dark-blue-text " \
        "b\'>Business Development Director - Digital Transformation<\/div>\n<div class=\'data-details\'>\n<span>NY - " \
        "New York<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot " \
        "commute-info\'>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Business " \
        "Development Director – Digital Transformation New York 150-170k Base, 200-230k OTE + Executive Benefits Our " \
        "client is leading the digital transformation charge on a global scale. Through o...<\/div>\n<div " \
        "class=\'block\'>\$150k - \$170k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div " \
        "class=\'data-results-bubble bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a " \
        "aria-label=\"Business Development Director - Digital Transformation jobs in New York\" " \
        "class=\"data-results-content block job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|29\" " \
        "data-job-did=\"J3P203629LND82ZX189\" data-company-did=\"\" data-ipath=\"CRJR29\" " \
        "data-external-company-link=\"\" data-jdp-joblink=\"/job/J3P203629LND82ZX189\" " \
        "href=\"/job/J3P203629LND82ZX189\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(\"false\" === " \
        "\"true\") {\n      \$(\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(" \
        "this).children(\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(" \
        "\"hiring event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      " \
        "})\n    }\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3r53g627r6dszzkp97\" aria-label=\"Save this City Government- " \
        "Director of HR job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www" \
        ".careerbuilder.com/job/J3R53G627R6DSZZKP97?save_job_did=J3R53G627R6DSZZKP97\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"City Government- Director of HR Job at city " \
        "of Stonecrest\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/a4c4c3cc13f17aead7334a7a1659d35f.jpg\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div " \
        "class=\'data-results-publish-time\'>Today<\/div>\n<div class=\'data-results-title dark-blue-text b\'>City " \
        "Government- Director of HR<\/div>\n<div class=\'data-details\'>\n<span>ExecuSource<\/span>\n<span>GA - " \
        "Stonecrest<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot " \
        "commute-info\'>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Location: " \
        "Stonecrest, GA Salary: Based on experience IMMEDIATE Director of HR position available! We are currently " \
        "representing a local city government seeking a Director of HR to join their team o...<\/div>\n<div " \
        "class=\'block\'>\$130k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"City Government- Director of " \
        "HR jobs in Stonecrest\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|30\" data-job-did=\"J3R53G627R6DSZZKP97\" " \
        "data-company-did=\"C2Y34X619L3MB0J7L23\" data-ipath=\"CRJR30\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3R53G627R6DSZZKP97\" href=\"/job/J3R53G627R6DSZZKP97\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3t72l6v31gm42d7k1k\" aria-label=\"Save this Art Director (Concept " \
        "Art &amp; Character Illustration) job\" " \
        "data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder.com/job" \
        "/J3T72L6V31GM42D7K1K?save_job_did=J3T72L6V31GM42D7K1K\" data-gtm=\"jrp-job-list|save-link-modal-prompt\" " \
        "href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div " \
        "class=\'col-2 layout-results\'>\n<div class=\'col small col-mobile-inline\'>\n<div " \
        "class=\'data-results-img\'><img alt=\"Art Director (Concept Art & Character Illustration) Job at city of El " \
        "Segundo\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div " \
        "class=\'data-results-publish-time\'>Today<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Art " \
        "Director (Concept Art & Character Illustration)<\/div>\n<div class=\'data-details\'>\n<span>Robert " \
        "Half<\/span>\n<span>CA - El Segundo<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot " \
        "commute-info\'>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: " \
        "00320-0011801732 Classification: Art Director Compensation: \$70000.00 to \$100000.00 yearly The Creative " \
        "Group is seeking an ART DIRECTOR with experience in the gaming industry to join one o...<\/div>\n<div " \
        "class=\'block\'>\$70k - \$100k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div " \
        "class=\'data-results-bubble bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a " \
        "aria-label=\"Art Director (Concept Art &amp; Character Illustration) jobs in El Segundo\" " \
        "class=\"data-results-content block job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|31\" " \
        "data-job-did=\"J3T72L6V31GM42D7K1K\" data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR31\" " \
        "data-external-company-link=\"\" data-jdp-joblink=\"/job/J3T72L6V31GM42D7K1K\" " \
        "href=\"/job/J3T72L6V31GM42D7K1K\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(\"false\" === " \
        "\"true\") {\n      \$(\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(" \
        "this).children(\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(" \
        "\"hiring event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      " \
        "})\n    }\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3q0nd6kgxhy5lyz1qr\" aria-label=\"Save this Remote Director of " \
        "Automation and Test Engineering job\" " \
        "data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder.com/job" \
        "/J3Q0ND6KGXHY5LYZ1QR?save_job_did=J3Q0ND6KGXHY5LYZ1QR\" data-gtm=\"jrp-job-list|save-link-modal-prompt\" " \
        "href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div " \
        "class=\'col-2 layout-results\'>\n<div class=\'col small col-mobile-inline\'>\n<div " \
        "class=\'data-results-img\'><img alt=\"Remote Director of Automation and Test Engineering Job at city of " \
        "Seattle\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/fe95e189769f858d1f6e3d912cfddece.jpg\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>1 " \
        "day ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Remote Director of Automation and Test " \
        "Engineering<\/div>\n<div class=\'data-details\'>\n<span>Kforce Technology<\/span>\n<span>WA - " \
        "Seattle<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>RESPONSIBILITIES: Kforce\'s Seattle, " \
        "WA based client, a growing and established Technology Healthcare and Medical company seeking a Remote " \
        "Director of Automation and Software Test Engineering. We ar...<\/div>\n<div class=\'block\'>\$150k - " \
        "\$175k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Remote Director of Automation " \
        "and Test Engineering jobs in Seattle\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|32\" data-job-did=\"J3Q0ND6KGXHY5LYZ1QR\" " \
        "data-company-did=\"CHN42X5VT1W3T20JRLY\" data-ipath=\"CRJR32\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3Q0ND6KGXHY5LYZ1QR\" href=\"/job/J3Q0ND6KGXHY5LYZ1QR\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3s0kw6r0wlcw57m553\" aria-label=\"Save this Director of Field " \
        "Marketing job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www" \
        ".careerbuilder.com/job/J3S0KW6R0WLCW57M553?save_job_did=J3S0KW6R0WLCW57M553\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Director of Field Marketing Job at city of " \
        "Boston\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>2 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Director of Field Marketing<\/div>\n<div " \
        "class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>MA - Boston<\/span>\n<span>Full " \
        "Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: 02100-0011915983 Classification: Director " \
        "of Marketing Compensation: \$120000.00 to \$140000.00 yearly We are looking for a Director of Field " \
        "Marketing to help lead the charge in driving our ...<\/div>\n<div class=\'block\'>\$120k - " \
        "\$140k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Field Marketing " \
        "jobs in Boston\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|33\" data-job-did=\"J3S0KW6R0WLCW57M553\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR33\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3S0KW6R0WLCW57M553\" href=\"/job/J3S0KW6R0WLCW57M553\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-jdf3kj6qn0kk28yxcf8\" aria-label=\"Save this Director of Admissions " \
        "job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder.com/job" \
        "/JDF3KJ6QN0KK28YXCF8?save_job_did=JDF3KJ6QN0KK28YXCF8\" data-gtm=\"jrp-job-list|save-link-modal-prompt\" " \
        "href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div " \
        "class=\'col-2 layout-results\'>\n<div class=\'col small col-mobile-inline\'>\n<div " \
        "class=\'data-results-img\'><img alt=\"Director of Admissions Job at city of Tampa\" " \
        "data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production/0c9028119f634c08312969a176971fc4.jpg\" " \
        "class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64," \
        "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div class=\'col big " \
        "col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>2 days ago<\/div>\n<div " \
        "class=\'data-results-title dark-blue-text b\'>Director of Admissions<\/div>\n<div " \
        "class=\'data-details\'>\n<span>Ultimate Medical Academy<\/span>\n<span>FL - Tampa<\/span>\n<span>Full " \
        "Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Purpose of the Position: The Director, " \
        "Admissions (DOA) is responsible for directing a team of advisors who interface with prospective students and " \
        "those influencing the student’s decision to atten...<\/div>\n<div " \
        "class=\'block\'><\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Admissions jobs in Tampa\" " \
        "class=\"data-results-content block job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|34\" " \
        "data-job-did=\"JDF3KJ6QN0KK28YXCF8\" data-company-did=\"C8A3ZL61P2FLMYDH1KS\" data-ipath=\"CRJR34\" " \
        "data-external-company-link=\"\" data-jdp-joblink=\"/job/JDF3KJ6QN0KK28YXCF8\" " \
        "href=\"/job/JDF3KJ6QN0KK28YXCF8\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(\"false\" === " \
        "\"true\") {\n      \$(\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(" \
        "this).children(\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(" \
        "\"hiring event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      " \
        "})\n    }\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j2s5zh76f2lr339jlmq\" aria-label=\"Save this Medical Director - " \
        "Addiction Medicine job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www" \
        ".careerbuilder.com/job/J2S5ZH76F2LR339JLMQ?save_job_did=J2S5ZH76F2LR339JLMQ\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Medical Director - Addiction Medicine Job " \
        "at city of Hanover\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/bec9f34c88893e3e71b7e0d696491def.png\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>4 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Medical Director - Addiction " \
        "Medicine<\/div>\n<div class=\'data-details\'>\n<span>HRselect<\/span>\n<span>PA - " \
        "Hanover<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>We are working with a Full Continuum, " \
        "Evidenced Based, Residential Substance Abuse Facility that is in search of an Addiction Medical Director to " \
        "join their team. This is an exciting opportunity to...<\/div>\n<div class=\'block\'>\$210k - " \
        "\$255k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Medical Director - Addiction " \
        "Medicine jobs in Hanover\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|35\" data-job-did=\"J2S5ZH76F2LR339JLMQ\" " \
        "data-company-did=\"CHP6NY622CT7ST36ZVW\" data-ipath=\"CRJR35\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J2S5ZH76F2LR339JLMQ\" href=\"/job/J2S5ZH76F2LR339JLMQ\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3w73778fqpwk6dzbg2\" aria-label=\"Save this Assistant Director of " \
        "Nursing job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder" \
        ".com/job/J3W73778FQPWK6DZBG2?save_job_did=J3W73778FQPWK6DZBG2\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Assistant Director of Nursing Job at city " \
        "of Orchard City\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/3f493e6249dd7b2037415702bda6204b.png\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>6 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Assistant Director of " \
        "Nursing<\/div>\n<div class=\'data-details\'>\n<span>Volunteers of America National " \
        "Services<\/span>\n<span>CO - Orchard City<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div " \
        "class=\'data-snapshot commute-info\'>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'block " \
        "show-mobile\'>Volunteers of America is looking for a compassionate and experienced leader to join our team " \
        "as ADON at Horizons care center in beautiful Eckert, CO! JOB DESCRIPTION The primary purpose of the " \
        "Assi...<\/div>\n<div class=\'block\'>\$77k - \$83k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div " \
        "class=\'data-results-bubble bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a " \
        "aria-label=\"Assistant Director of Nursing jobs in Orchard City\" class=\"data-results-content block " \
        "job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|36\" data-job-did=\"J3W73778FQPWK6DZBG2\" " \
        "data-company-did=\"C7X53J6D175T84C6LKP\" data-ipath=\"CRJR36\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3W73778FQPWK6DZBG2\" href=\"/job/J3W73778FQPWK6DZBG2\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j2y7376fr0tzxcbj1f1\" aria-label=\"Save this Director of Marketing " \
        "job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder.com/job" \
        "/J2Y7376FR0TZXCBJ1F1?save_job_did=J2Y7376FR0TZXCBJ1F1\" data-gtm=\"jrp-job-list|save-link-modal-prompt\" " \
        "href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div " \
        "class=\'col-2 layout-results\'>\n<div class=\'col small col-mobile-inline\'>\n<div " \
        "class=\'data-results-img\'><img alt=\"Director of Marketing Job at city of Hicksville, " \
        "NY\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production/284edeb80a186174950f05aa2e6fc819" \
        ".jpg\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64," \
        "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div class=\'col big " \
        "col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>21 days ago<\/div>\n<div " \
        "class=\'data-results-title dark-blue-text b\'>Director of Marketing<\/div>\n<div " \
        "class=\'data-details\'>\n<span>NY State Solar<\/span>\n<span>NY - Hicksville<\/span>\n<span>Full " \
        "Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>New York State Solar is seeking a hands-on " \
        "Director of Marketing with experience in B2C industries. In the Director of Marketing role you will design, " \
        "implement and monitor effective marketing stra...<\/div>\n<div class=\'block\'>\$120k - " \
        "\$140k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Marketing jobs in " \
        "Hicksville\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|37\" data-job-did=\"J2Y7376FR0TZXCBJ1F1\" " \
        "data-company-did=\"CDF4S56PLSXY25VR27H\" data-ipath=\"CRJR37\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J2Y7376FR0TZXCBJ1F1\" href=\"/job/J2Y7376FR0TZXCBJ1F1\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-jd94jc79bdqfkzs3dxj\" aria-label=\"Save this Director, ICU,  " \
        "Med Surg job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder" \
        ".com/job/JD94JC79BDQFKZS3DXJ?save_job_did=JD94JC79BDQFKZS3DXJ\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Director, ICU,  Med Surg Job at city of " \
        "Gainesville, Texas\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/aa006229343199ae85d27ba6a391c42d.jpg\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>7 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Director, ICU,  Med Surg<\/div>\n<div " \
        "class=\'data-details\'>\n<span>North Texas Medical Center<\/span>\n<span>TX - " \
        "Gainesville<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot " \
        "commute-info\'>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Director, ICU, " \
        "Med Surg North Texas Medical Center (NTMC), a 60 bed acute care hospital located in Gainesville, Texas, " \
        "seeks an experienced Director, ICU and Med/Surg services. The Director is a Re...<\/div>\n<div " \
        "class=\'block\'>\$50k - \$108,750/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div " \
        "class=\'data-results-bubble bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a " \
        "aria-label=\"Director, ICU,  Med Surg jobs in Gainesville\" class=\"data-results-content block " \
        "job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|38\" data-job-did=\"JD94JC79BDQFKZS3DXJ\" " \
        "data-company-did=\"CCM67B6XYSWG62G79XC\" data-ipath=\"CRJR38\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/JD94JC79BDQFKZS3DXJ\" href=\"/job/JD94JC79BDQFKZS3DXJ\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3w79g63y2s84zdkkq7\" aria-label=\"Save this Human Resources (" \
        "HR)Director job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www" \
        ".careerbuilder.com/job/J3W79G63Y2S84ZDKKQ7?save_job_did=J3W79G63Y2S84ZDKKQ7\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Human Resources (HR)Director Job at city of " \
        "Parsippany\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>7 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Human Resources (" \
        "HR)Director<\/div>\n<div class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>NJ - " \
        "Parsippany<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot " \
        "commute-info\'>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: " \
        "02750-0011910956 Classification: Human Resources (HR) Manager Compensation: \$130000.00 to \$160000.00 " \
        "yearly A busy company in the Livignston area is seeking a Human Resources Director to jo...<\/div>\n<div " \
        "class=\'block\'>\$130k - \$160k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div " \
        "class=\'data-results-bubble bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a " \
        "aria-label=\"Human Resources (HR)Director jobs in Parsippany\" class=\"data-results-content block " \
        "job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|39\" data-job-did=\"J3W79G63Y2S84ZDKKQ7\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR39\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3W79G63Y2S84ZDKKQ7\" href=\"/job/J3W79G63Y2S84ZDKKQ7\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3w41t6bck9p7l96xns\" aria-label=\"Save this Director of " \
        "Finance-M&amp;A Focused- Manufacturing (Luv) job\" " \
        "data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder.com/job" \
        "/J3W41T6BCK9P7L96XNS?save_job_did=J3W41T6BCK9P7L96XNS\" data-gtm=\"jrp-job-list|save-link-modal-prompt\" " \
        "href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div " \
        "class=\'col-2 layout-results\'>\n<div class=\'col small col-mobile-inline\'>\n<div " \
        "class=\'data-results-img\'><img alt=\"Director of Finance-M&A Focused- Manufacturing (Luv) Job at city of " \
        "Atlanta\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>7 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Director of Finance-M&A Focused- " \
        "Manufacturing (Luv)<\/div>\n<div class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>GA - " \
        "Atlanta<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: 00900-0011695355 Classification: " \
        "VP/Director of Finance Compensation: \$185000.00 to \$250000.00 yearly We have been engaged by a industry " \
        "leading company headquartered in Atlanta in its targ...<\/div>\n<div class=\'block\'>\$185k - " \
        "\$250k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Finance-M&amp;A " \
        "Focused- Manufacturing (Luv) jobs in Atlanta\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|40\" data-job-did=\"J3W41T6BCK9P7L96XNS\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR40\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3W41T6BCK9P7L96XNS\" href=\"/job/J3W41T6BCK9P7L96XNS\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j2z5466zxwszx9z6xqs\" aria-label=\"Save this Director - Technology " \
        "Operations job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www" \
        ".careerbuilder.com/job/J2Z5466ZXWSZX9Z6XQS?save_job_did=J2Z5466ZXWSZX9Z6XQS\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Director - Technology Operations Job at " \
        "city of Ann Arbor\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/eb75066c0cbbf4ab44815d704a81b430.jpg\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>28 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Director - Technology " \
        "Operations<\/div>\n<div class=\'data-details\'>\n<span>IHA<\/span>\n<span>MI - Ann Arbor<\/span>\n<span>Full " \
        "Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>POSITION DESCRIPTION: The Director of Technology " \
        "Operations is primarily responsible for the operational excellence of IHA’s technical infrastructure and " \
        "customer service functions. Provides leader...<\/div>\n<div " \
        "class=\'block\'><\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director - Technology Operations jobs " \
        "in Ann Arbor\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|41\" data-job-did=\"J2Z5466ZXWSZX9Z6XQS\" " \
        "data-company-did=\"CD67DM79QQCWVVV3SN0\" data-ipath=\"CRJR41\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J2Z5466ZXWSZX9Z6XQS\" href=\"/job/J2Z5466ZXWSZX9Z6XQS\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-jd87s15x95st1pfkmq7\" aria-label=\"Save this Assistant Director of " \
        "Public Policy job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www" \
        ".careerbuilder.com/job/JD87S15X95ST1PFKMQ7?save_job_did=JD87S15X95ST1PFKMQ7\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Assistant Director of Public Policy Job at " \
        "city of Washington DC\" data-src=\"\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>8 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Assistant Director of Public " \
        "Policy<\/div>\n<div class=\'data-details\'>\n<span>The American Academy of Actuaries<\/span>\n<span>DC - " \
        "Washington<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot " \
        "commute-info\'>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Assistant Director " \
        "of Public Policy Many of today\'s most pressing public policy issues across a wide spectrum of concerns, " \
        "such as climate change, retirement security, health equity, and so many ot...<\/div>\n<div " \
        "class=\'block\'><\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Assistant Director of Public Policy " \
        "jobs in Washington\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|42\" data-job-did=\"JD87S15X95ST1PFKMQ7\" data-company-did=\"\" " \
        "data-ipath=\"CRJR42\" data-external-company-link=\"\" data-jdp-joblink=\"/job/JD87S15X95ST1PFKMQ7\" " \
        "href=\"/job/JD87S15X95ST1PFKMQ7\"><\/a>\n<script>\n  \$(document).ready(function(){\n    if(\"false\" === " \
        "\"true\") {\n      \$(\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(" \
        "this).children(\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(" \
        "\"hiring event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      " \
        "})\n    }\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3m5ss725q7wyf8psz1\" aria-label=\"Save this Director of Human " \
        "Resources job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www" \
        ".careerbuilder.com/job/J3M5SS725Q7WYF8PSZ1?save_job_did=J3M5SS725Q7WYF8PSZ1\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Director of Human Resources Job at city of " \
        "Sanford\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>27 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Director of Human Resources<\/div>\n<div " \
        "class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>FL - Sanford<\/span>\n<span>Full " \
        "Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: 01030-0011884869 Classification: Human " \
        "Resources (HR) Manager Compensation: \$120000.00 to \$140000.00 yearly Human Resources Director opening for " \
        "a Private-Equity owned operation in Sanford....<\/div>\n<div class=\'block\'>\$120k - " \
        "\$140k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Human Resources " \
        "jobs in Sanford\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|43\" data-job-did=\"J3M5SS725Q7WYF8PSZ1\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR43\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3M5SS725Q7WYF8PSZ1\" href=\"/job/J3M5SS725Q7WYF8PSZ1\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3q41f7440xvq7fvpf0\" aria-label=\"Save this Director of Decision " \
        "Support job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder" \
        ".com/job/J3Q41F7440XVQ7FVPF0?save_job_did=J3Q41F7440XVQ7FVPF0\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Director of Decision Support Job at city of " \
        "Chester\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>9 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Director of Decision " \
        "Support<\/div>\n<div class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>PA - " \
        "Chester<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: 03720-0011907276 Classification: Director " \
        "of Accounting Compensation: \$130000.00 to \$145000.00 yearly Are you an experienced professional looking " \
        "for a career transition? There is an impera...<\/div>\n<div class=\'block\'>\$130k - " \
        "\$145k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Decision Support " \
        "jobs in Chester\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|44\" data-job-did=\"J3Q41F7440XVQ7FVPF0\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR44\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3Q41F7440XVQ7FVPF0\" href=\"/job/J3Q41F7440XVQ7FVPF0\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3r3865wmc6ht4g2btk\" aria-label=\"Save this Director - Finance, " \
        "Acquisition Integration job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https" \
        "://www.careerbuilder.com/job/J3R3865WMC6HT4G2BTK?save_job_did=J3R3865WMC6HT4G2BTK\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Director - Finance, Acquisition Integration " \
        "Job at city of Alpharetta\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>27 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Director - Finance, Acquisition " \
        "Integration<\/div>\n<div class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>GA - " \
        "Alpharetta<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot " \
        "commute-info\'>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: " \
        "00870-0011844898 Classification: VP/Director of Finance Compensation: \$165000.00 to \$190000.00 yearly " \
        "SENIOR DIRECTOR OF FINANCE - GLOBAL ACQUISITION AND INTEGRATION - Global, Private Equit...<\/div>\n<div " \
        "class=\'block\'>\$165k - \$190k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div " \
        "class=\'data-results-bubble bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a " \
        "aria-label=\"Director - Finance, Acquisition Integration jobs in Alpharetta\" class=\"data-results-content " \
        "block job-listing-item\" data-gtm=\"jrp-job-list|job-title-click|45\" data-job-did=\"J3R3865WMC6HT4G2BTK\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR45\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3R3865WMC6HT4G2BTK\" href=\"/job/J3R3865WMC6HT4G2BTK\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3t39j6dzf4b2hg2jns\" aria-label=\"Save this Director of Accounting " \
        "job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder.com/job" \
        "/J3T39J6DZF4B2HG2JNS?save_job_did=J3T39J6DZF4B2HG2JNS\" data-gtm=\"jrp-job-list|save-link-modal-prompt\" " \
        "href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div " \
        "class=\'col-2 layout-results\'>\n<div class=\'col small col-mobile-inline\'>\n<div " \
        "class=\'data-results-img\'><img alt=\"Director of Accounting Job at city of Southfield\" " \
        "data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production/296a1e03358f1aa11a66440d406f61a2.png\" " \
        "class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64," \
        "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div class=\'col big " \
        "col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>16 days ago<\/div>\n<div " \
        "class=\'data-results-title dark-blue-text b\'>Director of Accounting<\/div>\n<div " \
        "class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>MI - Southfield<\/span>\n<span>Full " \
        "Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: 02210-0011770485 Classification: Director " \
        "of Accounting Compensation: \$175000.00 to \$185000.00 yearly Director of Accounting Our global client is " \
        "looking to make a critical hire. In the rol...<\/div>\n<div class=\'block\'>\$175k - " \
        "\$185k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Accounting jobs " \
        "in Southfield\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|46\" data-job-did=\"J3T39J6DZF4B2HG2JNS\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR46\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3T39J6DZF4B2HG2JNS\" href=\"/job/J3T39J6DZF4B2HG2JNS\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3r13v75x2nhf9wz53m\" aria-label=\"Save this Director of Accounting " \
        "job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder.com/job" \
        "/J3R13V75X2NHF9WZ53M?save_job_did=J3R13V75X2NHF9WZ53M\" data-gtm=\"jrp-job-list|save-link-modal-prompt\" " \
        "href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div " \
        "class=\'col-2 layout-results\'>\n<div class=\'col small col-mobile-inline\'>\n<div " \
        "class=\'data-results-img\'><img alt=\"Director of Accounting Job at city of Philadelphia\" " \
        "data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production/296a1e03358f1aa11a66440d406f61a2.png\" " \
        "class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64," \
        "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div class=\'col big " \
        "col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>16 days ago<\/div>\n<div " \
        "class=\'data-results-title dark-blue-text b\'>Director of Accounting<\/div>\n<div " \
        "class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>PA - Philadelphia<\/span>\n<span>Full " \
        "Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: 03720-0011804778 Classification: Director " \
        "of Accounting Compensation: \$120000.00 to \$140000.00 yearly Available for an immediate hire, Robert Half " \
        "Finance is searching for a skilled, eager,...<\/div>\n<div class=\'block\'>\$120k - " \
        "\$140k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Accounting jobs " \
        "in Philadelphia\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|47\" data-job-did=\"J3R13V75X2NHF9WZ53M\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR47\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3R13V75X2NHF9WZ53M\" href=\"/job/J3R13V75X2NHF9WZ53M\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3m7ty6hyh5v1fpmj8f\" aria-label=\"Save this Director of Social " \
        "Media job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder" \
        ".com/job/J3M7TY6HYH5V1FPMJ8F?save_job_did=J3M7TY6HYH5V1FPMJ8F\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Director of Social Media Job at city of " \
        "West Hollywood\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>27 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Director of Social Media<\/div>\n<div " \
        "class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>CA - West Hollywood<\/span>\n<span>Full " \
        "Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: 00322-0011884586 Classification: Director " \
        "of Social Media Compensation: \$110000.00 to \$130000.00 yearly TCG is seeking a Social Media Director to " \
        "join our agency client on a permanent basis...<\/div>\n<div class=\'block\'>\$110k - " \
        "\$130k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Director of Social Media jobs " \
        "in West Hollywood\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|48\" data-job-did=\"J3M7TY6HYH5V1FPMJ8F\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR48\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3M7TY6HYH5V1FPMJ8F\" href=\"/job/J3M7TY6HYH5V1FPMJ8F\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3m68g797001th9yf5m\" aria-label=\"Save this Art Director job\" " \
        "data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www.careerbuilder.com/job" \
        "/J3M68G797001TH9YF5M?save_job_did=J3M68G797001TH9YF5M\" data-gtm=\"jrp-job-list|save-link-modal-prompt\" " \
        "href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div " \
        "class=\'col-2 layout-results\'>\n<div class=\'col small col-mobile-inline\'>\n<div " \
        "class=\'data-results-img\'><img alt=\"Art Director Job at city of Lakewood\" " \
        "data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production/296a1e03358f1aa11a66440d406f61a2.png\" " \
        "class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" src=\"data:image/gif;base64," \
        "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" /><\/div>\n<\/div>\n<div class=\'col big " \
        "col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>28 days ago<\/div>\n<div " \
        "class=\'data-results-title dark-blue-text b\'>Art Director<\/div>\n<div " \
        "class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>CO - Lakewood<\/span>\n<span>Full " \
        "Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: 00610-0011883716 Classification: Art " \
        "Director Compensation: \$55000.00 to \$70000.00 yearly Robert Half Marketing & Creative (formerly known as " \
        "The Creative Group/TCG) is partnering with a gl...<\/div>\n<div class=\'block\'>\$55k - " \
        "\$70k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Art Director jobs in " \
        "Lakewood\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|49\" data-job-did=\"J3M68G797001TH9YF5M\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR49\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3M68G797001TH9YF5M\" href=\"/job/J3M68G797001TH9YF5M\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  " \
        "})\n<\/script>\n<\/div>\n\n<div class=\'data-results-content-parent relative\'>\n<a " \
        "class=\"data-results-save-job saved-job-j3p4mz6mzn1jr3sttnl\" aria-label=\"Save this Sr. Director of Fund " \
        "Administration job\" data-saved-jobdid=\"https://www.careerbuilder.com/user/sign-in?next=https://www" \
        ".careerbuilder.com/job/J3P4MZ6MZN1JR3STTNL?save_job_did=J3P4MZ6MZN1JR3STTNL\" " \
        "data-gtm=\"jrp-job-list|save-link-modal-prompt\" href=\"javascript:void(0)\"><i aria-label=\'Saved Job\' " \
        "class=\'fa fa-heart-o\'><\/i>\n<\/a>\n<div class=\'col-2 layout-results\'>\n<div class=\'col small " \
        "col-mobile-inline\'>\n<div class=\'data-results-img\'><img alt=\"Sr. Director of Fund Administration Job at " \
        "city of Denver\" data-src=\"https://www.careerbuilder.com/cdn/optimized/us-production" \
        "/296a1e03358f1aa11a66440d406f61a2.png\" class=\"lazy intl-company-logo\" onerror=\"imgNotLoaded(this)\" " \
        "src=\"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7\" " \
        "/><\/div>\n<\/div>\n<div class=\'col big col-mobile-inline\'>\n<div class=\'data-results-publish-time\'>28 " \
        "days ago<\/div>\n<div class=\'data-results-title dark-blue-text b\'>Sr. Director of Fund " \
        "Administration<\/div>\n<div class=\'data-details\'>\n<span>Robert Half<\/span>\n<span>CO - " \
        "Denver<\/span>\n<span>Full Time<\/span>\n<\/div>\n<div class=\'data-snapshot commute-info\'>\n<\/div>\n<div " \
        "class=\'data-snapshot\'>\n<div class=\'block show-mobile\'>Ref ID: 00610-0011884002 Classification: Fund " \
        "Controller Compensation: \$150000.00 to \$200000.00 yearly Partnering with an investment company in Denver, " \
        "CO looking to add a Senior Director of Fund A...<\/div>\n<div class=\'block\'>\$150k - " \
        "\$200k/year<\/div>\n<\/div>\n<div class=\'data-snapshot\'>\n<div class=\'data-results-bubble " \
        "bubble-green\'>Easy Apply<\/div>\n<\/div>\n<\/div>\n<\/div>\n\n<a aria-label=\"Sr. Director of Fund " \
        "Administration jobs in Denver\" class=\"data-results-content block job-listing-item\" " \
        "data-gtm=\"jrp-job-list|job-title-click|50\" data-job-did=\"J3P4MZ6MZN1JR3STTNL\" " \
        "data-company-did=\"CCM2J66N3HFX0NR4479\" data-ipath=\"CRJR50\" data-external-company-link=\"\" " \
        "data-jdp-joblink=\"/job/J3P4MZ6MZN1JR3STTNL\" href=\"/job/J3P4MZ6MZN1JR3STTNL\"><\/a>\n<script>\n  \$(" \
        "document).ready(function(){\n    if(\"false\" === \"true\") {\n      \$(" \
        "\'.data-results-content-parent\').off().on(\'click\', function(){\n        if (\$(this).children(" \
        "\'a.data-results-content.block.job-listing-item\').context.innerText.toLowerCase().includes(\"hiring " \
        "event\")) {\n          window.dataLayer.push({ \'event\': \'JobSearchClicks\' });\n        }\n      })\n    " \
        "}\n    if(\$(document).find(\'.partner-label\').length == 0){\n      var partnerContainer = \$(" \
        "document).find(\'.data-results-content-parent.partner-job\')[0]\n      \$(\'<div class=\"pt10 pb10 " \
        "partner-label\">Partner Jobs<\/div>\').insertBefore(partnerContainer)\n    }\n  })\n<\/script>\n<\/div>\n "

result = re.findall(r'"/job/.*"\s', slovo)
url = "http://127.0.0.1:8001/mainsystem/paginate/"
data = requests.get(url)
# res1 = re.findall(r'append\(.*\);', data.text)
result1 = re.findall(r'"/job/.{19}\\"\s',  data.text)
print(data.status_code)
print(result1[0][1:-3])
print(result1)
