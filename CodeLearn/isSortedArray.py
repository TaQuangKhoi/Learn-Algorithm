"""
Cho một mảng các số nguyên, hãy kiểm tra xem mảng đã được sắp xếp hay chưa.
Trả về True nếu đúng và False nếu không.

Độ phức tạp thời gian dự kiến: O(n)

Ví dụ:
    - Với arr = [0,1,2]  kết quả là isSortedArray(arr) = true. Mảng đã được sắp xếp.
    - Với arr = [1,4,2]  kết quả là isSortedArray(arr) = false.

Đầu vào/Đầu ra:
    - [Giới hạn thời gian chạy] 1 seconds 
    - [Đầu vào] array of integers arr
    - Điều kiện tiên đề:
        1 ≤ arr.length ≤ 10^6
    - [Đầu ra] boolean
        Trả về True nếu đúng và False nếu không.
"""

def isSortedArray(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


arr = [35, 34, 3, 13, 19, 7, 10, 5, 38, 39]

print(len(arr))

print(isSortedArray(arr))