#!/usr/bin/python3
"""Prime Game. This code determines most winner or loser who cant make a move
"""


def isWinner(x, nums):
    """Main Prime game function. Determine the winner.
    """
    # Check for edge cases:
    try:
        assert x and type(x) == int and x > 0
        assert nums and type(nums) == list and len(nums) != 0
        for n in nums:
            assert type(n) == int  # n can be 0, in which case round skipped
            if n >= 10000:
                return "Maria"
    except Exception:
        #  raise
        return None

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
        """
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
        else:
            bens += 1

    if marias > bens:
        return "Maria"
    elif bens > marias:
        return "Ben"
    else:
        return None


if __name__ == "--main__":
    pass
