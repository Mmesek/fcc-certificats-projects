# https://replit.com/@Mmesek/fcc-arithmetic-formatter

def arithmetic_arranger(problems: list[str], show_result: bool = False) -> str:
    if len(problems) > 5:
        return "Error: Too many problems."
    result = [""] * 4
    spaces = " " * 4
    for problem in problems:
        a, op, b, = problem.split(" ")
        if any(not i.isdigit() for i in [a, b]):
            return "Error: Numbers must only contain digits."
        if op not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if any(len(i) > 4 for i in [a, b]):
            return "Error: Numbers cannot be more than four digits."
        length = max(len(a), len(b))
        result[0] += f"{a:>{length + 2}}" + spaces
        result[1] += f"{op} {b:>{length}}" + spaces
        result[2] += "-" * (length + 2) + spaces
        if show_result:
            if op == "+":
                r = int(a) + int(b)
            else:
                r = int(a) - int(b)
            result[3] += f"{r:>{length + 2}}"
            result[3] += spaces
    return "\n".join([line.rstrip() for line in result]).rstrip()

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
