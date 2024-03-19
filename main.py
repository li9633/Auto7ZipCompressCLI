import os
import sys
import msvcrt


def generateCLI(password, compresslevel, compressPath, size: str = '15g'):
    generStr = f"7z a -v{size} -p{password} -mx{compresslevel} -mhe=on \"{compressPath}.7z\" \"{compressPath}\""
    return generStr


def getCompressPath() -> list[str]:
    with open(".\path.txt", encoding='utf-8') as f:
        compressPath: list[str] = f.read().splitlines()
        f.close()
    return compressPath


def replaceFile(runCLI):
    with open(".\path.txt", "w", encoding='utf-8') as f:
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
    for i in CLIArgs:
        processedArgs.append(i)
    try:
        processedArgs.index("-r")
    except ValueError:
        None
    else:
        r_index = processedArgs.index("-r")

    try:
        processedArgs.index("-n")
    except ValueError:
        None
    else:
        n_index = processedArgs.index("-n")

    if r_index > -1 and n_index > -1:
        method = processedArgs.pop(r_index if r_index > n_index else n_index)
        return processedArgs, "-n" if method == "-r" else "-r"
    else:
        method = processedArgs[processedArgs.index(
            "-r" if r_index > n_index else "-n")]
        return processedArgs, method


def swtichRunMode(runCLI, method="-r"):
    if method == "-r":
        replaceFile(runCLI)
    else:
        generateFile(runCLI)


if __name__ == '__main__':
    args = sys.argv
    if os.path.exists("path.txt") is not True:
        print("(path.txt)目录文件不存在！\n请按任意键继续...")
        # msvcrt.getch()
        os._exit(1)
    compressPath: list[str] = getCompressPath()
    runCLI: list = []
    processedArgs, method = processCLIArgs(args[1:])
    processedArgs.pop(processedArgs.index(method))
    for i in range(0, len(compressPath)):
        runCLI.append(generateCLI(1234, 0, compressPath[i])+"\n")
    runCLI.insert(0, "chcp 65001\n")
    runCLI.append("pause\n")
    swtichRunMode(runCLI, method=method)
