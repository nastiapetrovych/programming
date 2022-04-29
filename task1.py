"""
The third task
"""
# 64 Петрович Анастасія ['>=', '=='] ['*', '**'] ['<<', '>>']

VARIANT = 64


class Node:
    """
    Creates the linked list
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class BigInteger:
    """
    Makes function work properly
    """

    def __init__(self, initValue="0"):
        self.item = initValue
        self.head = None
        self.negative = None
        self.str_value = initValue
        self.binary = False

        if not isinstance(self.item, str):
            self.item = str(self.item)
        if self.item.startswith('-'):
            self.item = self.item[1:]
            self.negative = True
        for character in self.item:
            self.add_node(character)

    def add_node(self, value):
        """
        Adds node to a list
        """
        point = Node(value)
        if self.head is None:
            self.head = point
            return
        current = self.head
        while True:
            if current.next is None:
                current.next = point
                break
            current = current.next

    def to_string(self):
        """
        Returns the image of integer
        """
        return str(self)

    def __eq__(self, other):
        """
        Compare if two each number in node is equal
        """
        indicator = True
        lst1 = []
        lst2 = []
        while self.head is not None:
            lst1.append(self.head.value)
            self.head = self.head.next
        while other.head is not None:
            lst2.append(other.head.value)
            other.head = other.head.next

        if len(lst1) == len(lst2) and self.negative == other.negative:
            for inx in range(len(lst1)):
                indicator = (lst1[inx] == lst2[inx])
                if not indicator:
                    break
        else:
            return False
        return True if indicator else False

    def __ge__(self, other):
        """
        Compares if each number in node is equal or bigger than another
        """
        indicator = True
        lst1 = []
        lst2 = []
        while self.head is not None:
            lst1.append(self.head.value)
            self.head = self.head.next
        while other.head is not None:
            lst2.append(other.head.value)
            other.head = other.head.next
        sign = True
        if self.negative and other.negative:
            sign = False
        elif not self.negative and other.negative:
            return True
        elif self.negative and not other.negative:
            return False

        if len(lst1) > len(lst2):
            return sign
        elif len(lst1) == len(lst2):
            for inx in range(len(lst1)):
                indicator = (lst1[inx] >= lst2[inx])
                break
            return True if indicator else False
        return False

    def __mul__(self, other):
        """
        Multiply the given numbers
        """
        val = int(self.item)
        times = int(other.item)
        result = 0
        for _ in range(times):
            result += val
        if self.negative and other.negative:
            return BigInteger(str(result))
        if self.negative or other.negative:
            result = '-' + str(result)
            return BigInteger(result)
        else:
            return BigInteger(str(result))

    def __str__(self):
        """
        Returns the value
        """
        return str(self.str_value)

    def __pow__(self, power):
        """
        The raising of number to some power
        """
        element = int(self.item)
        power_value = int(power.item)
        if element == 0 and power_value == 0:
            return BigInteger('0')
        negative = self.negative
        result = 1
        for _ in range(power_value):
            result *= element
        if negative:
            if power_value % 2 == 0:
                negative = False
        if power.negative:
            result = 1 / result
        return BigInteger(str(result)) if not negative else BigInteger(f'-{str(result)}')

    def to_binary(self):
        bin_number = bin(int(self.item))[2:]
        self.binary = True
        return BigInteger(bin_number)

    def __rshift__(self, other):
        """
        Equal to number * (2**another number)
        """
        bin_number = self.item
        if not self.binary:
            bin_number = self.to_binary().item
            self.binary = True
        power = int(other.item)
        negative = self.negative
        for _ in range(power):
            bin_number = bin_number[:-1]
        final = str(bin_number)
        return BigInteger('-' + final) if negative else BigInteger(final)

    def __add__(self, other):
        """
        Adds two numbers
        """
        lst1 = []
        lst2 = []
        while self.head is not None:
            lst1.append(self.head.value)
            self.head = self.head.next
        while other.head is not None:
            lst2.append(other.head.value)
            other.head = other.head.next
        final = ''
        extra = 0
        lst1 = lst1[::-1]
        lst2 = lst2[::-1]
        while len(lst1) != len(lst2):
            if len(lst1) > len(lst2):
                lst2.append('0')
            else:
                lst1.append('0')
        for x_el, y_el in zip(lst1, lst2):
            result = int(x_el) + int(y_el)
            final += str((result % 10) + extra)
            extra = result // 10
        return BigInteger(final[::-1])

    def __lshift__(self, other):
        """
        Equals to number % (2 ** another number)
        """
        bin_number = self.item
        if not self.binary:
            bin_number = self.to_binary().item
            self.binary = True
        power = int(other.item)
        negative = self.negative
        for _ in range(power):
            bin_number += '0'
        final = str(bin_number)
        return BigInteger('-' + final) if negative else BigInteger(final)
