# Tổng quan

Dữ liệu thô được tải từ trang https://taichinh.nuoiem.com, đây là các dữ liệu sao kê do dự án Nuôi Em công khai.

![cong-khai-tai-chinh-nuoi-em](./assets/cong-khai-tai-chinh-nuoi-em.png)

- Sao kê được chia theo từng năm và từng tháng
- Tất cả các tệp sao kê được Publish to web, nên có thể tải về ở định dạng CSV, link tổng hợp nằm trong file [nuoiem.csv](nuoiem.csv)
- Riêng năm 2021, dữ liệu được bỏ trong cùng một file Google Spreadsheet (trùng ID), sao kê từng tháng là mỗi Sheet nên link có khác với các sao kê năm khác

## Thống kê dữ liệu sai

Dữ liệu thô bị sai rất nhiều về **nội dung** (trùng lặp, dư thừa các dữ liệu tháng khác) và **định dạng** (dư cột, sai tên cột, cột giống như nội dung khác nhau). Nên quá trình xử lý liệu phải kết hợp:

- Thủ công, kiểm tra dữ liệu bằng mắt thường
- Thủ công, với từng tệp dữ liệu riêng biệt (ví dụ xóa các phần thống kê)
- Thủ công, cập nhật lại các mã NE do nội dung giao dịch viết dính liền, thiếu chữ ...
- Tự động (chuẩn hóa tên cột, chuẩn hóa định dạng dữ liệu, extract thông tin từ nội dung giao dịch)