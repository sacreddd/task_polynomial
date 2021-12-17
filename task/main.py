import time
from datetime import timedelta
max_degree = int(input())
coefs = [int(input()) for i in range(max_degree + 1)]


start_time = time.monotonic()



def main():
    print("------start------")
    final_string = ""
    count = 0
    for coef in coefs:
        if coef > 0:
            if final_string == "":
                if coef != 1:
                    final_string += str(coef) + degree_counter(max_degree, count, True)
                else:
                    final_string += degree_counter(max_degree, count, False)
            else:
                if coef != 1:
                    final_string += " + " + str(coef) + degree_counter(max_degree, count, True)
                else:
                    if max_degree - count == 0:
                        final_string += " + " + str(coef) + degree_counter(max_degree, count, False)
                    else:
                        final_string += " + " + degree_counter(max_degree, count, False)
        elif coef < 0:
            if coef != -1:
                final_string += " - " + str(abs(coef)) + degree_counter(max_degree, count, True)
            else:
                final_string += " - " + degree_counter(max_degree, count, False)
        count += 1

    if final_string == "":
        print("0")
    else:
        print(final_string)


def degree_counter(degree, cnt, condition: bool) -> str:
    if degree - cnt == 0:
        return ""
    if condition:
        if degree - cnt == 1:
            return " * x"
        else:
            return " * x^" + str(degree - cnt)
    else:
        if degree - cnt == 1:
            return "x"
        else:
            return "x^" + str(degree - cnt)


if __name__ == "__main__":
    main()

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
