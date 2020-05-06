def sqrt(x):
    """Compute the sqrt using the method of Heron of Alexandria."""
    if x < 0:
        raise ValueError(f"Cannot compute sqrt of negative number {x}")
    guess = x
    i = 0
    while guess * guess !=x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess