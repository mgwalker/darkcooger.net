import chevron
import json
import os.path
from shutil import copyfile
from datetime import date, timedelta

template = open("today/day.mustache", "r")


def get_date_from_str(short_date):
    return date(2001, int(short_date[:2]), int(short_date[2:]))


def get_str_from_date(date):
    return f"{date.month if date.month >= 10 else f'0{date.month}'}{date.day if date.day >= 10 else f'0{date.day}'}"


with open("today/index.json", "r") as f:
    today_meta = json.load(f)
    f.close()

now = get_str_from_date(date.today())

day = next(d for d in today_meta if d["short_date"] == now)

template.seek(0)
short_date = day["short_date"]

this_day = get_date_from_str(short_date)

for entry in day["entries"]:
    copyfile(f"today/{entry['file']}", f"docs/today/{entry['file']}")

next_date = get_str_from_date(this_day + timedelta(1))
next_date = next_date if os.path.isfile(f"docs/today/{next_date}.html") else False
prev_date = get_str_from_date(this_day + timedelta(-1))
prev_date = prev_date if os.path.isfile(f"docs/today/{prev_date}.html") else False

template_data = {
    **day,
    "hero": day["entries"][0]["file"],
    "title": f"{day['entries'][0]['year']}: {day['entries'][0]['title']}",
    "next_date": next_date,
    "prev_date": prev_date,
}

with open(f"docs/today/{short_date}.html", "w") as day_file:
    day_file.write(chevron.render(template, template_data))
    day_file.close()

if short_date == now:
    with open(f"docs/today/index.html", "w") as index_file:
        template.seek(0)
        index_file.write(chevron.render(template, template_data))
        index_file.close()
