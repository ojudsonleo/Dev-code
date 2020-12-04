import os
import sys
import time
import random
import turtle
import numpy as np


class Joel(object):
    def __init__(self):
        self.os = os.uname().sysname
        self.user = os.getlogin()
        self.id = id(Joel)
        self.name = "Joel"
        self.adult = 20
        self.teenager = 13
        self.child = 12

    def __repr__(self):
        return f"{self.name}()"

    def is_adult(self, age):
        if age >= self.adult:
            print("True you are a adult")
            return True

        else:
            print("False you are not a adult")
            return False

    def is_child(self, age):

        if age <= self.child:
            print("True you are a child")
            return True

        else:
            print("False you are not a child")
            return False

    def is_teenager(self, age):

        if age >= self.teenager:
            print("True you are a teenager")
            return True

        else:
            print("False you are not a teenager")
            return False

    class Os(object):
        class MakeADir(object):
            def __init__(self, DirName):
                self.DirName = DirName
                self.name = "MakeADir"

                os.makedirs(self.DirName)

            def __repr__(self):
                return f"{self.name}()"

        class RemoveADir(object):
            def __init__(self, DirName):
                self.DirName = DirName
                self.name = "RemoveADir"

                try:
                    os.removedirs(self.DirName)
                except Exception as err:
                    print(err)

            def __repr__(self):
                return f"{self.name}()"

        class RenameAFileOrADir(object):
            def __init__(self, FileName, RenameTo):
                self.name = "RenameAFileOrADir"
                self.FileName = FileName
                self.RenameTo = RenameTo

                try:
                    os.rename(self.FileName, self.RenameTo)
                except Exception as err:
                    print(err)

            def __repr__(self):
                return f"{self.name}()"

        class ListItems(object):
            def __init__(self):
                self.name = "ListItems"
                self.lister = os.listdir()

                for i in self.lister:
                    print(i)

        class EditAFile(object):
            def __init__(self, FileName, word):
                self.FileName = FileName
                self.word = word
                self.name = "EditAFile"

                self.process(self.FileName, self.word)

            def __repr__(self):
                return f"{self.name}()"

            @staticmethod
            def process(f, w):
                with open(f, "w") as file:
                    file.write(w)

            class Find_The_Size_IN_Bytes(object):
                def __init__(self, function):
                    self.name = "Find_The_Size_IN_Bytes"
                    self.func = function

                def __repr__(self):
                    return f"{self.name}()"

                def process(self):
                    sys.getsizeof(self.func)

    class Book(object):
        def __init__(self, bookName, numberOfPages):
            self.bookName = bookName
            self.numberOfPages = numberOfPages
            self.name = "Book"

        def __repr__(self):
            return f"{self.name}()"

    class House(object):
        def __init__(self):
            self.name = "House"
            self.HouseName = ""
            self.NumberOfMemberInTheHouse = 0
            self.NumberOfFanInTheHouse = 0

        def __repr__(self):
            return f"{self.name}()"

    class RandomPassWord(object):

        def __init__(self):
            self.name = "RandomPassWord"
            self.Random()

        def __repr__(self):
            return f"{self.Random()})"

        @staticmethod
        def generateRandomString():
            A = "A"
            B = "B"
            C = "C"
            D = "D"
            E = "E"
            F = "F"
            G = "G"
            H = "H"
            I = "I"
            J = "J"
            K = "K"
            L = "L"
            M = "M"
            N = "N"
            O = "O"
            P = "P"
            Q = "Q"
            R = "R"
            S = "S"
            T = "T"
            U = "U"
            V = "V"
            W = "W"
            X = "X"
            Y = "Y"
            Z = "Z"

            a = "a"
            b = "b"
            c = "c"
            d = "d"
            e = "e"
            f = "f"
            g = "g"
            h = "h"
            i = "i"
            j = "j"
            k = "k"
            l = "l"
            m = "m"
            n = "n"
            o = "o"
            pp = "p"
            q = "q"
            r = "r"
            s = "s"
            t = "t"
            u = "u"
            v = "v"
            w = "w"
            x = "x"
            y = "y"
            z = "z"

            CAPS = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
            small = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, pp, q, r, s, t, u, v, w, x, y, z]
            result = ""
            CC = ""
            SS = ""
            WW = random.randint(0, 1)

            for xx in range(4):
                num1 = random.randint(0, len(small) - 1)
                num2 = random.randint(0, len(CAPS) - 1)
                CC = CC + CAPS[num2]
                SS = SS + small[num1]
            if WW == 0:
                result = result + CC
                result = result + SS
            elif WW == 1:
                result = result + SS
                result = result + CC

            return result

        @staticmethod
        def generateRandomInt():
            n0 = 0
            n1 = 1
            n2 = 2
            n3 = 3
            n4 = 4
            n5 = 5
            n6 = 6
            n7 = 7
            n8 = 8
            n9 = 9
            nNumber = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
            result = ""

            for NN in range(4):
                ranNum = random.randint(0, len(nNumber) - 1)
                result = f"{result + str(nNumber[ranNum])}"

            return result

        @staticmethod
        def generateRandomSymbol():
            s1 = '!'
            s2 = '@'
            s3 = '#'
            s4 = '$'
            s5 = '%'
            s6 = '^'
            s7 = '&'
            s8 = '*'
            s9 = '('
            s0 = ')'
            s10 = '~'
            s11 = '?'
            result = ''

            numSymbol = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]
            for SS in range(4):
                ranSymbol = random.randint(0, len(numSymbol) - 1)
                result = result + numSymbol[ranSymbol]

            return result

        def Random(self):
            ran = [self.generateRandomString(), self.generateRandomInt()]
            ranResult = ""
            ranSN = random.randint(0, 1)
            if ranSN == 0:
                ranResult = ranResult + ran[ranSN] + ran[ranSN + 1]

            else:
                ranResult = ranResult + ran[ranSN] + ran[ranSN + -1]

            result = ranResult + self.generateRandomSymbol()

            return result

    class Animals(object):

        def __init__(self):
            self.name = "Animals"

        def __repr__(self):
            return f"{self.name}()"

        class Dog(object):
            def __init__(self, nameOfDog, age):
                self.nameOfDog = nameOfDog
                self.age = age
                self.name = "Dog"

            def __repr__(self):
                return f"{self.name}()"

            def info(self):
                self.speak()

            def speak(self):
                print(f"My name is {self.nameOfDog} and my age is {self.age}")

            def change_name(self, name):
                self.nameOfDog = name

            def change_age(self, age):
                self.age = age

        class Cat(object):
            def __init__(self, nameOfCat, age):
                self.nameOfCat = nameOfCat
                self.age = age
                self.name = "Cat"

            def __repr__(self):
                return f"{self.name}()"

            def info(self):
                self.speak()

            def speak(self):
                print(f"My name is {self.nameOfCat} and my age is {self.age}")

            def change_name(self, name):
                self.nameOfCat = name

            def change_age(self, age):
                self.age = age

        class Lion(object):
            def __init__(self, nameOfLion, age):
                self.nameOfCat = nameOfLion
                self.age = age
                self.name = "Lion"

            def __repr__(self):
                return f"{self.name}()"

            def info(self):
                self.speak()

            def speak(self):
                print(f"My name is {self.nameOfCat} and my age is {self.age}")

            def change_name(self, name):
                self.nameOfCat = name

            def change_age(self, age):
                self.age = age

        class Tiger(object):
            def __init__(self, nameOfTiger, age):
                self.nameOfCat = nameOfTiger
                self.age = age
                self.name = "Tiger"

            def __repr__(self):
                return f"{self.name}()"

            def info(self):
                self.speak()

            def speak(self):
                print(f"My name is {self.nameOfCat} and my age is {self.age}")

            def change_name(self, name):
                self.nameOfCat = name

            def change_age(self, age):
                self.age = age

        class Cow(object):
            def __init__(self, nameOfCow, age):
                self.nameOfCat = nameOfCow
                self.age = age
                self.name = "Cow"

            def __repr__(self):
                return f"{self.name}()"

            def info(self):
                self.speak()

            def speak(self):
                print(f"My name is {self.nameOfCat} and my age is {self.age}")

            def change_name(self, name):
                self.nameOfCat = name

            def change_age(self, age):
                self.age = age

        class Rat(object):
            def __init__(self, nameOfRat, age):
                self.nameOfCat = nameOfRat
                self.age = age
                self.name = "Rat"

            def __repr__(self):
                return f"{self.name}()"

            def info(self):
                self.speak()

            def speak(self):
                print(f"My name is {self.nameOfCat} and my age is {self.age}")

            def change_name(self, name):
                self.nameOfCat = name

            def change_age(self, age):
                self.age = age

        class Rabbit(object):
            def __init__(self, nameOfRabbit, age):
                self.nameOfCat = nameOfRabbit
                self.age = age
                self.name = "Cat"

            def __repr__(self):
                return f"{self.name}()"

            def info(self):
                self.speak()

            def speak(self):
                print(f"My name is {self.nameOfCat} and my age is {self.age}")

            def change_name(self, name):
                self.nameOfCat = name

            def change_age(self, age):
                self.age = age

        class Goat(object):
            def __init__(self, nameOfGoat, age):
                self.nameOfCat = nameOfGoat
                self.age = age
                self.name = "Goat"

            def __repr__(self):
                return f"{self.name}()"

            def info(self):
                self.speak()

            def speak(self):
                print(f"My name is {self.nameOfCat} and my age is {self.age}")

            def change_name(self, name):
                self.nameOfCat = name

            def change_age(self, age):
                self.age = age

        class Math(object):
            def __init__(self):
                self.name = "Math"

            def __repr__(self):
                return f"{self.name}()"

            @staticmethod
            def Sub(value1, value2):
                print(value1 - value2)

            @staticmethod
            def Add(value1, value2):
                print(value1 + value2)

            @staticmethod
            def Mut(value1, value2):
                print(value1 * value2)

            @staticmethod
            def Div(value1, value2):
                print(value1 / value2)

            class NumberToRupees(object):
                def __init__(self, Number):
                    self.number = Number
                    self.name = "NumberToRupees"
                    self.process(self.number)

                def __repr__(self):
                    return f"{self.name}()"

                @staticmethod
                def process(number):
                    print(f"{number} Rs")

            class Convert(object):
                def __init__(self):
                    self.name = "Convert"

                def __repr__(self):
                    return f"{self.name}()"

                class MeterToCm(object):
                    def __init__(self, Number):
                        self.ans = ""
                        self.Number = Number
                        self.name = "MeterToCm"
                        self.process(self.Number)

                    def __repr__(self):
                        return f"{self.name}()"

                    def process(self, value):
                        self.ans = value * 100

                class MeterToKm(object):
                    def __init__(self, Number):
                        self.Number = Number
                        self.ans = ""
                        self.name = "MeterToKm"
                        print(self.Number)

                    def __repr__(self):
                        return f"{self.name}()"

                    def process(self, value):
                        self.ans = value / 1000

                class KmToMeter(object):
                    def __init__(self, Number):
                        self.Number = Number
                        self.name = "KmToMeter"
                        self.ans = ""
                        self.process(self.Number)

                    def __repr__(self):
                        return f"{self.name}()"

                    def process(self, value):
                        self.ans = value / 1000

        class NumberToRomanNumber1To100(object):
            def __init__(self, number):
                self.number = number
                self.name = "NumberToRomanNumber1To100"
                self.ans = ""

                self.n1 = "I"
                self.n2 = "II"
                self.n3 = "III"
                self.n4 = "IV"
                self.n5 = "V"
                self.n6 = "VI"
                self.n7 = "VII"
                self.n8 = "VIII"
                self.n9 = "IX"
                self.n10 = "X"

                self.n11 = "XI"
                self.n12 = "XII"
                self.n13 = "XIII"
                self.n14 = "XIV"
                self.n15 = "XV"
                self.n16 = "XVI"
                self.n17 = "XVII"
                self.n18 = "XVIII"
                self.n19 = "XIX"
                self.n20 = "XX"

                self.n21 = "XXI"
                self.n22 = "XXII"
                self.n23 = "XXIII"
                self.n24 = "XXIV"
                self.n25 = "XXV"
                self.n26 = "XXVI"
                self.n27 = "XXVII"
                self.n28 = "XXVIII"
                self.n29 = "XXIX"
                self.n30 = "XXX"

                self.n31 = "XXXI"
                self.n32 = "XXXII"
                self.n33 = "XXXIII"
                self.n34 = "XXXIV"
                self.n35 = "XXXV"
                self.n36 = "XXXVI"
                self.n37 = "XXXVII"
                self.n38 = "XXXVIII"
                self.n39 = "XXXIX"
                self.n40 = "XL"

                self.n41 = "XLI"
                self.n42 = "XLII"
                self.n43 = "XLIII"
                self.n44 = "XLIV"
                self.n45 = "XLV"
                self.n46 = "XLVI"
                self.n47 = "XLVII"
                self.n48 = "XLVIII"
                self.n49 = "XLIX"
                self.n50 = "L"

                self.n51 = "LI"
                self.n52 = "LII"
                self.n53 = "LIII"
                self.n54 = "LIV"
                self.n55 = "LV"
                self.n56 = "LVI"
                self.n57 = "LVII"
                self.n58 = "LVIII"
                self.n59 = "LIX"
                self.n60 = "LX"

                self.n61 = "LXI"
                self.n62 = "LXII"
                self.n63 = "LXIII"
                self.n64 = "LXIV"
                self.n65 = "LXV"
                self.n66 = "LXVI"
                self.n67 = "LXVII"
                self.n68 = "LXVIII"
                self.n69 = "LXIX"
                self.n70 = "LXX"

                self.n71 = "LXXI"
                self.n72 = "LXXII"
                self.n73 = "LXXIII"
                self.n74 = "LXXIV"
                self.n75 = "LXXXV"
                self.n76 = "LXXVI"
                self.n77 = "LXXVII"
                self.n78 = "LXXVII"
                self.n79 = "LXXIX"
                self.n80 = "LXXX"

                self.n81 = "LXXXI"
                self.n82 = "LXXXII"
                self.n83 = "LXXXIII"
                self.n84 = "LXXXIV"
                self.n85 = "LXXXV"
                self.n86 = "LXXXVI"
                self.n87 = "LXXXVII"
                self.n88 = "LXXXVII"
                self.n89 = "LXXXIX"
                self.n90 = "XC"

                self.n91 = "XCI"
                self.n92 = "XCII"
                self.n93 = "XCIII"
                self.n94 = "XCIV"
                self.n95 = "XCV"
                self.n96 = "XCVI"
                self.n97 = "XCVII"
                self.n98 = "XCVII"
                self.n99 = "XCIX"
                self.n100 = "C"

                self.LIST = [
                    self.n1, self.n2, self.n3, self.n4, self.n5,
                    self.n6, self.n7, self.n8, self.n9, self.n10,

                    self.n11, self.n12, self.n13, self.n14, self.n15,
                    self.n16, self.n17, self.n18, self.n19, self.n20,

                    self.n21, self.n22, self.n23, self.n24, self.n25,
                    self.n26, self.n27, self.n28, self.n29, self.n30,

                    self.n31, self.n32, self.n33, self.n34, self.n35,
                    self.n36, self.n37, self.n38, self.n39, self.n40,

                    self.n41, self.n42, self.n43, self.n44, self.n45,
                    self.n46, self.n47, self.n48, self.n49, self.n50,

                    self.n51, self.n52, self.n53, self.n54, self.n55,
                    self.n56, self.n57, self.n58, self.n59, self.n60,

                    self.n61, self.n62, self.n63, self.n64, self.n65,
                    self.n66, self.n67, self.n68, self.n69, self.n70,

                    self.n71, self.n72, self.n73, self.n74, self.n75,
                    self.n76, self.n77, self.n78, self.n79, self.n80,

                    self.n81, self.n82, self.n83, self.n84, self.n85,
                    self.n86, self.n87, self.n88, self.n89, self.n90,

                    self.n91, self.n92, self.n93, self.n94, self.n95,
                    self.n96, self.n97, self.n98, self.n99, self.n100
                ]

                self.num = number

                self.show_answer()

            def __repr__(self):
                return f"{self.name}()"

            def show_answer(self):
                for i in range(0, 99):
                    if i == self.num:
                        self.ans = self.LIST[i - 1]
                        break
                    else:
                        continue
                print("Roman number(" + str(self.ans) + ")")

        class Tabels(object):
            def __init__(self, which_tabels, from_1_to_how_much=10):
                self.name = "Tabels"
                self.which_tabels = which_tabels
                self.from_table = from_1_to_how_much

            def __repr__(self):
                return f"{self.name}()"

            def process(self):
                for i in range(1, int(self.from_table + 1)):
                    print(self.which_tabels, "x", i,
                          "=", self.which_tabels * i)

    class ShapesOnConsole(object):
        def __init__(self):
            self.name = "ShapesOnConsole"

        def __repr__(self):
            return f"{self.name}()"

        class Square(object):
            def __init__(self):
                self.name = "Square"
                self.printer()

            def __repr__(self):
                return f"{self.name}()"

            @staticmethod
            def printer():
                print("______________________________")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|____________________________|")

        class Rectangle(object):
            def __init__(self):
                self.name = "Rectangle"
                self.printer()

            def __repr__(self):
                return f"{self.name}()"

            @staticmethod
            def printer():
                print("_____________________________________________________")
                print("|                                                   |")
                print("|                                                   |")
                print("|                                                   |")
                print("|                                                   |")
                print("|                                                   |")
                print("|___________________________________________________|")

        class Triangle(object):
            def __init__(self):
                self.name = "Triangle"
                self.process()

            def __repr__(self):
                return f"{self.name}()"

            @staticmethod
            def process():
                print("      /\\")
                print("     /  \\")
                print("    /    \\")
                print("   /      \\")
                print("  /        \\")
                print(" /          \\")
                print("/____________\\")

    class Designs(object):
        def __init__(self):
            self.name = "Designs"

        def __repr__(self):
            return f"{self.name}()"

        class D1(object):
            def __init__(self):
                self.name = "D1"
                self.process()

            def __repr__(self):
                return f"{self.name}()"

            @staticmethod
            def process():
                print("     ()     ")
                print("    (  )    ")
                print("   (    )   ")
                print("  (      )  ")
                print(" (        ) ")
                print("  (      )  ")
                print("   (    )   ")
                print("    (  )    ")
                print("     ()     ")

    class PrintYourNameManyTimes(object):
        def __init__(self, name, times=2):
            self.nameOfMe = name
            self.times = times
            self.name = "PrintYourNameManyTimes"

        def __repr__(self):
            return f"{self.name}()"

        def process(self):
            for n in range(1, self.times + 1):
                print(n, ":", self.nameOfMe)

    class Vehicles(object):
        def __init__(self):
            self.name = "Vehicles"

        def __repr__(self):
            return f"{self.name}()"

        class Car(object):
            def __init__(self, car_name, rate, total_speed=70, total_gear=5, on_gear=0):
                self.name = "Car"
                self.car_name = car_name
                self.total_gear = total_gear
                self.total_speed = total_speed
                self.on_gear = on_gear
                self.rate = rate

            def __repr__(self):
                return f"{self.name}()"

            def info(self):
                print("Car name :", self.car_name)
                print("Total Gear is :", self.total_gear)
                print("Rate :", self.rate)
                print("Total Speed :", self.total_speed)
                print("On Gear :", self.on_gear)

            def change_gear(self, change_gear_to):
                if self.total_gear < change_gear_to:
                    print("total speed = ", self.total_speed,
                          ", but you have given", change_gear_to, "as a gear")
                else:
                    self.on_gear = change_gear_to

            def change_car_name(self, changed_car_name):
                self.car_name = changed_car_name

            def change_car_rate(self, changed_care_rate):
                self.rate = changed_care_rate

            def changed_car_total_speed(self, change_total_speed):
                self.total_speed = change_total_speed

        class Bus(object):
            def __init__(self, bus_name, rate, total_speed=70, total_gear=5, on_gear=0):
                self.bus_name = bus_name
                self.total_gear = total_gear
                self.rate = rate
                self.total_speed = total_speed
                self.on_gear = on_gear
                self.name = "Bus"

            def __repr__(self):
                return f"{self.name}()"

            def info(self):
                print("Bus name :", self.bus_name)
                print("Total Gear is :", self.total_gear)
                print("Rate :", self.rate)
                print("Total Speed :", self.total_speed)
                print("On Gear :", self.on_gear)

            def change_gear(self, change_gear_to):
                if self.total_gear < change_gear_to:
                    print("total speed = ", self.total_speed,
                          ", but you have given", change_gear_to, "as a gear")
                else:
                    self.on_gear = change_gear_to

            def change_bus_name(self, changed_bus_name):
                self.bus_name = changed_bus_name

            def change_bus_rate(self, changed_bus_rate):
                self.rate = changed_bus_rate

            def changed_bus_total_speed(self, change_total_speed):
                self.total_speed = change_total_speed

    class ProcessAge(object):
        def __init__(self, age):
            self.age = age
            self.name = "ProcessAge"
            self.adult = 20
            self.teenager = 13
            self.child = 12

        def __repr__(self):
            return f"{self.name}()"

        def is_adult(self):
            if self.age >= self.adult:
                print("True you are a adult")
                return True

            else:
                print("False you are not a adult")
                return False

        def is_teenager(self):
            if self.age >= self.teenager:
                print("True you are a teenager")
                return True

            else:
                print("False you are not a teenager")
                return False

        def is_child(self):
            if self.age <= self.child:
                print("True you are a child")
                return True

            else:
                print("False you are not a child")
                return False

        def change_age(self, age):
            self.age = age

        def find_age(self):
            print(self.age)

    class FindTheDay(object):
        def __init__(self):
            self.name = "FindTheDay"
            self.process()

        def __repr__(self):
            return f"{self.name}()"

        @staticmethod
        def process():
            day = time.ctime()
            t = day.split(" ")
            print(t[0])

    class CountWords(object):
        def __init__(self, word):
            self.name = "CountWords"
            self.word = word
            self.p1 = ""
            self.p2 = []

        def __repr__(self):
            return f"{self.name}()"

        def process(self):
            self.p1 = self.word.split(" ")
            self.p2 = [x for x in self.p1 if (x != ' ') & (x != '')]

            print(len(self.p2))

    class PrintNumber1ToHowMuch(object):
        def __init__(self, from_no, to_no):
            self.name = "PrintNumber1ToHowMuch"
            self.from_no = from_no
            self.to_no = to_no
            self.process()

        def __repr__(self):
            return f"{self.name}()"

        def process(self):
            for i in range(self.from_no, self.to_no):
                print(i)

    class ChooseOneOrAnother(object):
        def __init__(self, first, secend):
            self.name = " ChooseOneOrAnother"
            self.first = first
            self.secend = secend
            self.choose()

        def __repr__(self):
            return f"{self.name}()"

        def choose(self):
            r = random.randint(1, 2)
            if r == 1:
                print(self.first)

            else:
                print(self.secend)

    class Pong(object):
        def __init__(self, up=20, down=20):
            self.name = "Pong"
            self.up = int(up)
            self.down = int(down)

            self.wn = turtle.Screen()
            self.wn.title("Pong by joel_jebitto")
            self.wn.bgcolor("black")
            self.wn.setup(width=800, height=600)
            self.wn.tracer(0)

            self.score_a = 0
            self.score_b = 0

            self.paddle_a = turtle.Turtle()
            self.paddle_a.speed(0)
            self.paddle_a.shape("square")
            self.paddle_a.color("white")
            self.paddle_a.shapesize(stretch_wid=5, stretch_len=1)
            self.paddle_a.penup()
            self.paddle_a.goto(-350, 0)

            self.paddle_b = turtle.Turtle()
            self.paddle_b.speed(0)
            self.paddle_b.shape("square")
            self.paddle_b.color("white")
            self.paddle_b.shapesize(stretch_wid=5, stretch_len=1)
            self.paddle_b.penup()
            self.paddle_b.goto(350, 0)

            self.ball = turtle.Turtle()
            self.ball.speed(0)
            self.ball.shape("square")
            self.ball.color("white")
            self.ball.penup()
            self.ball.goto(0, 0)
            self.ball.dx = 0.1
            self.ball.dy = -0.1

            self.pen = turtle.Turtle()
            self.pen.speed(0)
            self.pen.color("white")
            self.pen.penup()
            self.pen.hideturtle()
            self.pen.goto(0, 260)
            self.pen.write(f"Player A : {self.score_a}  Player B : {self.score_b}", align="center",
                           font=("Courier", 24, "normal"))

            self.wn.listen()
            self.wn.onkeypress(self.paddle_a_up, "w")
            self.wn.onkeypress(self.paddle_a_down, "s")
            self.wn.onkeypress(self.paddle_b_up, "Up")
            self.wn.onkeypress(self.paddle_b_down, "Down")

            while True:
                self.wn.update()

                self.ball.setx(self.ball.xcor() + self.ball.dx)
                self.ball.sety(self.ball.ycor() + self.ball.dy)

                if self.ball.ycor() > 290:
                    self.ball.sety(290)
                    self.ball.dy *= -1

                if self.ball.ycor() < -290:
                    self.ball.sety(-290)
                    self.ball.dy *= -1

                if self.ball.xcor() > 390:
                    self.ball.goto(0, 0)
                    self.ball.dx *= -1
                    self.score_a += 1
                    self.pen.clear()
                    self.pen.write(f"Player A : {self.score_a}  Player B : {self.score_b}", align="center",
                                   font=("Courier", 24, "normal"))

                if self.ball.xcor() < -390:
                    self.ball.goto(0, 0)
                    self.ball.dx *= -1
                    self.score_b += 1
                    self.pen.clear()
                    self.pen.write(f"Player A : {self.score_a}  Player B : {self.score_b}", align="center",
                                   font=("Courier", 24, "normal"))

                if ((self.ball.xcor() > 340) and (self.ball.xcor() < 350)) and (
                        self.ball.ycor() < (self.paddle_b.ycor()) + 40 and (self.ball.ycor()) > (
                        self.paddle_b.ycor() - 40)):
                    self.ball.setx(340)
                    self.ball.dx *= -1

                if ((self.ball.xcor() < -340) and (self.ball.xcor() > -350)) and (
                        self.ball.ycor() < (self.paddle_a.ycor()) + 40 and (self.ball.ycor()) > (
                        self.paddle_a.ycor() - 40)):
                    self.ball.setx(-340)
                    self.ball.dx *= -1

        def __repr__(self):
            return f"{self.name}()"

        def paddle_a_up(self):
            y = self.paddle_a.ycor()
            y += self.up
            self.paddle_a.sety(y)

        def paddle_a_down(self):
            y = self.paddle_a.ycor()
            y -= self.down
            self.paddle_a.sety(y)

        def paddle_b_up(self):
            y = self.paddle_b.ycor()
            y += self.up
            self.paddle_b.sety(y)

        def paddle_b_down(self):
            y = self.paddle_b.ycor()
            y -= self.down
            self.paddle_b.sety(y)

    class TurtleDrawer(object):
        def __init__(self, PenColor="white", BgColor="black"):
            self.S = turtle.Screen()
            self.S.setup(width=800, height=800)

            try:
                self.S.bgcolor(BgColor)

            except Exception as err:
                print(err)
                print("color not found")

            self.Drawer = turtle.Turtle()

            try:
                self.Drawer.pencolor(PenColor)

            except Exception as err:
                print(err)
                print("color not found")

            self.Drawer.lt(90)

            self.S.listen()
            self.S.onkeypress(self.up, "Up")
            self.S.onkeypress(self.down, "Down")
            self.S.onkeypress(self.right, "Right")
            self.S.onkeypress(self.left, "Left")
            self.S.onkeypress(self.clear, "c")
            self.S.onkeypress(self.goto_center, "0")
            self.S.onkeypress(self.square, "s")
            self.S.onkeypress(self.info, "i")
            self.S.onkeypress(self.circle, "o")
            self.S.onkeypress(self.penup, "u")
            self.S.onkeypress(self.pendown, "d")

            # Game Loop
            try:
                while True:
                    self.S.update()
            except Exception as err:
                print(err)

        def up(self):
            self.Drawer.fd(20)
            print("forward")

        def down(self):
            self.Drawer.bk(20)
            print("backward")

        def left(self):
            self.Drawer.lt(90)
            print("left")

        def right(self):
            self.Drawer.rt(90)
            print("right")

        def clear(self):
            self.Drawer.clear()

        def goto_center(self):
            self.Drawer.penup()
            self.Drawer.goto(0, 0)

        def square(self):
            for s in range(4):
                self.Drawer.fd(100)
                self.Drawer.left(90)

        def circle(self):
            self.Drawer.circle(20)

        def penup(self):
            self.Drawer.penup()

        def pendown(self):
            self.Drawer.pendown()

        def info(self):
            self.Drawer.clear()
            self.Drawer.write(
                f" Forward : up arrow \n backward : down arrow \n right : right arrow \n left : left arrow \n square : s \n goto center : 0 \n clear : c \n circle : o \n penup : u \n pendown : d",
                align="center", font=("Courier", 24, "normal"))

    class PrintStringOppositely(object):
        def __init__(self, string):
            self.name = "PrintStringOppositely"
            self.string = string

            self.N = []
            self.A = []

            self.str = ""

            self.process()

        def __repr__(self):
            return f"{self.name}()"

        def process(self):
            for i in self.string:
                self.str = i + self.str

            print(self.str)

    class PrintTheVowelsInTheStringInCaps(object):
        def __init__(self, string=""):
            self.name = "PrintTheVowelsInTheStringInCaps"
            self.string = string
            self.value = [1, 1]
            self.process()

        def __repr__(self):
            return f"{self.name}()"

        def process(self):
            self.string = self.string.replace("a", "A", 1)
            self.string = self.string.replace("e", "E", 1)
            self.string = self.string.replace("i", "I", 1)
            self.string = self.string.replace("o", "o", 1)
            self.string = self.string.replace("u", "U", 1)

            print(self.string)


if __name__ == '__main__':
    arr = np.array([1, 2, 3])
    print(arr.shape)
