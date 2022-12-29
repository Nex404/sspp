

def get_monthly_rate()->float:
    rate = float(input("Whats your monthly savings rate? "))
    return rate

def get_time_period()->int:
    period = int(input("How many month do you want to save: "))
    return period

def get_interest_rate()->float:
    rate = float(input("Whats the yearly interest rate in decimal: "))
    return rate

def get_sum(list_of_monthly_inputs:list, yearly_interest_rate:float)->float:
    sum = 0
    monthly_interest_rate = yearly_interest_rate / 12
    for month in list_of_monthly_inputs:
        sum += month
        sum = sum + sum*monthly_interest_rate

    return sum

def main()->None:
    rate = get_monthly_rate()
    period = get_time_period()
    interest_rate = get_interest_rate()
    r_l = [rate for _ in range(period)]
    print(f"After {period} month and a savings rate of {rate} per month, you would accumalate {period*rate} money.")
    print(f"But you are a smart guy and invested the money with an approximate interest rate of {interest_rate}.")
    print(f"This results in a sum of: {get_sum(r_l, interest_rate):.2f}")


if __name__=="__main__":
    main()