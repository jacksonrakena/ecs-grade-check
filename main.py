from random import seed
from random import random
import mechanicalsoup
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
import time
import datetime

import gmail
import userpass


class Result:
    def __init__(self, subject, assig, mark):
        self.subject = subject
        self.assig = assig
        self.mark = mark

    def email_format_space(self, minlen) -> str:
        diff = minlen - len(self.email_format())
        spaces = " " * diff
        return str(self.assig) + ": " + spaces + str(self.mark) + "\n"

    def email_format(self) -> str:
        return str(self.assig) + ": " + str(self.mark) + "\n"

    def __str__(self):
        return str(self.subject) + ": " + str(self.assig) + ": " + str(self.mark) + "\n"

    def __repr__(self):
        return str(self)


def main():
    db = TinyDB("db.json")
    # Drop tables
    # db.drop_tables()

    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://apps.ecs.vuw.ac.nz/cgi-bin/studentmarks")
    browser.select_form("form[action=\"/login-ticket\"]")

    browser["username"] = userpass.get_username()
    browser["password"] = userpass.get_password()
    browser.submit_selected()

    results = []
    new_results = {}

    page = str(browser.page)
    # page = testing.defaultPage
    soup = BeautifulSoup(page, 'html.parser')
    # print(list(soup.children))
    # subject_tags = soup.find_all("h3")
    # for subject_tag in subject_tags:
    #     subject_str = subject_tag.text.strip()
    #     subject_map[subject_str] = []

    mark_tags = soup.find_all(lambda tag: tag.name == "span" and "Final Mark" in tag.text)
    for mark in mark_tags:
        assig_tag = mark.find_parent("h4").find(text=True, recursive=False)
        assig_str = assig_tag.strip().replace("_", " ")
        subject_str = mark.find_previous("h3").text.strip()

        s = assig_str + ": " + mark.text.strip()[len("Final Mark: "):]
        mark_float = float(mark.text.strip()[len("Final Mark: "):])
        x = Result(subject_str, assig_str, mark_float)
        results.append(x)

    for result in results:
        entry_query = Query()
        db_result = db.search(
            (entry_query.subject == result.subject) & (entry_query.assig == result.assig) & (
                        entry_query.mark == result.mark))
        if (len(db_result)) == 0:
            db.insert({"subject": result.subject, "assig": result.assig, "mark": result.mark})
            if result.subject not in new_results:
                new_results[result.subject] = []
            new_results.get(result.subject).append(result)

    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if len(new_results) > 0:
        print(new_results)
        str_list = []
        for subject in new_results.keys():
            str_list.append(subject + "\n\n")
            maxlen = 0
            # Find the max size to align mark with
            for result in new_results.get(subject):
                currlen = len(result.email_format())
                if (currlen > maxlen):
                    maxlen = currlen

            # Append to string list
            for result in new_results.get(subject):
                # str_list.append(" - " + result.assig + ": " + str(result.mark) + "\n")
                str_list.append(result.email_format_space(maxlen))

            str_list.append("\n")

        subject = "New ECS Results" if len(str_list) > 1 else "New ECS Result"
        gmail.send_email(subject, "".join(str_list))
        print("Email sent at: " + time_str)
    else:
        print("No new results at: " + time_str)

    # pprint.pprint(subject_map)


if __name__ == "__main__":
    seed(1)
    while (True):
        main()
        sleep_minutes = 15+(random()*(30-15))
        print("Sleeping for: " + str(sleep_minutes) + " minutes")
        time.sleep(sleep_minutes*60)

