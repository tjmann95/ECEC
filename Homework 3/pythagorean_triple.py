# Generate each Pythagorean triple uniquely using Euclid's Augmented Formula.


from fractions import gcd


def py_triple(cmax):
    # 1. Construct an empty list to hold all the triples as they are found.
    pythagorean_triple = []

    # 2. Use range with two arguments so n ranges over the values [1, 2, ..., 10].
    for n in range(1,11):
        # 3. Now impose conditions 1 and 2. Use range with three arguments so m ranges over the values:
        #   [n + 1, n + 3, n + 5, ... , 10]   if n odd, or[n+1, n+3, n+5, ... , 9] if n even.
        for m in range(n+1, 11, 2):
            # 4. Let k range over the values [1, 2, ... , 20] - because the smallest c is 5.
            for k in range(1, 21):
                # 5. Now impose condition 3. Use gcd to test if m and n are coprime.
                if gcd(m,n) == 1:  # Test if m and n are coprime.
                    # 6-7. Complete this pythonic assignment using Euclid's three formulas.
                    a, b, c = k*(m*m - n*n), k*(2*m*n), k*(m*m + n*n)
                    triple = [a, b, c]  # Store the triple as a list.
                    # 8. Sort the triple so that a <= b <= c.
                    triple.sort()
                    if c <= cmax:    # Only take triples in the target range.
                        # 9. Append the list [a, b, c] to the list of triples.
                        pythagorean_triple.append( triple )
    return pythagorean_triple


triples = py_triple(300)
# 10. Print out the number of Pythagorean triples you found.
number_found = len(triples)
print "There are %d Pythagorean Triples (a, b, c) with c <= 100." % number_found
print triples
