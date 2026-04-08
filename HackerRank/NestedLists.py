if __name__ == '__main__':
    records=[]
    scores=[]
    found=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        alunmi=[name,score]
        records.append(alunmi)
        scores.append(score)
    scores=sorted(set(scores))
    score=scores[-2]
    for i in range(0,len(records)):
        if score== records[i][1]:
            found.append(records[i][0])
    found=sorted(found)
    for i in range(0,len(found)):
        print(found[i])