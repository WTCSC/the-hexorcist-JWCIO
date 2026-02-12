def to_base(num, base):
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    negative = num < 0
    num = abs(num)
    
    while num > 0:
        remainder = num % base
        result.append(digits[remainder])
        num = num // base
    
    result.reverse()
    return ("-" if negative else "") + "".join(result)


def from_base(num_str, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_str = num_str.upper().strip()
    
    negative = num_str.startswith("-")
    if negative:
        num_str = num_str[1:]
    
    result = 0
    for char in num_str:
        result = result * base + digits.index(char)
    
    return -result if negative else result

def main():
    """Interactive base converter"""
    print("BASE CONVERTER")
    
    while True:
        print("\nChoose an option:")
        print("1. Convert FROM decimal to another base")
        print("2. Convert TO decimal from another base")
        print("3. Convert between two non-decimal bases")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "4":
            print("\nGoodbye!")
            break
        
        elif choice == "1":
            try:
                num = int(input("\nEnter decimal number: "))
                base = int(input("Enter target base (2-36): "))
                
                if base < 2 or base > 36:
                    print("Error: Base must be between 2 and 36")
                    continue
                
                result = to_base(num, base)
                print(f"\n{num} in base {base} = {result}")
                
            except ValueError:
                print("Error: Invalid input. Please enter valid numbers.")
        
        elif choice == "2":
            try:
                num_str = input("\nEnter number: ")
                base = int(input("Enter source base (2-36): "))
                
                if base < 2 or base > 36:
                    print("Error: Base must be between 2 and 36")
                    continue
                
                result = from_base(num_str, base)
                print(f"\n{num_str} (base {base}) = {result} (decimal)")
                
            except (ValueError, IndexError):
                print("Error: Invalid input or digit not valid for given base.")
        
        elif choice == "3":
            try:
                num_str = input("\nEnter number: ")
                from_b = int(input("Enter source base (2-36): "))
                to_b = int(input("Enter target base (2-36): "))
                
                if from_b < 2 or from_b > 36 or to_b < 2 or to_b > 36:
                    print("Error: Bases must be between 2 and 36")
                    continue
                
                decimal = from_base(num_str, from_b)
                result = to_base(decimal, to_b)
                
                print(f"\n{num_str} (base {from_b}) = {decimal} (decimal) = {result} (base {to_b})")
                
            except (ValueError, IndexError):
                print("Error: Invalid input or digit not valid for given base.")
        
        else:
            print("Error: Please enter a number between 1 and 4")

main()