def find_senior(lst):
    k = 0
    arr = []
    for i in range(len(lst)):
        if lst[i]['age'] > k:
            k = lst[i]['age']
    for j in range(len(lst)):
        if lst[j]['age'] == k:
            arr.append(lst[j])
    return arr
 
def main():
    list1 = [
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
  { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
    ]

    print(find_senior(list1))

if __name__ == "__main__":
    main()
