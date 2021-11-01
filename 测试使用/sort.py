from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("参数数据处理")
        self.resize(400,400)
        self.setup_ui()

    def setup_ui(self):
        self.lin = QLineEdit("", self)
        self.lin.move(120,50)
        self.lin.resize(250, 25)
        # 第一个按钮
        btn = QPushButton(self)
        btn.setText("打开文件")
        btn.move(25,50)
        btn.clicked.connect(self.test)
        # 第二个按钮
        self.btn2 = QPushButton(self)
        self.btn2.setText("修改")
        self.btn2.move(25,100)
        self.btn2.clicked.connect(self.sort_data)

    def test(self):
        fd = QFileDialog.getOpenFileName(self, "选择一个txt文件", r"C:\Users\Administrator\Desktop\测试脚本\测试数据集", "txt(*.txt)")
        self.path = fd[0]
        self.lin.setText(self.path)

    def sort_data(self):
        try:
            if not self.path:
                em = QErrorMessage(self)
                em.setWindowTitle("错误提示")
                em.showMessage("请选择txt文件")
            # # 删除 null
            lines = [l for l in open(self.path, "r") if l.find("null", 0, 8) != 0]
            fd = open(self.path, "w")
            fd.writelines(lines)
            fd.close()
            # 排列成10个数据一行
            path2 = self.path.replace(".txt", "ss.txt")
            with open(self.path) as f1:
                cnames = f1.readlines()
                for i in range(0, len(cnames)):
                    cnames[i] = cnames[i].replace("\n", ",")
                    if i % 10 == 0 and i != 0:
                        cnames[i] = cnames[i].strip() + "\n"
            with open(path2, "w") as f2:
                f2.writelines(cnames)
        except BaseException as e:
            em = QErrorMessage(self)
            em.setWindowTitle("修改失败")
            em.showMessage("数据修改失败")
        else:
            em = QErrorMessage(self)
            em.setWindowTitle("修改成功")
            em.showMessage("数据修改成功")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())