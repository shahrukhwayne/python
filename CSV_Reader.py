import pandas as pd
import numpy as np

data = {
    'name': np.array(['shahrukh', 'salman', 'amir']),
    'roll_no': np.array([3, 15, 21]),
    'age': np.array([21, 20, 22]),
    'branch': np.array(['Computer Science', 'Mechanical Engineering', 'Literature']),
    'city': np.array(['Delhi', 'Mumbai', 'Lucknow']),
    'marks': np.array([85, 90, 75])
}

df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)

while True:
    print("\n===== CSV Data Reader Menu =====")
    print("1. Display Full Data")
    print("2. Display First 3 Rows")
    print("3. Show All Columns")
    print("4. Filter Students by City")
    print("5. Sort Students by Marks")
    print("6. Show Average Marks")
    print("7. Exit")

    choice = int(input("Enter Your Choice (1-7): "))

    if choice == 7:
        print("----Exiting Program Goodbye---")
        break

    match choice:
        case 1:
            print("\nFull Data:\n")
            print(df)
        case 2:
            print("\nFirst 3 Rows:\n")
            print(df.head(3))
        case 3:
            print("\nColumns:\n")
            print(df.columns.to_list())
        case 4:
            city = input("Enter city to filter: ")
            print(df[df['city'] == city])
        case 5:
            print("\nSorted by Marks:\n")
            print(df.sort_values('marks', ascending=False))
        case 6:
            print("\nAverage Marks:\n", df['marks'].mean())
