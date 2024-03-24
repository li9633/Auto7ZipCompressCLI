from fileprocess import generateFile, replaceFile


def generateCLI(compressPath: str, compressFile: str, password=None, compresslevel=None, size: str = None, mhe=True):
    generStr = "7z a "
    if password is not None:
        generStr += f"-p{password} "
    if compresslevel is not None:
        generStr += f"-mx{compresslevel} "
    if size is not None:
        generStr += f"-v{size} "
    if mhe is True:
        generStr += f"-mhe=on "
    generStr += f"\"{compressPath}.7z\" \"{compressFile}\"\n"
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
    print("使用\'-r\' , \'-p\' 选项来控制脚本文件的生成方式")
    print("\'-r\' 将path.txt文件替换为run.cmd")
    print("\'-p\' 生成一个新的run.cmd文件,path.txt将不会被改变")
    print("不指定生成方式时，将默认使用\'-r\'")
    print("--------------------------------------------------------------------")
    print(f"使用{validCLI}有效选项来控制批量压缩的方式")
    for i in range(0, len(validCLI)):
        if validCLI[i] == "-p":
            print(f"{validCLI[i]} 为压缩文件设置一个密码,例子 {validCLI[i]}1234")
        if validCLI[i] == "-v":
            print(f"{validCLI[i]} 为压缩文件设置分卷包,例子 {validCLI[i]}1g")
        if validCLI[i] == "-mx":
            print(f"{validCLI[i]} 压缩时指定压缩等级 0\|1\|3\|5\|7\|9  0最快 ，9文件体积最小")
        if validCLI[i] == "-h":
            print(f"{validCLI[i]} 显示此帮助")
        if validCLI[i] == "-mhe":
            print(f"{validCLI[i]} 关闭加密文件头 默认:开启")
    print("--------------------------------------------------------------------")


def processCLIArgs(args: list[str]):
    validCLI: list[str] = ["-h", "-p", "-v", "-mx", "-mhe"]
    arg = str()
    i = 0
    isVaild = 0
    isVaildArg = []
    option = {"password": None, "size": None, "level": None, "mhe": True}
    for arg in args:
        isVaild = 0
        for i in range(0, len(validCLI)):
            if arg.find(validCLI[i]) != -1:
                if arg[arg.find(validCLI[i]):len(validCLI[i])] == "-p":
                    option["password"] = arg.replace("-p", "")
                if arg[arg.find(validCLI[i]):len(validCLI[i])] == "-v":
                    option["size"] = arg.replace("-v", "")
                if arg[arg.find(validCLI[i]):len(validCLI[i])] == "-h":
                    helpMenu(validCLI)
                if arg[arg.find(validCLI[i]):len(validCLI[i])] == "-mx":
                    option["level"] = arg.replace("-mx", "")
                if arg[arg.find(validCLI[i]):len(validCLI[i])] == "-mhe":
                    option["mhe"] = False
                    isVaild -= 1
            else:
                isVaild += 1
        if isVaild == len(validCLI):
            isVaildArg.append(arg)

    if len(isVaildArg) != 0:
        return ValueError, isVaildArg
    else:
        return option, None
