import os.path

#解压指定路径下的所有文件
def  delete_xls_all(log_path):
    for dirpath, dirnames, filenames in os.walk(log_path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.gz':
               filepath = os.path.join(dirpath, filename)
               delfile(filepath) # 删除文件
            else:
                print(dirpath + ':  There is not gz file')
#删除单个文件          
def delfile(fname):
    if os.path.exists(fname):
        os.remove(fname)

def main():
    log_path=input('enter a path:')
    #log_path = 'E:\\python_log\\test_gz_file'
    if os.path.exists(log_path):#判断路径是否存在 异常处理1
       delete_xls_all(log_path)
    else:
        print('path do not exist')
        main()

if __name__ == "__main__":
    main()
