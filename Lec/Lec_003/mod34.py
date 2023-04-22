def maxToMin (start_list):
    end_list = []
    max = start_list[0]
    min = start_list[0]

    for i in start_list:
        if i > max:
            max = i
        elif i < min:
            min = i

    for i in start_list:
        if i == max:
            i = min
        end_list.append(i)

    return end_list