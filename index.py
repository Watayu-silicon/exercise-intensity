num_array = [0, 14.3, 28.6, 42.9, 57.2, 71.5, 85.8, 100]
word_array = ["非常に楽", "かなり楽", "やや楽", "ややきつい", "きつい", "かなりきつい", "非常にきつい"]
exercise = int(input())
rest = int(input())
age = int(input())
if age < 65:
    max = 220-age
elif age >= 65:
    max = 207-(age*0.7)
mid1 = exercise - rest
mid2 = max - rest
result = round(mid1 / mid2 * 100, 1)
for i in range(0, 7):
    if result >= num_array[i] and result < num_array[i+1]:
        print("運動強度", result, "%")
        print(word_array[i])