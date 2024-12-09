def find_person(phonebook, target_name):
  """
  Hàm tìm kiếm một người trong danh bạ

  Args:
    phonebook: Danh sách các liên lạc, mỗi liên lạc là một tuple (tên, số điện thoại)
    target_name: Tên cần tìm

  Returns:
    Số điện thoại của người được tìm thấy, hoặc "Not Found" nếu không tìm thấy
  """

  for person in phonebook:
    if person[0] == target_name:
      return person[1]
  return "Not Found"

# Ví dụ danh bạ
phonebook = [
  ("Nguyen Van A", "0987654321"),
  ("Tran Thi B", "0123456789"),
  ("Le Van C", "9876543210")
]

# Tìm kiếm
target_name = "Tran Thi B"
result = find_person(phonebook, target_name)
print(result)