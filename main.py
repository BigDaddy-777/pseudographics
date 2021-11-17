import dictionary
dictionary = dictionary.dictionary


def pseudographics(word):
    output_matrix = [([" " * i]) for i in range(10)]  # [([])for i in range(10)]
    for i in word:
        if i not in dictionary:
            word = "ошибка"

    for key in word:
        wle_y = 0
        while wle_y < len(dictionary[key]):
            constr = ""

            wle_x = 0
            while wle_x < len(dictionary[key][wle_y]):
                add = "   "

                if wle_x == len(dictionary[key][wle_y])-1:
                    add = ""

                if dictionary[key][wle_y][wle_x] == "0":

                    if wle_x < len(dictionary[key][wle_y]) - 1:

                        if dictionary[key][wle_y][wle_x + 1] == "1":
                            add = " \\/"
                            if dictionary[key][wle_y - 1][wle_x + 1] == "0":
                                add = "  /"
                    if wle_y > 0:

                        if wle_x < len(dictionary[key][wle_y]) - 1:

                            if dictionary[key][wle_y - 1][wle_x + 1] == "1":
                                add = " \\/"

                        if dictionary[key][wle_y - 1][wle_x] == "1":
                            add = "// "

                            if "1" in dictionary[key][wle_y - 1][wle_x + 1]:
                                add = "///"

                if dictionary[key][wle_y][wle_x] == "1":
                    add = "\\\\\\"
                constr += add

                wle_x += 1

            output_matrix[wle_y].append(constr)
            wle_y += 1

    return output_matrix


if __name__ == '__main__':
    while True:
        word = input().lower()
        matrix = pseudographics(word)
        for i in matrix:
            print(*i)
