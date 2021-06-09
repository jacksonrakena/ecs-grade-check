from random import seed
from random import random
import mechanicalsoup
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
import time
import datetime
import gmail
import log
import userpass


class Result:
    def __init__(self, subject, assig, mark):
        self.subject = subject
        self.assig = assig
        self.mark = mark

    def email_format_space(self, minlen) -> str:
        diff = minlen - len(self.email_format())
        spaces = " " * diff
        return str(self.assig) + ": " + spaces + str(self.mark)

    def email_format(self) -> str:
        return str(self.assig) + ": " + str(self.mark)

    def __str__(self):
        return str(self.subject) + ": " + str(self.assig) + ": " + str(self.mark) + "\n"

    def __repr__(self):
        return str(self)


def format_results(results) -> str:
    str_list = []
    first = True
    for subject in results.keys():
        if first:
            first = False
        else:
            str_list.append("\n")
        str_list.append("=" * len(subject) + "\n")
        str_list.append(subject + "\n")
        str_list.append("=" * len(subject) + "\n")
        maxlen = 0
        # Find the max size to align mark with
        for result in results.get(subject):
            currlen = len(result.email_format())
            if currlen > maxlen:
                maxlen = currlen

        # Append to string list
        for result in results.get(subject):
            # str_list.append(" - " + result.assig + ": " + str(result.mark) + "\n")
            str_list.append(result.email_format_space(maxlen) + "\n")

    return "".join(str_list)


def email(new_results):
    """
    Emails the new results
    :param new_results: the new results
    """
    subject = "New ECS Results" if len(new_results) > 1 else "New ECS Result"
    gmail.send_email(subject, format_results(new_results))


def main():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://apps.ecs.vuw.ac.nz/cgi-bin/studentmarks")
    browser.select_form("form[action=\"/login-ticket\"]")

    browser["username"] = userpass.get_username()
    browser["password"] = userpass.get_password()
    browser.submit_selected()

    # Full list of results
    results = []
    # Map of new results <str course, Result result>
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

    # Check for each result, whether the database already contains it
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
    if epoch > 0:
        if len(new_results) > 0:
            email(new_results)
            log.print_log("Email sent at: " + time_str)
            log.log("=================NEW RESULTS=================")
            log.log(format_results(new_results))
            log.log("=============================================")
        else:
            log.print_log("No new results at: " + time_str)
    else:
        log.print_log("Initialized " + str(len(results)) + " results at: " + time_str)
        log.print_log("===============INITIAL RESULTS===============")
        log.print_log(format_results(new_results))
        log.print_log("=============================================")

    # pprint.pprint(subject_map)


if __name__ == "__main__":
    db = TinyDB("db.json")
    # Drop tables
    db.drop_tables()

    # Clear the log
    log.clear()

    # Initialize gmail
    gmail.init()

    seed()
    epoch = 0
    while True:
        main()
        epoch += 1
        # Sleep
        sleep_minutes = 15 + (random() * (30 - 15))
        log.print_log("Sleeping for: " + str(sleep_minutes) + " minutes")
        time.sleep(sleep_minutes * 60)
