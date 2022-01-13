from random import randint

class CpfGeneratorValidator():
    def __init__(self, cpf = None):

        self.cpf_mask = 'xxx.xxx.xxx-xx'

        if cpf:
            self.cpf = cpf
        else:
            self.cpf = ''

        self.cpf_formatted = ''

    def generate_cpf(self):
        counter = 1

        while counter <= 9:
            self.cpf += str(randint(0,9))

            counter += 1

        self.generate_cpf_first_digit()

        self.generate_cpf_second_digit()

    def generate_cpf_first_digit(self):

        sum_result = 0

        counter = 10

        for num in self.cpf:
            sum_result += int(num) * counter
            counter -= 1

        result = 11 - (sum_result % 11)

        if result > 9:
            self.cpf += '0'
        else:
            self.cpf += str(result)

    def generate_cpf_second_digit(self):
        sum_result = 0

        counter = 11

        for num in self.cpf:
            sum_result += int(num) * counter

            counter -= 1

        result = 11 - (sum_result % 11)

        if result > 9:
            self.cpf += '0'
        else:
            self.cpf += str(result)

    def validate_cpf(self):
        pass

    def print_cpf(self):
        position = 0

        result = ''

        for num in self.cpf_mask:
            if num != '-' and num !='.':
                result += self.cpf[position]
                position += 1
            else:
                result += num

        self.cpf_formatted = result

        print(result)