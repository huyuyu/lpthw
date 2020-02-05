# Strings, Bytes, and Character Encodings

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()  
    # ＃readline()里面的代码会扫描文件的每一个字节，直到找到一个\n为止
    # 然后它停止读取文件，并且返回此前读取的文件内容。
    # 读取完成后将“磁头”移到\n后面，下次读取的时候就会自动读取下一行。
    if line:
	    print_line(line, encoding, errors)
	    return main(language_file, encoding, errors)  # 递归，保持循环

def print_line(line, encoding, errors):
    next_lang = line.strip()  # 去掉'\n'
    raw_bytes = next_lang.encode(encoding, errors=errors)  # 解码
    cooked_string = raw_bytes.decode(encoding, errors=errors) #编码成字符串
    print(raw_bytes, "<===>", cooked_string)

languages = open("ex23_languages.txt", encoding="utf-8") 
main(languages, input_encoding, error)

# 了解 string 同  byte swquences 的区别
#      在Python中，字符串是一段由UTF-8编码的字符序列。
#      字节是Python用来存储这个UTF-8字符串的“原始”字节序列
#      字节以b'开头告诉Python您正在使用字节。
#      字节 = 字符串.encode()  字符串 = 字节.decode()