import requests

URL = "https://jsonplaceholder.typicode.com/posts/"
RECORDS = 0


def api(url: str):
    response = requests.get(url)
    return response.json()


def process(res):
    local_res = res
    records = len(local_res)
    for i in local_res:
        print(i)
    print(f'processing the response. recors: {records}')
    return records


def update_records(records):
    global RECORDS
    RECORDS += records


def get_all_records():
    print(f'all records: {RECORDS}')


def main():
    get_all_records()

    print("\n\n")

    res = api(URL)
    records = process(res)
    update_records(records)

    print("\n\n")

    get_all_records()


if __name__ == '__main__':
    main()
