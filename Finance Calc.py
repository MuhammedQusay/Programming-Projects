from os import system


def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_net_income: float = yearly_salary - yearly_tax

    system("cls||clear")

    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')


def main() -> None:
    while True:
        try:
            monthly_income: float = float(input('Enter your monthly income: '))
            tax_rate: float = float(input('Enter your tax rate (%): '))
            currency = input("Enter your currency: ")

            if monthly_income <= 0 or tax_rate < 0:
                print("Please enter valid positive values for income and tax rate.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for income and tax rate.")


    calculate_finances(monthly_income, tax_rate, currency)


if __name__ == "__main__":
    main()
