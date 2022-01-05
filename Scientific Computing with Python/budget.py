# Replit: https://replit.com/@Mmesek/fcc-budget-app


class Category:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.ledger: list = []

    def deposit(self, amount: float, description: str = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        return False

    def get_balance(self) -> float:
        total = 0
        for entry in self.ledger:
            total += entry["amount"]
        return total

    def total_spent(self) -> float:
        total = 0
        for entry in self.ledger:
            if entry["amount"] < 0:
                total += entry["amount"]
        return abs(total)

    def transfer(self, amount: float, target: "Category") -> bool:
        if self.withdraw(amount, f"Transfer to {target.name}"):
            target.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        if amount <= self.get_balance():
            return True
        return False

    def __str__(self) -> str:
        output = [f"{self.name:*^30}"]
        for entry in self.ledger:
            amount = f"{entry['amount']:>7.2f}"[:7]
            output.append(f"{entry['description'][:23]:<23}{amount}")
        output.append(f"Total: {self.get_balance()}")
        return "\n".join(output)


def create_spend_chart(categories: list[Category]) -> str:
    output = ["Percentage spent by category"]
    total = {}
    percentage = {}
    for category in categories:
        total[category.name] = category.total_spent()

    for category in total:
        percentage[category] = total[category] / sum(total.values()) * 100

    for i in range(100, -10, -10):
        line = f"{i:>3}|"
        for category in percentage:
            if i <= percentage[category]:
                line += " o "
            else:
                line += " " * 3
        output.append(line + " ")
    output.append(" " * 4 + "-" * 3 * len(percentage) + "-")
    for x in range(len(max(percentage.keys(), key=lambda x: len(x)))):
        line = " " * 4
        for category in percentage:
            if x < len(category):
                line += f" {category[x]} "
            else:
                line += " " * 3
        output.append(line + " ")
    with open("budger.txt", "w", newline="", encoding="utf-8") as file:
        file.writelines("\n".join(output))

    return "\n".join(output)


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(105.55, "groceries")
print(food.get_balance())
clothing = Category("Clothing")
clothing.deposit(1000, "initial deposit")
clothing.withdraw(33.40)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(10.99)

print(food)
print(clothing)
print(create_spend_chart([food, clothing, auto]))
