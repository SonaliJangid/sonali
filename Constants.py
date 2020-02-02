opportunity_desk = "http://opportunitydesk.org/"
intercompetition = "http://intercompetition.com/"
youthop = "https://www.youthop.com/"
mladinfo = "http://www.mladiinfo.eu/"
globeopportunities = "http://globeopportunities.com/"
armacad = "http://armacad.info"
agorize = "https://www.agorize.com/en/challenges"
marj3 = "https://www.marj3.com/en"
oyaop = "www.oyaop.com"
heysuccess = "http://www.heysuccess.com/"
opportunitiesforafricans = "https://www.opportunitiesforafricans.com/"

oppDesk_sheet_url = "oppDesk"
armacad_sheets_url = "armacad"
intercompetition_sheets_url = "intercompetition"
miladinfo_sheets_url = "miladinfo"
youthop_sheets_url = "youthop"
oyaopp_sheets_url = "oyaOp"
marj3_url = "marj3"
globeopportunities_url = "globeopportunities"
agorize_url = "agorize"
opportunitiesforafricans_url = "opportunitiesforafricans"

headline = "Headline"
description = "Description"
funding = "Funding"
deadline = "Deadline"
image_link = "Image Link"
official_link = "Official Link"
type = "Type"
sub_type = "SubType"
discipline = "Discipline"
minimum_qualification = "Minimum Qualification"
eligible_regions = "Eligible Regions"
where = "Where"
opportunity_link_on_website = "Opportunity Link on Website"

heading = [headline, description, funding, deadline, image_link, official_link, type, sub_type, discipline,
           minimum_qualification, eligible_regions, where, opportunity_link_on_website]

headline_index = 0
description_index = 1
funding_index = 2
deadline_index = 3
image_link_index = 4
official_link_index = 5
type_index = 6
sub_type_index = 7
discipline_index = 8
minimum_qualification_index = 9
eligible_regions_index = 10
where_index = 11
opportunity_link_on_website_index = 12

header_length = len(heading)

root = {opportunity_desk: 'https://opportunitydesk.org/category/{}/page/{}/',
        armacad: 'https://armacad.info/opportunities/{}?page={}',
        intercompetition: 'http://intercompetition.com/all.html?cid=0&order=date_e&ord_t=asc&start={}',
        youthop: 'https://www.youthop.com/browse/page/{}',
        oyaop: 'https://oyaop.com/page/{}/?s&opp&ven&submit=Search#038;opp&ven&submit=Search',
        marj3: 'https://www.marj3.com/en/scholarships?_sft_category={}&sf_paged={}',
        globeopportunities: 'https://globeopportunities.com/category/{}/page/{}/',
        agorize: 'https://www.agorize.com/api/v1/challenges',
        }

categories = {
    opportunity_desk: ['fellowships-and-scholarships', 'contests', 'grants', 'fellowships', 'training-and-conference'],
    armacad: ['grants', 'scholarships', 'fellowships', 'awards', 'study', 'online', 'prize', 'publications',
              'competition', 'financial-aid'],
    marj3: ['degree-scholarships', 'ib-scholarships-high-school', 'master-scholarships', 'phd-scholarships', 'post-doc',
            'undergraduate-scholarships-bachelor', 'vocational-diploma-2-years-before-university',
            'non-degree-opportunities', 'academic-and-long-term-fellowshipsresearch', 'accelerators-for-startups',
            'competitions-prizes-awards-and-grants', 'events-forum-summit-conference-seminar-and-symposium',
            'programs-en', 'international-certificate-programs', 'internships-and-summer-training',
            'non-academicshort-term-fellowships', 'programs-and-training-courses', 'summer-school',
            'volunteering-programs'],
    globeopportunities: ['conferences', 'fellowships', 'internship', 'forum', 'volunteering', 'scholarships',
                         'training'],
}

page_end = 10
