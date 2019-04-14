################################
#     https://www.regular-expressions.info/creditcard.html
#  
################################

import re



def is_valid_creditcard(sequence):
    """Check if a sequence is a valid credit card number.
    Rules for sequences to qualify as credit card numbers:

    Sequences must:

    -Contain exactly 16 digits;
    -Start with a 4,5 or 6;
    -Only consist of digits (0-9).

    Sequences may:
    -Have digits in groups of 4, separated by one hyphen.

    Sequence must not:
    -Use any other separator;
    -Have 4 or more consecutive repeated digits.
    """
    PATTERN = "([4-6]{1})([0-9]{3}-?)([0-9]{4}-?){2}([0-9]{4})"
    for i, n in enumerate(sequence):
        try:
            if (sequence[i], 
                sequence[i+1], 
                sequence[i+2],
                sequence[i+3]
            ) == (n, n, n, n):
                return False
        except IndexError:
            pass
    return bool(re.match(PATTERN, sequence))



x = '4134-4182-4444-1429'
print(is_valid_creditcard(x))
