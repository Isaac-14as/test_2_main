class Matrix():
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list


    def print_m(self):
        answer = ''
        for i in range(len(self.matrix_list)):
            answer += '|' + '\t'
            for j in range(len(self.matrix_list[i])):
                answer += str(self.matrix_list[i][j]) + '\t'
            answer = answer[:-1:]
            answer += '\t' + '|'
            answer += '\n'
        return answer


    def transposition(self):
        answer = [[self.matrix_list[j][i] for j in range(len(self.matrix_list))] for i in range(len(self.matrix_list[0]))]
        return Matrix(answer)
    

    def __sub__(self, another_matrix):
        answer = []
        for i in range(len(self.matrix_list)):
            a = []
            for j in range(len(self.matrix_list[0])):
                another_list = getattr(another_matrix, 'matrix_list')[i][j]
                a.append(self.matrix_list[i][j] - another_list)
            answer.append(a)
        return Matrix(answer)
    

    def __add__(self, another_matrix):
        answer = []
        for i in range(len(self.matrix_list)):
            a = []
            for j in range(len(self.matrix_list[0])):
                another_list = getattr(another_matrix, 'matrix_list')[i][j]
                a.append(self.matrix_list[i][j] + another_list)
            answer.append(a)
        return Matrix(answer)
    

    def __mul__(self, another_matrix):
        answer = []
        for i in range(len(self.matrix_list)):
            sub_answer = []
            for j in range(len(getattr(another_matrix, 'matrix_list')[0])):
                c = 0
                for r in range(len(getattr(another_matrix, 'matrix_list'))):
                    c += self.matrix_list[i][r] * getattr(another_matrix, 'matrix_list')[r][j]
                sub_answer.append(c)
            answer.append(sub_answer)
        return Matrix(answer)


    def __truediv__(self, divisor):
        answer = self.matrix_list
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[0])):
                answer[i][j] = answer[i][j] / divisor
        return Matrix(answer)  