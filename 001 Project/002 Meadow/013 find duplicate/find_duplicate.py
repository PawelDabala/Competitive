
rows = [
    ["cztery", "piec", "szejsc"],
    ["jeden", "dwa", "trzy"],
    ["cztery", "piec", "szejsc"],
    ["siedem", "osiem", "dziewic"],
    ["dziesiem", "jedenascie", "dwanascie"],
    ["trzynasicie", "czternascie", "pietnascie"],
    ["cztery", "piec", "szejsc"],
    ["siedem", "osiem", "dziewic"],
]

def remove_duplicate(rows):

    for nr in reversed(range(len(rows))):
        print(rows[nr], nr)
        if rows[1:2].count(rows[nr]) > 1:
            rows.pop(nr)

    return rows

def count_duplicate(rows):
    return abs(len(set(map(tuple, rows)))-len(rows))


remove_duplicate(rows)
# print(count_duplicate(rows))


