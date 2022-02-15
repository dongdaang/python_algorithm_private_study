def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    idx_list={}
    for idx,name in enumerate(enroll):
        idx_list[name]=idx
    for idx,name in enumerate(seller):
        price=100*amount[idx]
        answer[idx_list[name]]+=price
        while referral[idx_list[name]]!="-":
            answer[idx_list[name]]-=price//10
            name=referral[idx_list[name]]
            answer[idx_list[name]]+=price//10
            price=price//10
            if price==0:
                break
        answer[idx_list[name]]-=price//10
    return answer