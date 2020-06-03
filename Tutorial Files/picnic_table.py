def print_picnic(items_dict, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))
               
picnic_items = {'croissants': 5, 'grapes': 820, 'coconut water': 1, 'cups': 4, 'napkins': 20}

print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)