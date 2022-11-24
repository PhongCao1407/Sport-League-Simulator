from database.sport import Sport


if __name__ == "__main__":
    sports = Sport.objects.all()

    for sport in sports:
        print(sport)
