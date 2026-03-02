# Git Test — Python CLI 計算機

一個簡單的 Python 命令列計算機工具，支援四則運算（加、減、乘、除）並提供中英文問候訊息。

## 功能特色

- **四則運算**：加法 (`+`)、減法 (`-`)、乘法 (`*`)、除法 (`/`)
- **中英文問候**：每次執行時輸出 "Hello, World!" 及 "哈囉！世界！"
- **CLI 介面**：透過命令列參數直接運算

## 環境需求

- Python 3.6 以上

## 使用方式

```bash
python main.py <數字1> <運算子> <數字2>
```

### 範例

```bash
# 加法
python main.py 10 + 5
# 輸出: The sum of 10 and 5 is 15

# 減法
python main.py 10 - 3
# 輸出: The difference of 10 and 3 is 7

# 乘法
python main.py 4 '*' 5
# 輸出: The product of 4 and 5 is 20
# 注意：在 shell 中 * 需要加引號以避免被展開

# 除法
python main.py 10 / 2
# 輸出: The division of 10 by 2 is 5.0
```

> **提示**：乘法運算子 `*` 在某些 shell 中會被解讀為萬用字元，請以引號包裹（如 `'*'` 或 `"*"`）。

## 執行測試

```bash
python -m unittest discover tests -v
```

## 專案結構

```
├── LICENSE            # Apache 2.0 授權
├── README.md          # 專案說明文件
├── TECHNICAL.md       # 技術文件
├── main.py            # 主程式
└── tests/
    ├── __init__.py
    └── test_main.py   # 單元測試與 CLI 整合測試
```

## 授權

本專案採用 [Apache License 2.0](LICENSE) 授權。
