if __name__ == '__main__':
    list=[]
    N = int(input())
    for i in range(N):
        command=input()
        splitted=command.split()
        match splitted[0]:
            case "insert":
                list.insert(int(splitted[1]), int(splitted[2]))
            case "print":
                print(list)
            case "remove":
                list.remove(int(splitted[1]))
            case "append":
                list.append(int(splitted[1]))
            case "sort":
                list=sorted(list)
            case "pop":
                list.pop()
            case "reverse":
                list.reverse()
                