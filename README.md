# Bloxorz

Có 2 file chính là **main.py** và **Bloxorz.pyde**, cả 2 đều có các dòng tương tự sau,
để chạy thuật toán nào thì xóa comment của 2 cái tương ứng

```python
#
# name = "BFS"
# output_0 = input_0.BFS()
#
name = "DFS"
output_0 = input_0.DFS()
#
# name = "A*"
# output_0 = input_0.A_Star()
```

Hiện tại chỉ có 1 input đơn giản, không có công tắt, đã định nghĩa, chưa hiện thực

Để chạy chương trình thông thường thì chạy python cho file main.py

Để chạy giao diện gọi lệnh ***make_dist.bat***

Giao diện viết bằng thư viện Processing trên JYTHON, có thể tải IDE tại trang chủ Processing.org và cài đặt mode Python để soạn thảo và debug

## DSA.py

Hiện thực một cách tổng quát 3 thuật toán tìm kiếm DFS, BFS, A*, chỉ cần đúng inteface là chạy được, không phân biệt bài toán nào
Cấu trúc dữ liệu HEAP, BINARY_TREE

## State.py

Mỗi state được biểu diễn bằng một array 2 chiều, mỗi phần tử gồm 8 bit dữ liệu, và tọa độ cùng trạng thái (xoay, nằm theo chiều dọc, ngang)
