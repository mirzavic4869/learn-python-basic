# Mengecek bilangan prima


def is_prima(x):
    if (x <= 1):
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False

    return True


print(is_prima(5))
