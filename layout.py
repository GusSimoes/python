#layout.py


#github.com/pyqt/examples

#pip install pyqt5


def botao_clicado():
    alert=QMessageBox()
    alert.setText('Você clicou o botão!')
    alert.exec_()

from PyQt5.QtWidgets import * 

app = QApplication([])


btnAcima = QPushButton("Acima")
btnAcima.clicked.connect(botao_clicado)

btnAbaixo = QPushButton("Abaixo")
btnAbaixo.clicked.connect(botao_clicado)

layout = QVBoxLayout()
layout.addWidget(btnAcima)
layout.addWidget(btnAbaixo)

window = QWidget()
window.setLayout(layout)
window.show()

app.exec_()
