# a function that accepts a number and returns the sum of its digits

def sum_digits(num):
        total=0
        original_num=num
        while num!=0:
            rem=num%10         # fetch us digits of a number 'num'
            total+=rem
            num=num//10        # if num was 123, then after this step num becomes 12(123//10=12, neglecting the decimal values)
        print(f"Sum of digits of {original_num} is {total}")

user_inp=int(input("Enter a number: "))
sum_digits(user_inp)