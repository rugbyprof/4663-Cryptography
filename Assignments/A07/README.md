## Assignment 6 - Finding Primes
#### Due: 10-20-2020 (Tuesday @ 3:30 p.m.)

### Overview

A primality test is an algorithm for determining whether an input number is prime. Among other fields of mathematics, it is used for cryptography. Unlike integer factorization, primality tests do not generally give prime factors, only stating whether the input number is prime or not. Factorization is thought to be a computationally difficult problem, whereas primality testing is comparatively easy (its running time is polynomial in the size of the input). Some primality tests prove that a number is prime, while others like Miller–Rabin prove that a number is composite. Therefore, the latter might more accurately be called compositeness tests instead of primality tests. <sup>[[1]](#1)</sup>

Your assignment is to find tests in both categories (plus a third as mentioned by Dr. Mitchell). Those three categories are:

1. Certification
2. Compositeness 
3. Deterministic


### Certification

"A primality certificate or primality proof is a succinct, formal proof that a number is prime."<sup>[[1]](#1)</sup> This is a little beyond what we are wanting to do. Our goal is to find some algorithms that find primes in a "brute force" fashion that inherently guarantee the number found is prime. So to "certify" a number is prime, we are ok with using ***trial division***.  This is the simplest primality test there is. It goes something like this: 
>Given an input number, ***n***, check whether it is evenly divisible by any prime number between ***2*** and ***√n*** (i.e. that the division leaves no remainder). If so, then ***n*** is **composite**. Otherwise, it is ***prime***.

Of course this does not mean we are looking to waste time. We still want to do things efficiently. So we look for other, faster ways of determining primes as well. 

### Compositeness
A composite number is a positive integer that can be formed by multiplying two smaller positive integers. Equivalently, it is a positive integer that has at least one divisor other than 1 and itself. Every positive integer is composite, prime, or the unit 1, so the composite numbers are exactly the numbers that are not prime and not a unit <sup>[[4]](#4)</sup>. One test for compositeness is Rabin-Miller<sup>[[5]](#5)</sup>. Look at the wikipedia page for other tests for compositeness like: [Solovay–Strassen primality test](https://en.wikipedia.org/wiki/Primality_test)<sup>[[6]](#6)</sup>.


### Deterministic
A deterministic algorithm is an algorithm which, given a particular input, will always produce the same output, with the underlying machine always passing through the same sequence of states<sup>[[7]](#7)</sup>. There is one algorithm that claims to be deterministic, but I'm not sure how generalized this algorithm is. It can be found here: https://en.wikipedia.org/wiki/AKS_primality_test 



For an awesome summary of algorithms and other materials look here: [Finding primes & proving primality](https://primes.utm.edu/prove/index.html). It's a great summary of information dealing with primes.


### Requirements

Your assignment is to do a lit review of methods to find prime numbers in any and all of the above categories. There are plenty of algorithms to choose from, however, try and find algorithms other than obvious ones. That implies you need to dig a little bit and not turn in the the first / easily locatable algorithms when you start searching. You should list a minimum of 7 algorithms with short descriptions of each including the category in which they exist. You need to find at least 2 deterministic algorithms, and the other 5 can be in both of the other two categories. 

### Deliverables

- Create a folder called `A07` in assignments folder.
- Place your write-up in a README file inside A07 addressing the requirements. I won't put a word or page limit, however, your README should show and obvious effort digging for information other than the obvious.
- Follow the guidelines of [this](../../Resources/02-Readmees/README.md) to help you write a README.md for your assignment. I know that info is directed toward project with code, but at a minimum, you could look at the source to help with your markdown. 
- And just in case: https://guides.github.com/features/mastering-markdown/


#### References:

- <a id="1">[1]</a>: https://en.wikipedia.org/wiki/Primality_test
- <a id="2">[2]</a>: https://en.wikipedia.org/wiki/Primality_certificate
- <a id="3">[3]</a>: https://primes.utm.edu/prove/index.html
- <a id="4">[4]</a>: https://en.wikipedia.org/wiki/Composite_number
- <a id="5">[5]</a>: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
- <a id="6">[6]</a>:https://en.wikipedia.org/wiki/Primality_test
- <a id="7">[7]</a>:https://en.wikipedia.org/wiki/Deterministic_algorithm