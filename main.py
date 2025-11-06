import argparse
from typing import List


def calculate_arithmetic_sequence(
    n: int, total_sum: float, common_diff: float
) -> List[float]:
    """
    Calculate an arithmetic sequence given:
    - n: number of elements
    - total_sum: sum of all elements
    - common_diff: common difference between consecutive terms

    Formula:
    For an arithmetic sequence: a, a+d, a+2d, ..., a+(n-1)d
    Sum = n*a + d*(0+1+2+...+(n-1)) = n*a + d*n*(n-1)/2
    Therefore: a = (Sum - d*n*(n-1)/2) / n
    """
    if n <= 0:
        raise ValueError("Number of elements must be positive")

    first_term = (total_sum - common_diff * n * (n - 1) / 2) / n
    sequence = [first_term + i * common_diff for i in range(n)]

    return sequence


def format_sequence(sequence: List[float]) -> str:
    """Format the sequence for display."""
    return ", ".join(f"{x:.4f}" if x % 1 != 0 else f"{int(x)}" for x in sequence)


def verify_sequence(
    sequence: List[float], expected_sum: float, expected_diff: float
) -> bool:
    """Verify that the sequence meets the requirements."""
    if len(sequence) < 2:
        return abs(sum(sequence) - expected_sum) < 1e-9

    actual_sum = sum(sequence)
    sum_matches = abs(actual_sum - expected_sum) < 1e-9

    differences = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    diff_matches = all(abs(d - expected_diff) < 1e-9 for d in differences)

    return sum_matches and diff_matches


def main():
    parser = argparse.ArgumentParser(
        description="Create an arithmetic sequence given the number of elements, sum, and common difference.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -n 5 -s 25 -d 2
    Creates a sequence of 5 numbers with sum 25 and common difference 2
    Result: 1, 3, 5, 7, 9
  
  %(prog)s -n 4 -s 10 -d 1
    Creates a sequence of 4 numbers with sum 10 and common difference 1
    Result: 1, 2, 3, 4
        """,
    )

    parser.add_argument(
        "-n",
        "--num-elements",
        type=int,
        required=True,
        help="Number of elements in the sequence",
    )

    parser.add_argument(
        "-s",
        "--sum",
        type=float,
        required=True,
        help="Sum of all elements in the sequence",
    )

    parser.add_argument(
        "-d",
        "--diff",
        type=float,
        required=True,
        help="Common difference between consecutive elements",
    )

    parser.add_argument(
        "-v",
        "--verify",
        action="store_true",
        help="Verify that the generated sequence meets the requirements",
    )

    args = parser.parse_args()

    try:
        sequence = calculate_arithmetic_sequence(args.num_elements, args.sum, args.diff)

        print(f"Arithmetic Sequence ({args.num_elements} elements):")
        print(format_sequence(sequence))

        if args.verify:
            is_valid = verify_sequence(sequence, args.sum, args.diff)
            print("\nVerification:")
            print(f"  Sum: {sum(sequence):.4f} (expected: {args.sum})")
            print(f"  Common difference: {args.diff}")
            print(f"  Valid: {'✓' if is_valid else '✗'}")

    except ValueError as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
