class Calc:
    def get_gom(self, num1, num2):
        return num1 * num2

    def get_minus(self, num1, num2):
        return num1 - num2

    def get_divided_value(self, n1, n2):
        if n2 == 0:
            return None

        return n1 / n2
      
    def get_zegop(self, num):
        return num ** 2

    def getSumSum(self, num01, num02, num03):
        return num01 + num02 + num03