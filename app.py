def my_trib(n):
    n2 = n3 = 0
    n1 = 1
    nums = []
    for i in range(n):
        n1, n2, n3 = n3+n1, n2+n1, n2+n3
        nums.append(str(n1))
    return " ".join(nums)


def app():
    res = my_trib(10)
    print(res)


if __name__ == "__main__":
    app()
