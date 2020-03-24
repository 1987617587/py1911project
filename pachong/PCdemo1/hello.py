print("hello world")
arr1 = [1, 2]
arr2 = ["a", "b", "c", "b"]
# for i in arr2:
for i in range(len(arr2)):
    print(arr2[i],arr1[i%2])

