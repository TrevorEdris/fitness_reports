import csv


def read_csv_file(filename):
    # NOTE: Could refactor this to take in a `should_append_function` parameter
    #       that is a pointer to a function that would return True/False,
    #       indicating whether or not the reader should append a particular row
    data = []
    line_count = 0
    try:
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                data.append(row)
                line_count += 1
    except Exception as e:
        print(f'Unable to read {filename}: {e}')
    print(f'Read {line_count} lines from {filename}')
    return data


def load_exempt(filename):
    _data = read_csv_file(filename)
    exempt = []
    for row in _data:
        if len(row) < 1:
            continue
        exempt.append(row[0])
    return exempt


def load_data(filename, exempt):
    _data = read_csv_file(filename)
    data = []
    for row in _data:
        if should_append(row, exempt):
            data.append(row)
    return data


def should_append(row, exempt):
    if len(row) < 1:
        return False

    decision = False
    if row[0] and row[0] not in exempt:
        decision = True
    return decision
