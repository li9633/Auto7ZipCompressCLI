
import os


def clearAllMark(compressPath: list[str]):
    for i in range(0, len(compressPath)):
        compressPath[i] = compressPath[i].replace("\"", "")
    return compressPath


def formatCompressPath(compressPath: list[str]):
    for i in range(0, len(compressPath)):
        if os.path.isdir(compressPath[i]):
            compressPath[i] += "\\"
    return compressPath


def formatCompressFile(compressFile: list[str]):
    for i in range(0, len(compressFile)):
        if os.path.isfile(compressFile[i]):
            compressFile[i] = compressFile[i][0:compressFile[i].rfind(".")]
    return compressFile


def getCompressPath():
    with open("path.txt", encoding='utf-8') as f:
        compressPath: list[str] = f.read().splitlines()
        compressFile: list[str] = compressPath[:]
        formatCompressPath(clearAllMark(compressPath))
        formatCompressFile(clearAllMark(compressFile))
    return compressFile, compressPath


def replaceFile(runCLI):
    with open("path.txt", "w", encoding='utf-8') as f:
        for text in runCLI:
            f.writelines(text)
    if os.path.exists("run.cmd"):
        os.remove("run.cmd")
    os.rename("path.txt", "run.cmd")
    print(f"7z命令行脚本替换成功!，文件位于:{os.getcwd()}\\run.cmd")


def generateFile(runCLI):
    with open("run.cmd", "w", encoding="utf-8") as f:
        for text in runCLI:
            f.writelines(text)
    print(f"7z命令行脚本生成成功!，文件位于:{os.getcwd()}\\run.cmd")
