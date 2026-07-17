dic={
    0:'ali',
    1:'ahmad',
    2:'hassan'
}
print(dic.keys())
print(len(dic.values()))
print(dic.items())
dic.update({ 0:'maaz'})
print(dic)
print(dic.get(0))#this method shows value if value exists and shows none if it is not instead of error