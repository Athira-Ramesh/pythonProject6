d1={1:4,0:7,5:6,2:8}
print("original directory",d1)
sorted_d1=sorted(d1.items())
print("dictionary is ascending order by value",sorted_d1)
sorted_d1=sorted(d1.items(),reverse=True)
print("dictionary is discending order by value",sorted_d1)