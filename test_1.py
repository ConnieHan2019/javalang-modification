import ast
import csv
import os
from javalang.parser import Parser
from javalang.tokenizer import tokenize

from pkg_resources import resource_string
from javalang.parse import parse


def file_name(file_dir, output_root):
    L = []
    file_names = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_type = os.path.splitext(file)[1]
            prefix = os.path.splitext(file)[0]
            # print("prefix: ", prefix)
            # print("filename: ", file, "file type: ", file_type)
            if file_type == '.java':
                new_file = os.path.join(root, prefix + "_output.txt")
                file_names.append(new_file.replace(file_dir, output_root))
                L.append(os.path.join(root, file))
        for dir in dirs:
            sub_l, sub_files = file_name(dir, output_root)
            if len(sub_l) > 0:
                L.append(file_name(dir))
                file_names.append(sub_files)
    return L, file_names


def javalangparse(file_name):
    f = open(file_name, "r")
    tokens = tokenize(f.read())
    parser = Parser(tokens)
    parser.parse()
    sorted(parser.logs)
    length = len(parser.logs)
    print("total length：" + str(length))
    f.close()
    with open(file="test.csv", mode="w", encoding='UTF8', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # 先写入columns_name
        writer.writerow(["index", "column", "statement"])
        for i in range(length):
            writer.writerows([str(i),parser.logs[i].position,parser.logs[i].classname])

    # ast.dump(tree,f)
    # f.close()


# tokens = tokenize(f.read())
# parser = Parser(tokens)
# tree =  parser.parse()
# for node in tree:
#    print(node)


# Press the green button in the gutter to run the script.

root = "/Users/mingluhan/Graduation-Project/projects/TestJavaPj"
output_root = "/Users/mingluhan/Graduation-Project/projects/TestJavaPjOutput"
# root = "/Users/mingluhan/Graduation-Project/projects/TestJavaPj"
package1 = "/Users/mingluhan/Graduation-Project/projects/TestJavaPj/src/main/java/package1"
java_files, new_files = file_name(root, output_root)
for java_file in java_files:
    javalangparse(java_file)
