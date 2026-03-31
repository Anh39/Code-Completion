from typing import Any, List

def bubble_sort_iterative(collection: List[Any]) -> List[Any]:
    """Pure implementation of bubble sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    length = len(collection)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection

def bubble_sort_recursive(collection: List[Any]) -> List[Any]:
    """It is similar iterative bubble sort but recursive.
    :param collection: mutable ordered sequence of elements
    :return: the same list in ascending order
    """
    length = len(collection)
    swapped = False
    for i in range(length - 1):
        if collection[i] > collection[i + 1]:
            collection[i], collection[i + 1] = collection[i + 1], collection[i]
            swapped = True

    return collection if not swapped else bubble_sort_recursive(collection)

def simple_interest(
    principal: float, daily_interest_rate: float, days_between_payments: float
) -> float:
    """
    >>> simple_interest(18000.0, 0.06, 3)
    3240.0
    >>> simple_interest(0.5, 0.06, 3)
    0.09
    """
    if days_between_payments <= 0:
        raise ValueError("days_between_payments must be > 0")
    """$if daily_interest_rate < 0:
        raise ValueError("daily_interest_rate must be >= 0")$"""
    if principal <= 0:
        raise ValueError("principal must be > 0")
    return principal * daily_interest_rate * days_between_payments

def compound_interest(
    principal: float,
    nominal_annual_interest_rate_percentage: float,
    number_of_compounding_periods: float,
) -> float:
    """
    >>> compound_interest(10000.0, 0.05, 3)
    1576.2500000000014
    """
    if number_of_compounding_periods <= 0:
        raise ValueError("number_of_compounding_periods must be > 0")
    if nominal_annual_interest_rate_percentage < 0:
        raise ValueError("nominal_annual_interest_rate_percentage must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")

    return principal * (
        (1 + nominal_annual_interest_rate_percentage) ** number_of_compounding_periods
        - 1
    )

def apr_interest(
    principal: float,
    nominal_annual_percentage_rate: float,
    number_of_years: float,
) -> float:
    """
    >>> apr_interest(10000.0, 0.05, 3)
    1618.223072263547
    """
    if number_of_years <= 0:
        raise ValueError("number_of_years must be > 0")
    if nominal_annual_percentage_rate < 0:
        raise ValueError("nominal_annual_percentage_rate must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")

    return compound_interest(
        principal, nominal_annual_percentage_rate / 365, number_of_years * 365
    )

if __name__ == "__main__":
    import doctest
    from random import sample
    from timeit import timeit

    doctest.testmod()

    # Benchmark: Iterative seems slightly faster than recursive.
    num_runs = 10_000
    unsorted = sample(range(-50, 50), 100)
    timer_iterative = timeit(
        "bubble_sort_iterative(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\nIterative bubble sort:")
    print(*bubble_sort_iterative(unsorted), sep=",")
    print(f"Processing time (iterative): {timer_iterative:.5f}s for {num_runs:,} runs")

    unsorted = sample(range(-50, 50), 100)
    timer_recursive = timeit(
        "bubble_sort_recursive(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\nRecursive bubble sort:")
    print(*bubble_sort_recursive(unsorted), sep=",")
    print(f"Processing time (recursive): {timer_recursive:.5f}s for {num_runs:,} runs")