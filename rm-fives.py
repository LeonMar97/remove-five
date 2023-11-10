def solution(num:int)->int:
    str_num=str(num)
    neg=True if str_num[0]=='-' else False
    fives_loc=[i for i,j in enumerate(str_num) if j=='5'] 
    for cur_five in fives_loc:
        if cur_five<len(str_num)-2 and ((int(str_num[cur_five+1])>5 and not neg) or (int(str_num[cur_five+1])<5 and neg)):
            return int(str_num[:cur_five]+str_num[cur_five+1:]) #cur_five+1 is cur_next explained in readme
    return int(str_num[:fives_loc[-1]]+str_num[fives_loc[-1]+1:])
   

if __name__=="__main__":
    print(solution(-595859))