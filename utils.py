def add_time_to_date(original_date, time_to_add):
    new_time = original_date.replace(year=original_date.year + time_to_add)
    return new_time