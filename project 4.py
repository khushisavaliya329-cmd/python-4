
summary = {}


def input_data():
    """Take 1D or 2D data from the user."""
    print("1. 1D List")
    print("2. 2D List")
    choice = input("Enter choice: ")

    print("1. Sample Data")
    print("2. Manual Data")
    method = input("Enter choice: ")

    if choice == "1":
        if method == "1":
            return [10, 20, 30, 20, 40, 50], False
        data = [int(x) for x in input("Enter numbers: ").split(",")]
        return data, False

    if choice == "2":
        if method == "1":
            return [[10, 20], [30, 40], [50, 60]], True

        rows = int(input("Enter number of rows: "))
        data = []
        for i in range(rows):
            row = [int(x) for x in input("Enter row: ").split(",")]
            data.append(row)
        return data, True

    print("Invalid choice")
    return [10, 20, 30], False

def flatten(data, two_d):
    """Convert 2D list into 1D list."""
    if two_d:
        return [x for row in data for x in row]
    return data

def display(data, two_d):
    """Display the dataset."""
    if two_d:
        for row in data:
            print(*row, sep="\t")
    else:
        print(data)

def statistics(data):
    """Display basic statistics."""
    print("Length:", len(data))
    print("Sum:", sum(data))
    print("Minimum:", min(data))
    print("Maximum:", max(data))
    print("Average:", sum(data) / len(data))

def average(data):
    """Calculate average of values."""
    return sum(data) / len(data)

def duplicates(data):
    """Find duplicate values."""
    result = []
    for x in data:
        if data.count(x) > 1 and x not in result:
            result.append(x)
    print("Duplicates:", result)

def show_values(*args):
    """Display multiple values using args."""
    for x in args:
        print(x)

def show_summary(**kwargs):
    """Display dataset summary using kwargs."""
    list(map(lambda x: print(x[0], ":", x[1]), kwargs.items()))

def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Calculate Fibonacci using recursion."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def filter_data(data):
    """Filter and transform values using lambda."""
    limit = int(input("Enter threshold: "))
    result = list(filter(lambda x: x > limit, data))
    print("Filtered values:", result)
    print("Doubled values:", list(map(lambda x: x * 2, result)))

def update_summary(data):
    """Update global dataset summary."""
    global summary
    summary = {
        "Total": len(data),
        "Mean": average(data)
    }
    print(summary)

def multiple_values(data):
    """Return minimum, maximum and average."""
    return min(data), max(data), average(data)

def sorting(data, two_d):
    """Sort 1D or 2D list."""
    order = input("1. Ascending  2. Descending: ")
    reverse = order == "2"

    if two_d:
        result = [sorted(row, reverse=reverse) for row in data]
        print("Original:", data)
        print("Sorted:", result)
    else:
        data.sort(reverse=reverse)
        print("Sorted list:", data)

def main():
    """Run the main menu program."""
    data, two_d = input_data()

    while True:
        print("\n1.Display  2.Statistics  3.Average")
        print("4.Duplicates  5.Args  6.Kwargs")
        print("7.Factorial  8.Fibonacci  9.Lambda")
        print("10.Global  11.Multiple Values")
        print("12.Sort  13.Change Data  14.Exit")

        choice = input("Enter choice: ")
        values = flatten(data, two_d)

        if choice != "1" and choice != "13" and choice != "14" and not values:
            print("Dataset is empty")

        elif choice == "1":
            display(data, two_d)

        elif choice == "2":
            statistics(values)

        elif choice == "3":
            print("Average:", average(values))

        elif choice == "4":
            duplicates(values)

        elif choice == "5":
            show_values(*values)

        elif choice == "6":
            show_summary(total=len(values), sum=sum(values),
                         minimum=min(values), maximum=max(values),
                         average=average(values))

        elif choice == "7":
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n) if n >= 0 else "Invalid number")

        elif choice == "8":
            n = int(input("Enter terms: "))
            if n < 0:
                print("Invalid number")
            else:
                for i in range(n):
                    print(fibonacci(i), end=" ")
                print()

        elif choice == "9":
            filter_data(values)

        elif choice == "10":
            update_summary(values)

        elif choice == "11":
            print("Minimum, Maximum, Average:", multiple_values(values))

        elif choice == "12":
            sorting(data, two_d)

        elif choice == "13":
            data, two_d = input_data()

        elif choice == "14":
            print("Thank you!")
            break

        else:
            print("Invalid choice")


main()
