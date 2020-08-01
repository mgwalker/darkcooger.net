import chevron
import json
import os.path
import os
from shutil import move
from datetime import date, timedelta

now = date.today()
template = open("today/day.mustache", "r")


def get_date_from_str(short_date):
    return date(now.year, int(short_date[:2]), int(short_date[2:]))


def get_str_from_date(date):
    return f"{date.month if date.month >= 10 else f'0{date.month}'}{date.day if date.day >= 10 else f'0{date.day}'}"


def get_date_str(date):
    return f"{['', 'January','February','March','April','May','June','July','August','September','October','November','December'][date.month]} {date.day}"


def get_file_name(short_date, year):
    return f"{short_date}_{year}.jpg"


def write_html(short_date, comics, index=False):
    this_day = get_date_from_str(short_date)

    for comic in comics:
        fn = get_file_name(short_date, comic["year"])
        if os.path.isfile(f"today/{fn}"):
            move(f"today/{fn}", f"docs/today/images/{fn}")

    next_date = get_str_from_date(this_day + timedelta(1))
    next_date = next_date if os.path.isfile(f"docs/today/{next_date}.html") else False
    prev_date = get_str_from_date(this_day + timedelta(-1))
    prev_date = prev_date if os.path.isfile(f"docs/today/{prev_date}.html") else False

    template_data = {
        "entries": comics,
        "date": get_date_str(this_day),
        "hero": get_file_name(short_date, comics[0]["year"]),
        "title": f"{comics[0]['year']}: {comics[0]['title']}",
        "next_date": next_date,
        "prev_date": prev_date,
        "short_date": short_date,
    }

    with open(f"docs/today/{short_date}.html", "w") as day_file:
        template.seek(0)
        day_file.write(chevron.render(template, template_data))
        day_file.close()

    if index:
        with open(f"docs/today/index.html", "w") as index_file:
            template.seek(0)
            index_file.write(chevron.render(template, template_data))
            index_file.close()


with open("today/index.json", "r") as f:
    today_meta = json.load(f)
    f.close()

for _ in range(2):
    # for short_date in sorted(today_meta.keys()):
    #     comics = today_meta[short_date]
    #     comic_date = get_date_from_str(short_date)
    #     if comic_date <= now:
    #         write_html(short_date, comics)
    #         if comic_date == now:
    #             write_html(short_date, comics, True)

    all = [
        {"date": get_date_str(get_date_from_str(short_date)), "short_date": short_date}
        for short_date in sorted(today_meta.keys())
    ]
    print(all)

    with open(f"docs/today/all.html", "w") as all_file:
        all_template = open("today/all.mustache", "r")
        all_file.write(chevron.render(all_template, all))
        all_file.close()
        all_template.close()
    # template.seek(0)
    # day_file.write(chevron.render(template, template_data))
    # day_file.close()


template.close()
