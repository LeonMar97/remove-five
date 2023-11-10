def solution(num:int)->int:
    str_num=str(num)
    neg=True if str_num[0]=='-' else False
    fives_loc=[i for i,j in enumerate(str_num) if j=='5']
    if not neg:
        for i in fives_loc:
            if i<len(str_num)-2 and int(str_num[i+1])>5:
                return int(str_num[:i]+str_num[i+1:])
        return int(str_num[:fives_loc[-1]]+str_num[fives_loc[-1]+1:])
    else:
        for i in fives_loc:
            if i<len(str_num)-2 and int(str_num[i+1])<5:
                return int(str_num[:i]+str_num[i+1:])
        return int(str_num[:fives_loc[-1]]+str_num[fives_loc[-1]+1:])

if __name__=="__main__":
    print(solution(1525))
    

    
