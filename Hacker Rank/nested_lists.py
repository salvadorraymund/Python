if __name__ == "__main__":
    marksheet = []
    n = 5
    name = ["Harry", "Berry", "Cherry", "Rocky", "Cory"]
    score = [38, 39, 29, 20, 40]
    marksheet = [[name[i], score[i]] for i in range(n)]
    print(marksheet)
    second_highest = sorted(list(set([score for name, score in marksheet])))[1]
    highest = sorted(list(set([score for name, score in marksheet])))[-1]
    print('\n'.join([x for x, y in sorted(marksheet) if y == highest]))
    print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))
