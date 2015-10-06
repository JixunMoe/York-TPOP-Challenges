# Challenge I: prime numbers

## The Problem
A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

The property of being prime is called primality. A simple but slow method of verifying the primality of a given number `n` is known as trial division. It
consists of testing whether `n` is a multiple of any integer between 2 and ![sqrt of n](//i.imgur.com/YXrcf2k.png).

## The Basic
Write a program that, given a number comprised between 2 and 49, returns if it is a prime number or not. We can assume that the computer knows (stores) that `[2, 3, 5, 7]` are prime numbers.

## The Advanced Bit
Write a program that, given a number greater than 2, returns if it is a prime number or not. We can assume that the computer at the start knows only that 2 is prime number. We should use a loop to test several numbers.

## The Clever One
Write a program that, given a number greater than 2, returns if it is a prime number or not. We can assume that the computer at the start knows only that 2 is prime number. Every time the program is ran, it should remember the prime numbers it has found before.

## The Olympian One
Taken from the 2012 British Informatics Olympiad.

Every integer greater than 1 can be uniquely expressed as the product of prime numbers (ignoring reordering those numbers). This is called the prime factorisation of the number.

For example:

* 100 = 2 × 2 × 5 × 5
* 101 = 101 (since 101 is a prime number)

We are interested in the product of the distinct prime factors of a given number; in other words each number in the prime factorisation is to be used only once. Since `100 = 2 × 2 × 5 × 5` the product we require is `10` (i.e. `2 × 5`). Write a program which reads in a single integer `n` `(1 < n < 1,000,000)` and outputs a single integer, the product of the distinct prime factors of n.
