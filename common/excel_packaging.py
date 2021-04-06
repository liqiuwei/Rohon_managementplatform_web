import openpyxl


class ExcelHandler:
    def __init__(self, file_path):
        """初始化路径"""
        self.file_path = file_path
        self.workbook = None

    def open_file(self):
        """打开文件"""
        workbook = openpyxl.load_workbook(self.file_path)
        self.workbook = workbook
        return workbook

    def get_sheet(self, name):
        """获取表格"""
        workbook_sheet = self.open_file()
        return workbook_sheet[name]

    def read_data(self, name):
        """读取数据,每一行数据存放到字典当中"""
        sheet = self.get_sheet(name)
        # 获取所有的行
        rows = list(sheet)
        # 获取标题
        headers = []
        for row in rows[0]:
            headers.append(row.value)
        # 添加数据
        date = []
        for row in rows[1:]:
            row_date = {}
            for idx, cell in enumerate(row):
                row_date[headers[idx]] = cell.value
            date.append(row_date)
        return date

    def write(self, name, row, colmn, date):
        """写入单元格数据"""
        sheet = self.get_sheet(name)
        sheet.cell(row, colmn).value = date
        self.save()
        self.close()

    def save(self):
        """保存表单"""
        self.workbook.save(self.file_path)

    def close(self):
        """关闭文件"""
        self.workbook.close()
        self.close()
