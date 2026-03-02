# 技術文件

## 專案架構

```
git_test/
├── LICENSE            # Apache 2.0 授權條款
├── README.md          # 專案說明（使用者導向）
├── TECHNICAL.md       # 技術文件（開發者導向）
├── main.py            # 主程式入口與核心邏輯
└── tests/
    ├── __init__.py    # 使 tests 成為 Python 套件
    └── test_main.py   # 測試程式
```

## 模組說明

### `main.py`

專案的唯一原始碼檔案，包含所有運算函式與 CLI 入口邏輯。

---

### 函式一覽

#### `hello_world_en()`

- **用途**：印出英文問候訊息
- **參數**：無
- **回傳值**：無（副作用：`print("Hello, World!")`）

#### `hello_world_zh()`

- **用途**：印出中文問候訊息
- **參數**：無
- **回傳值**：無（副作用：`print("哈囉！世界！")`）

#### `additionMethod(num1, num2)`

- **用途**：回傳兩數之和
- **參數**：
  - `num1` (`int | float`)：第一個數字
  - `num2` (`int | float`)：第二個數字
- **回傳值**：`int | float` — `num1 + num2`

#### `subtractionMethod(num1, num2)`

- **用途**：回傳兩數之差
- **參數**：
  - `num1` (`int | float`)：被減數
  - `num2` (`int | float`)：減數
- **回傳值**：`int | float` — `num1 - num2`

#### `divisionMethod(num1, num2)`

- **用途**：回傳兩數相除的結果
- **參數**：
  - `num1` (`int | float`)：被除數
  - `num2` (`int | float`)：除數
- **回傳值**：`float` — `num1 / num2`
- **例外**：當 `num2 == 0` 時拋出 `ZeroDivisionError`

#### `multiplicationMethod(num1, num2)`

- **用途**：回傳兩數之積
- **參數**：
  - `num1` (`int | float`)：第一個數字
  - `num2` (`int | float`)：第二個數字
- **回傳值**：`int | float` — `num1 * num2`

---

## CLI 入口點邏輯

程式透過 `if __name__ == '__main__':` 區塊作為 CLI 入口，執行流程如下：

```
1. 印出中英文問候
2. 檢查 sys.argv 是否有至少 4 個參數（程式名 + 數字1 + 運算子 + 數字2）
   └─ 不足 → 印出 "Not enough arguments." 並以 exit code 1 結束
3. 解析參數：num1, operator, num2
4. 根據 operator 分派：
   ├─ '+' → additionMethod(int(num1), int(num2))
   ├─ '-' → subtractionMethod(int(num1), int(num2))
   ├─ '/' → divisionMethod(int(num1), int(num2))
   ├─ '*' → multiplicationMethod(int(num1), int(num2))
   └─ 其他 → 印出 "Unsupported operator."
```

### 已知限制

| 項目 | 說明 |
|------|------|
| 僅支援整數輸入 | CLI 以 `int()` 轉換輸入，不支援小數（函式本身支援 float） |
| 無除以零處理 | CLI 層未捕捉 `ZeroDivisionError`，會直接顯示 Python traceback |
| 無輸入驗證 | 非數字輸入會導致 `ValueError` |

---

## 測試策略

### 框架

使用 Python 內建 `unittest` 模組，無需額外安裝。

### 測試分類

| 測試類別 | 說明 | 類別名稱 |
|----------|------|----------|
| 加法測試 | 正數、負數、零、浮點數 | `TestAdditionMethod` |
| 減法測試 | 正數、負數結果、零、浮點數 | `TestSubtractionMethod` |
| 除法測試 | 整除、非整除、除以零例外 | `TestDivisionMethod` |
| 乘法測試 | 正數、負數、零、浮點數 | `TestMultiplicationMethod` |
| 問候測試 | 使用 mock 驗證 print 輸出 | `TestHelloWorld` |
| CLI 測試 | 使用 subprocess 驗證完整流程 | `TestCLI` |

### 執行方式

```bash
# 執行所有測試（詳細模式）
python -m unittest discover tests -v

# 執行特定測試類別
python -m unittest tests.test_main.TestAdditionMethod -v

# 執行單一測試
python -m unittest tests.test_main.TestDivisionMethod.test_divide_by_zero -v
```
