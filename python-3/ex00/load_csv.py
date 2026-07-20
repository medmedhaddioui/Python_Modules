# def findDisappearedNumbers( nums) :
#         nums.sort() 
#         print( nums)
#         missing_elements =  []
#         for index , i  in enumerate(nums):
#             if i != index+ 1:
#                 print(i , index)
#                 missing_elements.append(i)
#         return missing_elements
# test = [4,3,2,7,8,2,3,1]
# print(findDisappearedNumbers(test))


# -> Dataset: (You have to adapt the type of return according to your library)
import pandas as pd # type: ignore

def load(path: str):
    myData = pd.read_csv(path)
    myData.head()
    print(myData)    
