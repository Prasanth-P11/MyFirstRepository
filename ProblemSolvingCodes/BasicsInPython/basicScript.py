def seperate_data_type(a):
    b = []
    c = []
    for i in a:
        d = str(i)
        if d.isdigit():
            b.append(int(i))
        else:
            c.append(str(i))
    print(b)
    print(c)


if __name__ == "__main__":
    a = [1, 2, "hi", "how"]
    seperate_data_type(a)