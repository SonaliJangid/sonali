import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse

import Constants as cs
from util import print_exec_plus


def opportunity_details_extractor(link):
    content_dict = [None] * cs.header_length
    # content_dict is a empty dictionary
    # header_length is the length of the heading list
    try:
        source = requests.get(link)
        #  getting the link and storing in the source
        soup = BeautifulSoup(source.text)
        #  extracting the text from the source
    except Exception as e:
        # if any exception occur print the link
        print(link)
        print_exec_plus()

    # HEADLINE
    try:
        # headline_index is the key value (0) in which we are storing the value(headline as a text)
        content_dict[cs.headline_index] = soup.find('h1').text.strip()
    #     finding all the h1 tags then getting only the text part with the help of strip()
    except Exception as e:
        print(link)
        print_exec_plus()
        pass
    # pass is a keyword which executes nothing
    # means if there is any exeception pass the code

    # DESCRIPTION
    try:
        entry_content = soup.find('div', {'class': 'entry-content'})
        # finding the div with class=entry-content and storing in entry_content as a variable
        entry_content = entry_content.get_text().strip()
        # extracting only the text part
        lines_entry_content = entry_content.splitlines()
        # splitlines() is a method which breaks the string at line boundaries and returns a list of splitted strings
        lines_entry_content = '\n'.join([line for line in lines_entry_content if "adsbygoogle" not in line])
        # joining all the lines if there are no "adsbygoogle"
        content_dict[cs.description_index] = lines_entry_content
    #    description_index(1) is the key of content_dict
    #  storing the lines_entry_content(text) as value in the dict
    except Exception as e:
        print(link)
        print_exec_plus()
        pass
    # IMAGE LINK
    try:
        content_dict[cs.image_link_index] = cs.armacad + \
                                            soup.find('img', alt=lambda x: x and 'Opportunity Cover Image' in x)[
                                                'src'].strip()
    except Exception as e:
        print(link)
        print_exec_plus()
        pass
    # OFFICIAL LINK
    try:
        content_dict[cs.official_link_index] = soup.find(text=lambda x: x and x.lower() == 'Link To Original').get(
            'href').strip()
    except Exception as e:
        print(link)
        print_exec_plus()
        pass
    # OPP LINK ON WEBSITE
    try:
        content_dict[cs.opportunity_link_on_website_index] = link.strip()
    #     opportunity_link_on_website_index is the key in  the dict
    #     extracting the link and storing it as value in th dict
    except Exception as e:
        print(link)
        print_exec_plus()
        pass
    # DEADLINE
    try:
        content_dict[cs.deadline_index] = parse(soup.find(
            lambda tag: tag.name == "h3" and "Deadline" in tag.text).parent.parent.find('strong').text.strip(),
                                                fuzzy=True)
    except Exception as e:
        print(link)
        print_exec_plus()
        pass
    # DISCIPLINE
    try:
        disciplines_list = soup.find(lambda tag: tag.name == "h3" and "Disciplines" in tag.text).parent.parent.findAll(
            'a')
        content_dict[cs.discipline_index] = [x.text for x in disciplines_list]
    except Exception as e:
        print(link)
        print_exec_plus()
        pass
    # ELIGIBLE COUNTRIES
    try:
        content_dict[cs.eligible_regions_index] = soup.find(text='Eligible Countries').findNext('span').text
    #
    except Exception as e:
        print(link)
        print_exec_plus()
        pass
    # HOST COUNTRY
    try:
        content_dict[cs.where_index] = soup.find(text='Host Country').findNext('span').text
    except Exception as e:
        print(link)
        print_exec_plus()
        pass
    # QUALIFICATION
    try:
        content_dict[cs.minimum_qualification_index] = soup.find(text='Study Levels').findNext('span').text
    except Exception as e:
        print(link)
        print_exec_plus()
        pass
    # TYPE
    try:
        if content_dict[cs.type_index] is None:
            content_dict[cs.type_index] = []
        content_dict[cs.type_index].append(soup.find(text='Opportunities').findNext('span').text)
    except Exception as e:
        print(link)
        print_exec_plus()
        pass

    return content_dict


def pageLinkExtractor(source):
    headers = {'Referer': 'https://armacad.info/opportunities/grants',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/75.0.3770.142 Safari/537.36'}
    # Extract all opp links in a page
    with open('armacad.html', 'r', encoding='UTF-8') as file:
        html = file.read().replace('\n', '')

    # html = requests.get(source , verify=False)
    soup = BeautifulSoup(html)
    # links is an empty list


    links = []
    # all_opps_wrapper_element is a variable in which we are storing the all found division with id=w0
    all_opps_wrapper_element = soup.find('div', {'id': 'w0'})
    # now we are searching again all division (class=row) in the div (id=w0)
    all_opps_wrapper_element = all_opps_wrapper_element.find('div', {'class': 'row'})
    # for loop: finding all 'a' tag in all_opps_wrapper_element
    for tag in all_opps_wrapper_element.findAll('a'):
        # try is used to handle errors n exceptions while executing the code
        try:
            # here we are appending the found elements(href tags) in the empty list i.e. links[]
            links.append(tag.get('href'))
        except Exception as e:
            # Exception is a pre defined class which is used to handle the exceptions occur during the execution of try block
            print_exec_plus()
            # print_exec_plus() is a pre defined func in util package.
            continue
            # continue the further execution of code
    return links


    # returning the values in the list i.e. links[]

    # In[141]:


def pageBrowser(page_begin=0):
    # empty list
    all_opps_info = []
    #  there is a for loop in which category is a variable and cs.categories( categories
    # is a dic in which there are keys like opportunity_desk,armacad,marj3,globeopportunities . these keys are having
    # lists as values . cs is the object which is used to acess the lists )
    #

    for category in cs.categories[cs.armacad]:
        # empty list
        all_links = []

        # Get all URLs for opportunities present in all pages
        # now there is a nested loop which has page_number as index variable , range is from page_begin(0) to page_end +1(10+1)
        for page_number in range(page_begin, cs.page_end + 1):
            # now we are appending all opportunties link in the epmty list i.e. all_links=[]
            # pagelinkExtractor is a function which is called here.
            # root is a dict in which there are keys and list as values.
            # format is a pre defined function in which we are substituting the values of category and page_number in a string.
            # so in this statement we are first extracting the link then from root dict we are taking value of armacad with csas a object then in that
            # we are substituting the category and page number and atlast we are appending in a list (all_links)
            all_links.append(pageLinkExtractor(cs.root[cs.armacad].format(category, page_number)))

        all_links = sum(all_links, [])
        # counting the length of lists
        print("There have been {} links extracted".format(len(all_links)))
        # in this we are substituting the found length of all_links in the print statement

        # for loop: in this loop we are basically extracting the details from the each element in the all_links list
        for link in all_links:
            all_opps_info.append(opportunity_details_extractor(cs.armacad + link))
    # all_opps_info is list in which we are appending all the extract details
    return all_opps_info


pageBrowser()
