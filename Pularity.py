vote_dic={"alia":0,"bob":0,"charlie":0} #creating a dic with candidate name
 
n=int(input("No of voters")) #taking no of voters 

for i in range(0,n): #iterating over no of voters
    vote = input("vote for") #get vote for candidates
    
    if vote in vote_dic:  #if candidate found then increase one vote 
       vote_dic[vote] =+1 
    else: 
        print("invalid vote") 

max_vote= max(vote_dic,key=vote_dic.get) # geting the key with maximum value 
t=vote_dic[max_vote] #put that maximum value in variable


for key in vote_dic.keys(): #iterating over keys and compare their value with t
    value=vote_dic[key]    
    if value==t:
       print("winner is ",key)
