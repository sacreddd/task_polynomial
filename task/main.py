import time
from datetime import timedelta


def main():
    max_degree = int(input())
    coefs = [int(input()) for i in range(max_degree + 1)]

    start_time = time.monotonic()
    print("------start------")
    final_string = ""
    count = 0
    for coef in coefs:
        if coef != 0:
            coef_module = abs(coef)
            if coef < 0:
                final_string += " - "
            elif final_string != "":
                final_string += " + "
            if coef_module != 1 or (max_degree - count) == 0:
                final_string += str(coef_module)
            if(max_degree - count) >= 1:
                if coef_module != 1:
                    final_string += " * "
                final_string += "x"
                if (max_degree - count) > 1:
                    final_string += "^" + str(max_degree - count)
        count += 1

    if final_string == "":
        print("0")
    else:
        print(final_string)

    end_time = time.monotonic()
    print(timedelta(seconds=end_time - start_time))


if __name__ == "__main__":
    main()
