# test_vscode_python.py

import sys
import platform
import datetime

def main():
    print("=== Python 环境测试 ===")
    
    # Python版本
    print(f"Python版本: {sys.version}")
    
    # 操作系统
    print(f"操作系统: {platform.system()} {platform.release()}")
    
    # 当前时间
    print(f"当前时间: {datetime.datetime.now()}")
    
    # 简单计算
    a, b = 10, 20
    print(f"计算测试: {a} + {b} = {a + b}")
    
    print("✅ 如果你看到这行，说明运行成功！")

if __name__ == "__main__":
    main()