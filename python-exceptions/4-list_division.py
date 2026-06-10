#!/usr/bin/python3
def list_division(my_l_1, my_l_2, list_length):
    new_list = []
    for i in range(list_length):
        res = 0
        try:
            res = my_l_1[i] / my_l_2[i]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except (TypeError, ValueError):
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return new_list
