
# Auto7ZipCompressCLI

Windows环境快速生成批量7z压缩脚本的命令行工具

## 🚀 快速配置
1. 将程序文件和7-zip安装目录添加到系统PATH
2. 验证安装：
   ```cmd
   a7z -h && 7z -v
   ```

## 🔧 基础使用
1. 创建`path.txt`并粘贴待压缩路径（每行一个）
2. 生成脚本：
   ```cmd
   a7z -n -p密码 -v分卷大小 -mx压缩等级
   ```
3. 执行生成的`run.cmd`

## ⚙️ 核心参数
参数 | 说明
---|---
`-n` | 安全模式（保留path.txt）
`-p密码` | 设置压缩密码（示例：`-p1234`）
`-v大小` | 分卷压缩（如`-v2g`=2GB分卷）
`-mx0-9` | 压缩等级（0最快，9最小）
`-r` | 覆盖模式（替换旧脚本）

## 📌 注意事项
- 需提前安装7-zip（建议v19+）
- 路径中避免特殊字符`&%$`
- 加密时默认启用文件头加密（-mhe）
- 
[示例] 快速压缩：
```cmd
a7z -n -p123 -v500m -mx7
