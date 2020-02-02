import copy
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import Constants as cs
from confirm_with_db import check_if_new_opp
from util import print_exec_plus

# dir = "/var/www/html/lithics/apis/mauka/scripts"
dir = os.path.split(os.path.realpath(__file__))[0]

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(dir + '/Precisely-Translate-983b30831fad.json', scope)
# credentials = ServiceAccountCredentials.from_json_keyfile_name('precisely-361706e15b95.json', scope)
gc = gspread.authorize(credentials)


def add_opps_to_sheet(sheet_title, category, data):
    opps_list = copy.deepcopy(data)
    deletions = 0
    for index, opp in enumerate(data):
        if not check_if_new_opp(
                [opp[cs.headline_index], opp[cs.deadline_index], opp[cs.opportunity_link_on_website_index]]):
            del opps_list[index - deletions]
            deletions += 1

    try:
        opened_wk = gc.open(sheet_title)
        wks = opened_wk.worksheets()
        titles = []
        for wk in wks:
            titles.append(wk.title)
        if category not in titles:
            opened_wk.add_worksheet(title=category, rows=1000, cols=len(cs.heading))

        opened_wk = gc.open(sheet_title)
        wks = opened_wk.worksheets()

        for wk in wks:
            if wk.title == category:
                all_vals = wk.get_all_values()
                total_rows = len(all_vals)

                opps_list = sorted(opps_list, key=lambda x: (x[cs.deadline_index] is None, x[cs.deadline_index]))

                if total_rows == 0:
                    opps_list.insert(0, cs.heading)

                total_new__opps = len(opps_list)

                if total_new__opps > 0:
                    range_build = 'A' + str(total_rows + 1) + ':' + chr(ord('A') + (cs.header_length - 1)) + str(
                        total_rows + total_new__opps)
                    cell_list = wk.range(range_build)

                    first_row = cell_list[0].row
                    for index, cell in enumerate(cell_list):
                        row = cell._row - first_row
                        col = cell.col - 1
                        data = str(opps_list[row][col])
                        if data is None or data == "None":
                            data = ""
                        cell.value = data

                    wk.update_cells(cell_list, value_input_option="USER_ENTERED")

                print("DONE")
    except Exception as e:
        print_exec_plus()
