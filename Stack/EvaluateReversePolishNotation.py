class Solution:
    def evalRPN(self, tokens) -> int:
        index = 0
        while index < len(tokens):
            flag = 0
            item = tokens[index]
            if item == "+":
                temp = int(tokens[index-1])+int(tokens[index-2])
                flag = 1

            if item == "/":
                temp = int(int(tokens[index-2])/int(tokens[index-1]))
                flag = 1
            if item == "*":
                temp = int(tokens[index-2])*int(tokens[index-1])
                flag = 1
            if item == "-":
                temp = int(tokens[index-2])-int(tokens[index-1])
                flag = 1
            if flag == 1:
                tokens = tokens[:index-2]+[temp]+tokens[index+1:]
                index -= 2
            # print(tokens)
            index += 1
        return int(tokens[0])
