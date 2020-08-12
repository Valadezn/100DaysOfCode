# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RandomMenuDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QUrl
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

from recipeClass import Recipe



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.random_recipe_button = QtWidgets.QPushButton(self.centralwidget)
        self.random_recipe_button.setGeometry(QtCore.QRect(290, 10, 181, 51))
        self.random_recipe_button.setObjectName("random_recipe_button")
        self.left_group_box = QtWidgets.QGroupBox(self.centralwidget)
        self.left_group_box.setGeometry(QtCore.QRect(10, 60, 361, 501))
        self.left_group_box.setObjectName("left_group_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left_group_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.recipe_image = QtWidgets.QLabel(self.left_group_box)
        self.recipe_image.setText("")
        self.recipe_image.setObjectName("recipe_image")
        self.verticalLayout.addWidget(self.recipe_image)
        self.recipe_name_label = QtWidgets.QLabel(self.left_group_box)
        self.recipe_name_label.setObjectName("recipe_name_label")
        self.verticalLayout.addWidget(self.recipe_name_label)
        self.category_label = QtWidgets.QLabel(self.left_group_box)
        self.category_label.setObjectName("category_label")
        self.verticalLayout.addWidget(self.category_label)
        self.ingredients_label = QtWidgets.QLabel(self.left_group_box)
        self.ingredients_label.setText("")
        self.ingredients_label.setObjectName("ingredients_label")
        self.verticalLayout.addWidget(self.ingredients_label)
        
        #self.yt_viewer_label = QtWidgets.QLabel(self.left_group_box)
        #self.yt_viewer_label.setText("")
        #self.yt_viewer_label.setObjectName("yt_viewer_label")
        
        self.yt_viewer = QtWebEngineWidgets.QWebEngineView()
        self.yt_viewer.setObjectName("yt_viewer")
       
        self.verticalLayout.addWidget(self.yt_viewer)
        self.instructions_label = QtWidgets.QLabel(self.centralwidget)
        self.instructions_label.setGeometry(QtCore.QRect(390, 80, 381, 481))
        self.instructions_label.setText("")
        self.instructions_label.setObjectName("instructions_label")
        self.instructions_label.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.random_recipe_button.clicked.connect(self.getRecipe)
        self.new_recipe = Recipe()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.random_recipe_button.setText(_translate("MainWindow", "Get New Random Recipe!"))
        self.left_group_box.setTitle(_translate("MainWindow", "GroupBox"))
        self.recipe_name_label.setText(_translate("MainWindow", "Here"))
        self.category_label.setText(_translate("MainWindow", "Here"))

    def getRecipe(self):
        self.new_recipe.getNewRecipe()
        
        # Set name of recipe
        self.recipe_name_label.setText(self.new_recipe.get_name())
        
        self.category_label.setText(self.new_recipe.get_category())
        self.instructions_label.setText(self.new_recipe.get_instructions())
        
        # Set up YT video
        # TODO: edit youtube url to only get the 11 characters from the end of th eyoutube url
        s = """<iframe width="560" height="315" src="https://www.youtube.com/embed/L0MK7qz13bU?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>""".format(self.new_recipe.get_yt_url()[])
        print(s)
        base_url = "local"
        self.yt_viewer.setHtml(s, QUrl(base_url))
        
        # Set recipe thumbnail
        self.recipe_image.setPixmap(QtGui.QPixmap(self.new_recipe.get_thumbnail()))
        
        self.recipe_name_label.adjustSize()
        self.category_label.adjustSize()
        self.instructions_label.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #MainWindow.yt_viewer.show()
    sys.exit(app.exec_())