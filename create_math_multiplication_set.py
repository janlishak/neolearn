if __name__ == '__main__':
    with open("learning-sets/math-multiplication.txt", "w") as file:
        for a in range(1,10):
            for b in range(1, 10):
                file.write(f'{a}*{b}, {a*b}\n')