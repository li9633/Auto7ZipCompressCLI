import sys
import msvcrt
from fileprocess import *
from CLIprocess import *


if __name__ == '__main__':
    args = sys.argv

    processedArgs, method = processRunModeCLIArgs(args[1:])
    processedArgs.pop(processedArgs.index(method))
    option = processCLIArgs(processedArgs)
    try:
        processedArgs.index("-h")
    except ValueError:
        None
    else:
        print("请按任意键继续...")
        msvcrt.getch()
        os._exit(1)

    if os.path.exists("path.txt") is not True:
        print("(path.txt)目录文件不存在！\n请按任意键继续...")
        msvcrt.getch()
        os._exit(1)

    compressFile, compressPath = getCompressPath()
    runCLI: list = []

    for i in range(0, len(compressPath)):
        runCLI.append(generateCLI(
            compressFile[i], compressPath[i], password=option["password"], size=option["size"]))
    runCLI.insert(0, "chcp 65001\n")
    runCLI.append("pause\n")
    swtichRunMode(runCLI, method)
