import requests
from bs4 import BeautifulSoup
import openpyxl

def ready():
    f = open("naverSeries.csv", "w", encoding='UTF-8')
    f.write("순위,제목,작가\n")
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(['순위', '제목', '작가'])
    return f, wb, sheet

def to_csv_file(f, rank, title, writer):  # csv파일로
    f.write(str(rank) + "," + title + "," + writer + "\n")

def to_xlsx_file(sheet, rank, title, writer):  # xlsx파일로
    sheet.append([rank, title, writer])

def end(f, wb):
    f.close()
    wb.save("naverSeries.xlsx")

f, wb, sheet = ready()
count = 1

for page in range(1, 6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page=" + str(page)).text
    html = BeautifulSoup(raw, 'html.parser')
    containers = html.select("ul.lst_thum.v1 > li")
    for container in containers:
        title = container.select_one("ul.lst_thum.v1 a > strong").text.replace(",", " ")
        writer = container.select_one("ul.lst_thum.v1 a > span.writer").text.replace(",", " ")
        to_csv_file(f, count, title, writer)
        to_xlsx_file(sheet, count, title, writer)
        count += 1

for column in sheet.columns:#엑셀 너비 조정
    max = 0
    column_name = column[0].column_letter
    for cell in column:
        if len(str(cell.value)) > max:
            max = len(str(cell.value))
    width = (max + 2) * 2
    sheet.column_dimensions[column_name].width = width

end(f, wb)