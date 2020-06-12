from os import path, remove, popen
import datetime
import calendar
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor

import requests


def download(day):
    try:
        if day <= datetime.datetime.now().date():
            dt = day.strftime("%m-%d-%Y")
            url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{dt}.csv"
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                with open(f"data/covid-19/world/{dt}.csv", "wb") as f:
                    f.write(r.content)
                return True
    except:
        pass
    return False


def download_brazil(filename, url):
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        with open(f"data/covid-19/brazil/{filename}.csv", "wb") as f:
            f.write(r.content)
        return True


def get_day(months):
    days = []
    for month in months:
        year = 2020
        num_days = calendar.monthrange(year, month)[1]
        days += [datetime.date(year, month, day) for day in range(1, num_days + 1)]
    return days


if __name__ == "__main__":
    data_atual = datetime.datetime.now()
    print(f"Last run: {data_atual}")
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d")

    days = get_day([4, 5, 6, 7])
    with ThreadPoolExecutor(max_workers=cpu_count() * 2) as exc:
        rs = exc.map(download, days)

    a = download_brazil(
        f"cases-brazil-total-{data_atual}",
        "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-total.csv",
    )
    a = download_brazil(
        f"cases-brazil-cities-time-{data_atual}",
        "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities-time.csv",
    )
    a = download_brazil(
        f"cases-brazil-cities-{data_atual}",
        "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv",
    )
