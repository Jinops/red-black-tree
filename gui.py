import sys
import rbtree
from draw import draw
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from functools import partial

class MyApp(QWidget):
  def __init__(self, tree):
      super().__init__()
      self.rbtree = rbtree.RBTree() if tree is None else tree
      self.initUI()

  def initUI(self):
    grid = QGridLayout()
    self.setLayout(grid)
    self.setWindowTitle('Red-black Tree')
    self.setGeometry(300, 300, 300, 200)

    label_num = QLabel('Input a number below:')
    self.label_status = QLabel('Ready')
    self.edit_num = QLineEdit()
    btn_insert = QPushButton('&Insert', self)
    btn_delete = QPushButton('&Delete', self)
    btn_search = QPushButton('&Search', self)
    self.img_label = QLabel('tree')

    self.update_image_label()
    self.img_label.setFixedSize(500, 500)
    self.img_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
    self.img_label.setStyleSheet("background-color: white")

    self.label_status.setAlignment(Qt.AlignCenter)

    btn_insert.clicked.connect(partial(self.onclick, 'insert'))
    btn_delete.clicked.connect(partial(self.onclick, 'delete'))
    btn_search.clicked.connect(partial(self.onclick, 'search'))

    grid.addWidget(label_num, 0, 0)
    grid.addWidget(self.edit_num, 1, 0)
    grid.addWidget(btn_insert, 2, 0)
    grid.addWidget(btn_delete, 3, 0)
    grid.addWidget(btn_search, 4, 0)
    grid.addWidget(QLabel("<hr/>"), 5, 0)
    grid.addWidget(self.label_status, 6, 0)
    grid.addWidget(self.img_label, 0, 1, 30, 1)
    self.show()

  def onclick(self, value):
    num = self.edit_num.text()
    if not num.isdecimal():
       self.label_status.setText('Input number first!')
       return
    
    num = int(num)
    if value == 'insert':
      self.rbtree.insert(num)
    elif value == 'delete':
       pass # TODO
    elif value == 'search':
       pass # TODO
    else:
       return
    self.update_image_label()
    self.label_status.setText('{}: {}'.format(value, num))
    self.edit_num.clear()

  def update_image_label(self):
    draw(self.rbtree.root)
    self.img_label.setPixmap(QPixmap('data/tree.png'))

def run(rbtree):
  app = QApplication(sys.argv)
  ex = MyApp(rbtree)
  sys.exit(app.exec_())

if __name__ == "__main__":
    keys = [30, 20, 25, 40, 10, 35, 22, 13]
    rbtree = rbtree.make_tree(keys)
    run(rbtree)
