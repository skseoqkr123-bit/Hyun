# 리스트에 데이터 추가
# 맨 마지막에 추가
# 중간에 추가 

# 리스트 변수
scores = [ 10, 20, 30]
# 추가-마지막 
scores. append(100)
print(scores)
# append는 항상 마지막에 써야 함. 줄 설떄 뒤에 서는 느낌이랑 같음. insert는 추가, 새치기 같은 느낌 
scores.insert(1,200) #추가(insert)는 index위치에 
print(scores)

# <새로운 변수> deledte, del붙이고 끝에 인덱스로 마무리 하면 해당 인덱스 순서의 형을 지워버림
del scores[0] 

print(scores)
scores.pop(0) #pop. 이것도 마찬가지로 지우는 변수. 해당 괄호 안에 그 값이나 번호를 입력하면 지워진다. 