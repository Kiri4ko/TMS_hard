# frontend ------------------------------------------
bucket_3l_list = [" ", " ", " "]
bucket_5l_list = [" ", " ", " ", " ", " "]
clear = "\b" * 10000
front = """

    3l             5l
              _____________
              \{7}{7}{7}{7}{7}{7}{7}{7}{7}{7}{7}/
_________      \{6}{6}{6}{6}{6}{6}{6}{6}{6}/
\{2}{2}{2}{2}{2}{2}{2}/       \{5}{5}{5}{5}{5}{5}{5}/ 
 \{1}{1}{1}{1}{1}/         \{4}{4}{4}{4}{4}/
  \{0}{0}{0}/           \{3}{3}{3}/ 
   ¯¯¯             ¯¯¯
"""

# database ------------------------------------------
database = {
    'bucket_3l': 0,
    'bucket_5l': 0,
}

progress = 0
value_3l = database['bucket_3l']
value_5l = 5 - database['bucket_5l']
value_3l_from_5 = 3 - database['bucket_3l']
value_5l_from_5 = database['bucket_5l']

# backend -------------------------------------------
working = True

while working:

    # --------------------------------------------------------------
    bucket_3l_list = (["@"] * database['bucket_3l'] + [" "] * 3)[:3]
    bucket_5l_list = (["@"] * database['bucket_5l'] + [" "] * 5)[:5]
    print(front.format(*(bucket_3l_list[:4] + bucket_5l_list)))
    cmd = input(">> ")

    # --------------------------------------------------------------

    if cmd == "exit":
        working = False

    if cmd == "fill_3l":
        database['bucket_3l'] = 3
        progress += 1
        value_3l = database['bucket_3l']
        value_3l_from_5 = 3 - database['bucket_3l']
        print(f"Progress: {progress}")

    elif cmd == "pour_3l":
        database['bucket_3l'] = 0
        progress += 1
        value_3l = database['bucket_3l']
        value_3l_from_5 = 3 - database['bucket_3l']
        print(f"Progress: {progress}")

    elif cmd == "pour_5l":
        database['bucket_5l'] = 0
        progress += 1
        value_5l = 5 - database['bucket_5l']
        value_5l_from_5 = database['bucket_5l']
        print(f"Progress: {progress}")

    elif cmd == "fill_5l":
        database['bucket_5l'] = 5
        progress += 1
        value_5l = 5 - database['bucket_5l']
        value_5l_from_5 = database['bucket_5l']
        print(f"Progress: {progress}")

    elif cmd == "pour_from_3_to_5":
        if value_3l < value_5l:
            database['bucket_3l'] -= value_3l
            database['bucket_5l'] += value_3l
            value_5l = 5 - database['bucket_5l']
            value_3l = database['bucket_3l']

        if value_3l >= value_5l:
            database['bucket_5l'] += value_5l
            database['bucket_3l'] -= value_5l
            value_3l = database['bucket_3l']
            value_5l = 5 - database['bucket_5l']
        progress += 1
        print(f"Progress: {progress}")

    elif cmd == "pour_from_5_to_3":
        if value_5l_from_5 > value_3l_from_5:
            database['bucket_3l'] += value_3l_from_5
            database['bucket_5l'] -= value_3l_from_5
            value_5l_from_5 = database['bucket_5l']
            value_3l_from_5 = 3 - database['bucket_3l']

        if value_3l_from_5 >= value_5l_from_5:
            database['bucket_5l'] -= value_5l_from_5
            database['bucket_3l'] += value_5l_from_5
            value_3l_from_5 = 3 - database['bucket_3l']
            value_5l_from_5 = database['bucket_5l']
        progress += 1
        print(f"Progress: {progress}")

        if database['bucket_5l'] == 4:
            print("You decided!", f"Progress: {progress}.")
