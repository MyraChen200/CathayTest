def help_jack(items, limit):
    items.sort(key=lambda x: (x['value'], -x['weight']), reverse=True)
    max_value = 0

    for i, item in enumerate(items):
        left_limit = limit
        j = i

        if item['weight'] > limit:
            continue

        curr_max_value = 0
        while left_limit > 0 and j < len(items):
            if left_limit - items[j]['weight'] >= 0:
                curr_max_value += items[j]['value']
                left_limit -= items[j]['weight']
            j += 1
            max_value = max(curr_max_value, max_value)

    return max_value

def run_test():
    items = [ { "weight": 5, "value": 10 }, { "weight": 4, "value": 40 }, { "weight": 6, "value": 30 }, { "weight": 4, "value": 50 } ]
    limit = 10
    print(help_jack(items, limit) == 90)

run_test()
