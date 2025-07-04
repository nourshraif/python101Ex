def ItemExist(list,nb):
     if nb>list[-1]:
         return None
     elif nb<list[0]:
         return None
     else:
         for item in list:
             if item==nb:
                 return True
             
list=[1,2,3,4,5,6]    
result=ItemExist(list,23)
if(result is None):
    print("nb does not exist in the list") 
else:
    print("nb exists in the list")