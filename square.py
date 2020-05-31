filler_letter = "X"


class Square:
    """
    Square : a dictionary containing all the letters as keys, and the
    """

    def __init__(self, tab=None):
        """
        :type tab: dict
        """
        self._tableau = tab
        self.verifier_tableau()

    def print_tableau(self):
        iterator = 1
        final_list = ["" for i in range(25)]
        for letter in self._tableau.keys():
            final_list[self._tableau.get(letter) - 1] = letter

        for letter in final_list:
            if iterator % 5 != 0:
                print(letter, end=' ')
            else:
                print(letter)
            iterator += 1

    def get_tableau(self):
        return self._tableau

    def verifier_tableau(self):
        """
        True signifie que le tableau est nom
        False : le tableau est incorect
        :return:
        """
        tab_alphabet = dict(A=1, B=2, C=3, D=4, E=5,
                            F=6, G=7, H=8, I=9, J=10,
                            K=11, L=12, M=13, N=14, O=15,
                            P=16, Q=17, R=18, S=19, T=20,
                            U=21, V=22, X=23, Y=24, Z=25)
        if len(self._tableau) != 25:
            raise Exception("input tab not in the good length! Length : " + len(self._tableau))
        for letter in tab_alphabet.keys():
            if letter not in self._tableau:
                raise Exception("input tab (" +
                                str(self._tableau.keys()) +
                                ") given is not correct!\n"
                                "You need these keys : " +
                                str(tab_alphabet.keys()))
        tab_values = list(self._tableau.values())
        tab_values.sort()
        if tab_values != list(range(1, 26)):
            raise Exception("Values entered are not good!\n" + "values entered sorted : \n" + tab_values.__str__())
        return True

    def get_letter(self, index):
        if index <= 0 or index > 25:
            print("Error with the process of index " + index.__str__())
            return "*ERROR*"
        for letter in self._tableau.keys():
            if self._tableau.get(letter) == index:
                return letter

    def encrypt_letters(self, letter1, letter2):
        if letter1 == "W":
            letter1 = "V"
        if letter2 == "W":
            letter2 = "V"
        if letter1 not in self._tableau or letter2 not in self._tableau:
            raise Exception("Input letter : " +
                            str(letter1) +
                            " and " +
                            str(letter2) +
                            " are not accepted")

        # rows and columns numbers to know if some letters are aligned
        row_letter_1 = (self._tableau.get(letter1) - 1) // 5
        row_letter_2 = (self._tableau.get(letter2) - 1) // 5
        column_letter_1 = (self._tableau.get(letter1) - 1) % 5
        column_letter_2 = (self._tableau.get(letter2) - 1) % 5

        i1 = self._tableau.get(letter1) // 5
        j1 = self._tableau.get(letter1) % 5
        i2 = self._tableau.get(letter2) // 5
        j2 = self._tableau.get(letter2) % 5

        # print(lettre_1, i1, j1)
        # print(lettre_2, i2, j2)

        out_letter1 = ""
        out_letter2 = ""

        if letter1 == letter2:
            return letter1 + filler_letter + letter2
        elif row_letter_1 == row_letter_2:  # Letters are on the same row
            if j1 == 0:
                i1 -= 1
            if j2 == 0:
                i2 -= 1
            out_letter1 = self.get_letter(i1 * 5 + j1 + 1)
            out_letter2 = self.get_letter(i2 * 5 + j2 + 1)
        elif column_letter_1 == column_letter_2:  # Letters are on the same column
            if (i1 == 4 and j1 > 0) or i1 == 5:  # if letter == U -> Y or letter == Z
                i1 -= 5
            if (i2 == 4 and j2 > 0) or i2 == 5:  # if letter == U -> Y or letter == Z
                i2 -= 5
            out_letter1 = self.get_letter((i1 + 1) * 5 + j1)
            out_letter2 = self.get_letter((i2 + 1) * 5 + j2)
        else:
            if j1 == 0:
                out_letter1 = self.get_letter(i1 * 5 + j2 - 5)
                out_letter2 = self.get_letter(i2 * 5 + j1 + 5)
            elif j2 == 0:
                out_letter1 = self.get_letter(i1 * 5 + j2 + 5)
                out_letter2 = self.get_letter(i2 * 5 + j1 - 5)
            else:
                out_letter1 = self.get_letter(i1 * 5 + j2)
                out_letter2 = self.get_letter(i2 * 5 + j1)

        return out_letter1 + out_letter2

    def encrypt_text(self, text, filler_letter=filler_letter):
        assert (len(text) > 0)
        first_letter_iter = 0
        final_text = ''
        while first_letter_iter < len(text):
            if first_letter_iter + 1 == len(text):  # Case when len(text) is odd
                final_text += text[first_letter_iter]
                first_letter_iter += 2
                continue
            first_letter = text[first_letter_iter]
            second_letter = text[first_letter_iter + 1]
            final_text += self.encrypt_letters(first_letter, second_letter)
            first_letter_iter += 2
        return final_text

    def decrypt_letters(self, letter1, letter2):
        if letter1 not in self._tableau or letter2 not in self._tableau:
            raise Exception("Input letter : " +
                            str(letter1) +
                            " and " +
                            str(letter2) +
                            " are not accepted")

        row_letter_1 = (self._tableau.get(letter1) - 1) // 5
        row_letter_2 = (self._tableau.get(letter2) - 1) // 5
        column_letter_1 = (self._tableau.get(letter1) - 1) % 5
        column_letter_2 = (self._tableau.get(letter2) - 1) % 5

        i1 = self._tableau.get(letter1) // 5
        j1 = self._tableau.get(letter1) % 5
        i2 = self._tableau.get(letter2) // 5
        j2 = self._tableau.get(letter2) % 5

        if letter1 == letter2:  # This should not happen
            raise Exception("There are two identical letters joined in the text! \nHere is the letter : " + letter1)
        elif row_letter_1 == row_letter_2:  # Letters are on the same row
            if j1 == 1:
                i1 += 1
            if j2 == 1:
                i2 += 1
            out_letter1 = self.get_letter(i1 * 5 + j1 - 1)
            out_letter2 = self.get_letter(i2 * 5 + j2 - 1)
        elif column_letter_1 == column_letter_2:  # Letters are on the same column
            if i1 == 0 or (i1 == 1 and j1 == 0):  # if letter == A -> D or letter == E
                i1 += 5
            if i2 == 0 or (i2 == 1 and j2 == 0):  # if letter == A -> D or letter == E
                i2 += 5
            out_letter1 = self.get_letter((i1 - 1) * 5 + j1)
            out_letter2 = self.get_letter((i2 - 1) * 5 + j2)
        else:
            if j1 == 0:
                out_letter1 = self.get_letter(i1 * 5 + j2 - 5)
                out_letter2 = self.get_letter(i2 * 5 + j1 + 5)
            elif j2 == 0:
                out_letter1 = self.get_letter(i1 * 5 + j2 + 5)
                out_letter2 = self.get_letter(i2 * 5 + j1 - 5)
            else:
                out_letter1 = self.get_letter(i1 * 5 + j2)
                out_letter2 = self.get_letter(i2 * 5 + j1)

        return out_letter1 + out_letter2

    def decrypt_text(self, text, filler_letter=filler_letter):
        assert (len(text) > 0)
        first_letter_iter = 0
        final_text = ''
        while first_letter_iter < len(text):
            if first_letter_iter + 1 == len(text):  # Case when len(text) is odd
                final_text += text[first_letter_iter]
                first_letter_iter += 2
                continue
            first_letter = text[first_letter_iter]
            second_letter = text[first_letter_iter + 1]
            final_text += self.decrypt_letters(first_letter, second_letter)
            first_letter_iter += 2
        return final_text
