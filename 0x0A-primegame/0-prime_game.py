#!/usr/bin/python3
"""Prime Game. The person who cannot make a move loses the round.
"""


def isWinner(x, nums):
    """Main Prime game function. Determine the winner. Max number of rounds
    won.
    """
    # Check for edge cases:
    try:
        assert type(x) == int and x >= 1 and x <= 10000
        assert type(nums) == list
        for n in nums:
            assert type(n) == int and n >= 1 n <= 10000
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

    if marias >= bens:
        return "Maria"
    elif bens > marias:
        return "Ben"


if __name__ == "--main__":
    print("Winner:", isWinner(3, [4, 5, 1]))  # "Ben"
