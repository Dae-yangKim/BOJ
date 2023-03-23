menu_arr = []
for i in range(5):
    usr_input = int(input())
    menu_arr.append(usr_input)

hamburger_min = min(menu_arr[0] , min(menu_arr[1] , menu_arr[2]))
juice_min = min(menu_arr[-1] , menu_arr[-2])

result = (hamburger_min + juice_min) - 50
print(result)