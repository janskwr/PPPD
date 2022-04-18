def main():
    number = int(input("Podaj liczbę całkowitą większą niż 1: "))
    number_at_beginning = number
    if number <= 1:
        raise Exception("Liczba miała być większa niż 1!")
    else:
        primary_number = 2
        counter_of_unique_divisors = 0
        counter_of_tuples = 0
        tuples_storage = 0
        iterator_for_tuple_storage = 1
        previous_prime = -1
        new_prime_decomposition = 1
        while number > 1:
            while number % primary_number == 0:
                number = number // primary_number
                if previous_prime != primary_number:
                    counter_of_unique_divisors += 1
                previous_prime = primary_number
                counter_of_tuples += 1
            if counter_of_tuples > 0:
                if counter_of_tuples > 1:
                    new_prime_decomposition = new_prime_decomposition * (primary_number ** (counter_of_tuples - 1))
            tuples_storage += counter_of_tuples * iterator_for_tuple_storage
            counter_of_tuples = 0
            iterator_for_tuple_storage = iterator_for_tuple_storage * 10
            primary_number += 1
    print(f"Liczba różnych dzielników pierwszych {number_at_beginning} wynosi {counter_of_unique_divisors}.")
    print("Krotności tych dzielników to kolejno:")
    while tuples_storage > 0:
        if tuples_storage % 10 != 0:
            print(tuples_storage % 10)
        tuples_storage //= 10
    if new_prime_decomposition > 1:
        print(f"Po zmniejszeniu krotności każdego dzielnika pierwszego o 1 otrzymamy liczbę {new_prime_decomposition}.")
    else:
        print("Po zmniejszeniu krotności każdego dzielnika pierwszego o 1 otrzymamy liczbę 0.")


if __name__ == '__main__':
    main()
