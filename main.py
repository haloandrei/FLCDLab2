# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class HashTable(object):
    def __init__(self, length = 17):
        self.array = [None for i in range(0,length)]
        self.fill = 0

    def hash(self, key):
        sumString = 0
        for i in key:
            sumString += ord(i)
        return sumString % len(self.array)

    def add(self, symbol):
        self.fill += 1
        if self.fill > len(self.array):
            self.double()
        index = self.hash(symbol)
        if self.array[index] is not None:
            for val in self.array[index]:
                if (val == symbol):
                    break
                else:
                    self.array[index].append(symbol)
        else:
            self.array[index] = []
            self.array[index].append(symbol)

    def get(self, symbol):
        index = self.hash(symbol)
        if self.array[index] is None:
            return None
        else:
            for val in self.array[index]:
                if (val == symbol):
                    return symbol
            return None

    def double(self):
        print("hashTable expanded")
        newHtb = HashTable(len(self.array) * 2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue
            for val in self.array[i]:
                newHtb.add(val)
        self.array = newHtb.array

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st =HashTable(3)
    st.add("numar1")
    st.add("1")
    st.add("25")
    st.add("50")
    st.add("nu")
    st.add("a")
    st.add("b")
    print(st.get("numar1"), "at index:", st.hash("numar1"))
    print(st.get("1"), "at index:", st.hash("1"))
    print(st.get("25"), "at index:", st.hash("25"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
