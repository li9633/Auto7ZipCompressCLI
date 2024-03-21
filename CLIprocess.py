from fileprocess import generateFile, replaceFile


def generateCLI(password, compresslevel, compressPath: str, compressFile: str, size: str = '15g'):
    generStr = f"7z a -v{size} -p{password} -mx{compresslevel} -mhe=on \"{compressPath}.7z\" \"{compressFile}\"\n"
    return generStr


def processRunModeCLIArgs(CLIArgs: list):
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


def helpMenu(validCLI: list):
    print(f"使用{validCLI}这些有效选项来控制生成的脚本")
    for i in range(0, len(validCLI)):
        if validCLI[i] == "-p":
            print(f"{validCLI[i]} 为压缩文件设置一个密码,例子 {validCLI[i]}1234")
        if validCLI[i] == "-v":
            print(f"{validCLI[i]} 为压缩文件设置分卷包,例子 {validCLI[i]}1g")
        if validCLI[i] == "-h":
            print(f"{validCLI[i]} 显示此帮助")


def processCLIArgs(args: list[str]):
    validCLI: list[str] = ["-p", "-v", "-h"]
    arg = str()
    i = 0
    option = {"password": None, "size": None}
    for arg in args:
        for i in range(0, len(validCLI)):
            if arg.find(validCLI[i]) != -1:
                if arg[arg.find(validCLI[i]):len(validCLI[i])] == "-p":
                    option["password"] = arg.replace("-p", "")
                if arg[arg.find(validCLI[i]):len(validCLI[i])] == "-v":
                    option["size"] = arg.replace("-v", "")
                if arg[arg.find(validCLI[i]):len(validCLI[i])] == "-h":
                    helpMenu(validCLI)
    return option
