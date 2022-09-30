from datetime import date


def date_to_int(from_data: date):
    return int(from_data.strftime('%Y%m%d').replace('-', ''))
