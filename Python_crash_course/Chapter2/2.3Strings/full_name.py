first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!") 

message = f"Hello, {full_name.title()}!" #.title() 前面字母大写
print(message)

print("Python")
print("\tPython") #\t 前面添加空白
print("Languages:\nPython\nC\nJavaScript")  #\n 换行
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = "  python  "
favorite_language
favorite_language.rstrip() #删除末尾的空格
favorite_language.lstrip() #删除开头的空格
favorite_language.strip() #删除两边的空格


