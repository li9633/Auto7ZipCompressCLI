import os
import sys
import msvcrt


def formatCompressPath(compressPath: list[str]):
    for i in range(0, len(compressPath)):
        if os.path.isdir(compressPath[i]):
            compressPath[i] += "\\"
    return compressPath


def formatCompressFile(compressFile: list[str]):
    for i in range(0, len(compressFile)):
        if os.path.isfile(compressFile[i]):
            compressFile[i] = compressFile[i].split(".")[0]
    return compressFile


def generateCLI(password, compresslevel, compressPath: str, compressFile: str, size: str = '15g'):
    generStr = f"7z a -v{size} -p{password} -mx{compresslevel} -mhe=on \"{compressPath}.7z\" \"{compressFile}\"\n"
    return generStr


def getCompressPath():
    with open("path.txt", encoding='utf-8') as f:
        compressPath: list[str] = f.read().splitlines()
        compressFile = compressPath[:]
        formatCompressPath(clearAllMark(compressPath))
        compressFile = formatCompressFile(clearAllMark(compressFile))
    return compressFile, compressPath


def replaceFile(runCLI):
    with open("path.txt", "w", encoding='utf-8') as f:
        for text in runCLI:
            f.writelines(text)
    os.rename("path.txt", "run.cmd")


def generateFile(runCLI):
    with open("run.cmd", "w", encoding="utf-8") as f:
        for text in runCLI:
            f.writelines(text)


def processCLIArgs(CLIArgs: list):
    processedArgs = []
    r_index = -1
    n_index = -1
    lock = -1
    for i in CLIArgs:
        processedArgs.append(i)
    try:
        processedArgs.index("-r")
    except ValueError:
        lock += 1
    else:
        r_index = processedArgs.index("-r")

    try:
        processedArgs.index("-n")
    except ValueError:
        lock += 1
    else:
        n_index = processedArgs.index("-n")

    if lock == True:
        processedArgs.append("-r")
        return processedArgs, "-r"

    if r_index > -1 and n_index > -1:
        method = processedArgs.pop(r_index if r_index > n_index else n_index)
        return processedArgs, "-n" if method == "-r" else "-r"
    else:
        method = processedArgs[processedArgs.index(
            "-r" if r_index > n_index else "-n")]
        return processedArgs, method


def swtichRunMode(runCLI, method):
    if method == "-r":
        replaceFile(runCLI)
    else:
        generateFile(runCLI)


def clearAllMark(compressPath: list[str]):
    for i in range(0, len(compressPath)):
        compressPath[i] = compressPath[i].replace("\"", "")
    return compressPath


if __name__ == '__main__':
    args = sys.argv
    if os.path.exists("path.txt") is not True:
        print("(path.txt)目录文件不存在！\n请按任意键继续...")
        msvcrt.getch()
        os._exit(1)
    compressFile, compressPath = getCompressPath()
    runCLI: list = []
    processedArgs, method = processCLIArgs(args[1:])
    processedArgs.pop(processedArgs.index(method))
    for i in range(0, len(compressPath)):
        runCLI.append(generateCLI(1234, 0,  compressFile[i], compressPath[i]))
    runCLI.insert(0, "chcp 65001\n")
    runCLI.append("pause\n")
    swtichRunMode(runCLI, method)
