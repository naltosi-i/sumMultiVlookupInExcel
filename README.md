# Sumation multi columns value by VLOOKUP function in Excel
## 〇 隣り合う複数の列の値をキーとしてVLOOKUPで検索した戻り値を合計するプログラム。
## This program is sumation of return values by VLOOKUP keys in adacent columns.
  
## □ 説明 Explanation
### 基本構文 
IF(ISNUMBER(\[開始セル\])*1, IFERROR(VLOOKUP(TEXT(\[開始セル\], "@"),\[検索範囲\],\[戻り値列\],FALSE), 0), 0) + …

開始セルに数値が入っていた場合、それをキーとして検索範囲から検索し、戻り値列の値を返す。  
次に、隣の列のセルの値を検索し、戻り値列の値を加える。  
以下目的の列まで同様の処理を行う。

### 使用法
例を参考に変数に値を代入してプログラムを実行する。  
次の名前で「log」フォルダ内にファイルが出力される。(年-月-日_時分秒.txt)  
出力されたファイルのテキストをコピーし、Excelのセル内に貼り付ければ計算が完了する。  

## □ 例 Example
\[開始セル\] = G10  
\[検索範囲\] = レポート!\$G:\$V  
\[戻り値列\] = 16  

>start_column = 'G' # 開始セルの列を文字列で入力  
>start_row = '10' # 開始セルの行を文字列で入力  
>start_cell = start_column + start_row  
>columns = 36 # VLOOKUPしたい列の数  
>value = True # 検索範囲の対象が文字列の場合「True」、数値のままなら「False」  
>sheet = 'レポート4!' # 検索範囲の存在するシートを記入。末尾に「!」  
>search_start = '$' + 'G' # 検索範囲の開始列  
>search_end = '$' + 'V' # 検索範囲の末尾列  
>area = sheet + search_start + ':' + search_end  
>return_column = '16' # 戻り値列（検索範囲の開始列を1とする）  