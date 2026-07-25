dic={
    0:'ali',
    1:'ahmad',
    2:'hassan'
    #dictionary dont allow the repeated key value
    #dictionary is mutable and we can change the values of existing dictionary
}#dictionary stores the pair of values with the key on the left side
print(dic[0])
dic[1]="maaz"#this is allowed in the python
print(dic)
#we can also store list corresponding to any key value like that
word_meanings = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": ["a small animal"]
}
print(word_meanings["table"])#it will display value corresponding to key table

nested_dic={
    "name":"maaz",
        "score":{
            "chem":90,
            "bio":60,
            "math":99
        }    
        }
print(nested_dic["score"]["chem"])#and we can access the values of nested dictionary like this 

