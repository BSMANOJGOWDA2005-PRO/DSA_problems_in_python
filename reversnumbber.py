n = 6589                      # number to be reversed
nums = n                      # copy of the original number to manipulate
while nums > 0:               # loop until all digits are processed
    last_digit = nums % 10    # get the last digit of the number
    print(last_digit,end="")  # print the last digit without a newline
    nums = nums // 10         # remove the last digit from the number
    # // is floor division, which discards the decimal part and gives the quotient
