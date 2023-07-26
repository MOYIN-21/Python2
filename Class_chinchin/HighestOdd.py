def mean(number):
    numbers = number[0]
    for y in number:
        if y % 2 != 0:
            if numbers > y:
                numbers = y

        return numbers


read = [87, 50, 83]
call = mean(read)
print(f"largest:{call}")
