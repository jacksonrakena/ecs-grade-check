import mechanicalsoup
from bs4 import BeautifulSoup
import pprint
from tinydb import TinyDB, Query
import testing


class Result:
    def __init__(self, subject, assig, mark):
        self.subject = subject
        self.assig = assig
        self.mark = mark

    def __str__(self):
        return str(self.subject) + ": " + str(self.assig) + ": " + str(self.mark) + "\n"

    def __repr__(self):
        return str(self)

def main():
    db = TinyDB("db.json")

    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://apps.ecs.vuw.ac.nz/cgi-bin/studentmarks")
    browser.select_form("form[action=\"/login-ticket\"]")
    browser["username"] = "youngisaa"
    browser["password"] = input("Enter password:")
    browser.submit_selected()

    results = []
    newResults = []

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
        Entry = Query()
        db_result = db.search(
            (Entry.subject == result.subject) & (Entry.assig == result.assig) & (Entry.mark == result.mark))
        if (len(db_result)) == 0:
            db.insert({"subject": result.subject, "assig": result.assig, "mark": result.mark})
            newResults.append(result)

    if len(newResults) > 0:
        print(newResults)
    else:
        print("No new results")

    # pprint.pprint(subject_map)

if __name__ == "__main__":
    main()