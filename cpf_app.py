from random import randint

class CpfApp():
    def __init__(self, cpf = None):

        if cpf:
            self.cpf = cpf
        else:
            self.generate_cpf()

        self.cpf_formatted = CpfApp.get_formatted_cpf(self.cpf)

    def generate_cpf(self):
        counter = 1

        cpf = ''

        while counter <= 9:
            cpf += str(randint(0,9))

            counter += 1

        cpf = CpfApp.generate_cpf_first_digit(cpf)
        cpf = CpfApp.generate_cpf_second_digit(cpf)

        self.cpf = CpfApp.get_formatted_cpf(cpf)

    @staticmethod
    def generate_cpf_first_digit(cpf):

        sum_result = 0

        counter = 10

        for num in cpf:
            sum_result += int(num) * counter
            counter -= 1

        result = 11 - (sum_result % 11)

        if result > 9:
            cpf += '0'
            return cpf
        else:
            cpf += str(result)
            return cpf

    @staticmethod
    def generate_cpf_second_digit(cpf):
        sum_result = 0

        counter = 11

        for num in cpf:
            sum_result += int(num) * counter

            counter -= 1

        result = 11 - (sum_result % 11)

        if result > 9:
            cpf += '0'
            return cpf
        else:
            cpf += str(result)
            return cpf

    @staticmethod
    def validate_cpf(cpf):
        cpf = cpf.replace('.','')
        cpf = cpf.replace('-','')

        validation_first_digit = CpfApp.verify_first_digit(cpf)
        validation_second_digit = CpfApp.verify_second_digit(cpf)

        if CpfApp.verify_sequence(cpf):
            return False

        if validation_first_digit and validation_second_digit:
            return True
        else:
            return False

    @staticmethod
    def verify_sequence(cpf):
        sequence = True

        for number in cpf:
            if number != cpf[0]:
                sequence = False

        if sequence == True:
            return True
        else:
            return False
    
    @staticmethod
    def verify_first_digit(cpf):

        digit = cpf[-2]
        cpf = cpf[:-2]

        correct_digit = CpfApp.generate_cpf_first_digit(cpf)[-1]

        if str(correct_digit) == digit:
            return True
        else:
            return False 

    @staticmethod
    def verify_second_digit(cpf):
        digit = cpf[-1]
        cpf = cpf[:-1]

        correct_digit = CpfApp.generate_cpf_second_digit(cpf)[-1]

        if str(correct_digit) == digit:
            return True
        else:
            return False 

    @staticmethod
    def get_formatted_cpf(cpf):

        position = 0

        cpf_mask = 'xxx.xxx.xxx-xx'

        result = ''

        for num in cpf_mask:
            if num != '-' and num !='.':
                result += cpf[position]
                position += 1
            else:
                result += num

        return result