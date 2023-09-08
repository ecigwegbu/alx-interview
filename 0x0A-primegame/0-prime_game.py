#!/usr/bin/python3
"""Prime Game. This code
"""


def isWinner(x, nums):
    """Main Prime game function. Determine the winner.
    """
    # Check for edge cases:
    try:
        assert type(x) == int
        assert nums and type(nums) == list and len(nums) == x
        for n in nums:
            assert type(n) == int  # n can be 0, in which case round skipped
    except Exception:
        #  raise
        return None

    if x == 0:
        return "None"

    def is_prime(n):
        """Helper function 1
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def play_round(n):
        """Helper function to determine who wins the round.
        If n is 1, Ben wins automatically since Maria cannot make the move
        If n is 0, round_winner is None
        """
        if n == 0:
            return "Maria"  # None ?
        primes = [i for i in range(1, n + 1) if is_prime(i)]
        non_primes = [i for i in range(1, n + 1) if not is_prime(i)]

        turn = "Maria"
        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            non_primes = [np for np in non_primes if np % prime != 0]

            if primes or non_primes:
                turn = "Ben" if turn == "Maria" else "Maria"
            else:
                return turn
        return "Ben" if turn == "Maria" else "Maria"

    marias = 0
    bens = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            marias += 1
        elif winner == "Ben":
            bens += 1

    if marias > bens:
        return "Maria"
    elif bens > marias:
        return "Ben"
    else:
        return None


if __name__ == "--main__":
    print("Winner:", isWinner(3, [4, 5, 1]))  # "Ben"
