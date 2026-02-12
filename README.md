# Base Converter

A Python implementation of a number base converter that works **without** using Python's built-in conversion functions (`bin`, `hex`, `oct`, `int` with base parameter, or `format`).

## Overview

This program demonstrates the mathematical principles behind base conversion by implementing the algorithms from scratch. It supports conversion between any bases from 2 (binary) to 36 (using digits 0-9 and letters A-Z).

## How It Works

### Converting TO a Base (from decimal)

The algorithm uses **repeated division with remainder**:

1. Divide the number by the target base
2. The remainder becomes the next digit (reading right to left)
3. Continue with the quotient until it reaches zero
4. Reverse the collected digits

**Example:** Converting 255 to hexadecimal (base 16)
```
255 ÷ 16 = 15 remainder 15 (F)
15 ÷ 16 = 0 remainder 15 (F)
Result: FF
```

### Converting FROM a Base (to decimal)

The algorithm uses **positional notation** (Horner's method):

1. Start with a result of 0
2. For each digit from left to right:
   - Multiply the current result by the base
   - Add the value of the current digit
3. This builds up the decimal value

**Example:** Converting FF (hex) to decimal
```
Start: 0
F (15): 0 × 16 + 15 = 15
F (15): 15 × 16 + 15 = 255
Result: 255
```

## Features

- Convert from decimal to any base (2-36)
- Convert to decimal from any base (2-36)
- Convert between two non-decimal bases
- Interactive command-line interface
- Input validation and error handling
- Support for negative numbers

## Usage

Run the program:

```bash
python hex.py
```

### Menu Options

**1. Convert FROM decimal to another base**
```
Enter decimal number: 255
Enter target base (2-36): 16
255 in base 16 = FF
```

**2. Convert TO decimal from another base**
```
Enter number: FF
Enter source base (2-36): 16
FF (base 16) = 255 (decimal)
```

**3. Convert between two non-decimal bases**
```
Enter number: 11111111
Enter source base (2-36): 2
Enter target base (2-36): 16
11111111 (base 2) = 255 (decimal) = FF (base 16)
```

## Common Base Examples

| Base | Name        | Digits Used    | Example |
|------|-------------|----------------|---------|
| 2    | Binary      | 0-1            | 1010    |
| 8    | Octal       | 0-7            | 377     |
| 10   | Decimal     | 0-9            | 255     |
| 16   | Hexadecimal | 0-9, A-F       | FF      |
| 36   | Base-36     | 0-9, A-Z       | 73      |

## Educational Purpose

This implementation is designed for teaching and learning. Each function includes detailed line-by-line comments explaining the mathematical operations. It's perfect for:

- Understanding how number systems work
- Learning algorithm implementation
- Exploring mathematical operations in programming
- Teaching computer science fundamentals

## Requirements

- Python 3.x
- No external dependencies

## Implementation Details

The program consists of three main functions:

- `to_base(num, base)`: Converts a decimal number to any base
- `from_base(num_str, base)`: Converts a string in any base to decimal
- `main()`: Interactive CLI interface

All conversions between non-decimal bases go through decimal as an intermediate step.

## Limitations

- Bases are limited to 2-36 (using digits 0-9 and letters A-Z)
- Input numbers must be integers (no floating-point support)
- Very large numbers may be slow due to the iterative algorithms
