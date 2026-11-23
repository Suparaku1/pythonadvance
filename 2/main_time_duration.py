import timeduration


def main():
    d1 = timeduration.Duration(1, 32, 45)
    d1.print()
    print(d1.get_seconds())
    print(d1.get_hours())

    t1 = timeduration.Time(10, 52, 30)
    t1.print()
    t1.add(d1)
    t1.print()


if __name__ == "__main__":
    main()
