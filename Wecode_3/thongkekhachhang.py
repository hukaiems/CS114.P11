import pandas as pd
import sys

# em bi loi khi co 1 vai khach hang bi chenh 1 gia tri so voi dap an nen da tham khao goi y tu ban 
# Tang Nhat MSSV: 22521027

# low_memory=False em duoc he dieu hanh goi y khi chay ra loi
# em xem tren pandas va biet duoc parse_dates=
df = pd.read_csv(sys.stdin,
encoding='unicode_escape', encoding_errors='replace', low_memory=False, parse_dates=['InvoiceDate'])

# em da xu ly cai gia tri Nan trong cot CustomerID
df = df.dropna(axis='rows', subset='CustomerID')

# dong code em tham khao cua ban Tang Nhat
df = df.groupby('CustomerID')['InvoiceDate'].max().reset_index().sort_values(by='CustomerID')


# em tra chatgpt va biet duoc khi su dung min() thi no tro the single timestamp vi the nen khong can dt.
df["score"] = (df["InvoiceDate"] - df["InvoiceDate"].min()).dt.days

# em tra tren pandas va phat hien co .drop_duplicates()
# em tra tren pandas va biet duoc ham .sort_values()

# day la y tuong cu cua em nhung khong the lam duoc vi bi lech 1 vai gia tri
# df = df.drop_duplicates( subset=["CustomerID"], keep='last')
# df = df.sort_values(by=["CustomerID"])


# em tra tren stackoverflow va biet dong lenh index=False
sys.stdout.write(df.to_string(index=False, columns= ["CustomerID", "score"]))
sys.stdout.write('\n')