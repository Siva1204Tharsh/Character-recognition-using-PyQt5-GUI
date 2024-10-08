# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tamilRecogi.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# create first the ui file with pyuic5 and then run the script

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from keras.preprocessing import image
from keras.layers import Dense 
from keras.models import model_from_json 
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dropout
from keras.layers import BatchNormalization


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BrowseImage = QtWidgets.QPushButton(self.centralwidget)
        self.BrowseImage.setGeometry(QtCore.QRect(160, 370, 151, 51))
        self.BrowseImage.setObjectName("BrowseImage")
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(200, 80, 361, 261))
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 621, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Classify = QtWidgets.QPushButton(self.centralwidget)
        self.Classify.setGeometry(QtCore.QRect(160, 450, 151, 51))
        self.Classify.setObjectName("Classify")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 370, 111, 16))
        self.label.setObjectName("label")
        self.Training = QtWidgets.QPushButton(self.centralwidget)
        self.Training.setGeometry(QtCore.QRect(400, 450, 151, 51))
        self.Training.setObjectName("Training")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(400, 390, 211, 51))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BrowseImage.clicked.connect(self.loadImage)

        self.Classify.clicked.connect(self.classifyFunction)

        self.Training.clicked.connect(self.trainingFunction)

         
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BrowseImage.setText(_translate("MainWindow", "Browse Image"))
        self.label_2.setText(_translate("MainWindow", "Tamil CHARACTER RECOGNITION USING CNN"))
        self.Classify.setText(_translate("MainWindow", "Classify"))
        self.label.setText(_translate("MainWindow", "Recognized Class"))
        self.Training.setText(_translate("MainWindow", "Training"))


    def loadImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)") # Ask for file
        if fileName: # If the user gives a file
            print(fileName)
            self.file=fileName
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageLbl.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center

    def classifyFunction(self):
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("model.h5")
        print("Loaded model from disk")
        label=['1-A', '10-O', '100-No', '101-Noa', '102-Nou', '103-tha', '104-thaa', '105-thi', '106-thee', '107-thu', '108-thoo', '109-the', '11-Oa', '110-thae', '111-thai', '112-tho', '113-thoa', '114-thou', '115-nha', '116-nhaa', '117-nhi', '118-nhee', '119-nhu', '12-Ow', '120-nhoo', '121-nhe', '122-nhae', '123-nhai', '124-nho', '125-nhoa', '126-nhou', '127-pa', '128-paa', '129-pi', '13-k', '130-pee', '131-pu', '132-poo', '133-pe', '134-pae', '135-pai', '136-po', '137-poa', '138-pou', '139-ma', '14-nG', '140-maa', '141-mi', '142-mee', '143-mu', '144-moo', '145-me', '146-mae', '147-mai', '148-mo', '149-moa', '15-s(ch)', '150-mou', '151-ya', '152-yaa', '153-yi', '154-yee', '155-yu', '156-yoo', '157-ye', '158-yae', '159-yai', '16-Gn(nj)', '160-yo', '161-yoa', '162-you', '163-ra', '164-raa', '165-ri', '166-ree', '167-ru', '168-roo', '169-re', '17-t(d)', '170-rae', '171-rai', '172-ro', '173-roa', '174-rou', '175-la', '176-laa', '177-li', '178-lee', '179-lu', '18-N', '180-loo', '181-le', '182-lae', '183-lai', '184-lo', '185-loa', '186-lou', '187-va', '188-vaa', '189-vi', '19-tha', '190-vee', '191-vu', '192-voo', '193-ve', '194-vae', '195-vai', '196-vo', '197-voa', '198-vou', '199-zha', '2-Aa', '20-nh', '200-zhaa', '201-zhi', '202-zhee', '203-zhu', '204-zhoo', '205-zhe', '206-zhae', '207-zhai', '208-zho', '209-zhoa', '21-p', '210-zhou', '211-La', '212-Laa', '213-Li', '214-Lee', '215-Lu', '216-Loo', '217-Le', '218-Lae', '219-Lai', '22-m', '220-Lo', '221-Loa', '222-Lou', '223-Ra', '224-Raa', '225-Ri', '226-Ree', '227-Ru', '228-Roo', '229-Re', '23-y', '230-Rae', '231-Rai', '232-Ro', '233-Roa', '234-Rou', '235-na', '236-naa', '237-ni', '238-nee', '239-nu', '24-r', '240-noo', '241-ne', '242-nae', '243-nai', '244-no', '245-noa', '246-nou', '247-ak', '25-l', '26-v', '27-zh', '28-L', '29-R', '3-i', '30-n', '31-Ka', '32-Kaa', '33-Ki', '34-Kee', '35-Ku', '36-Koo', '37-Ke', '38-Kae', '39-Kai', '4-ee(ii)', '40-Ko', '41-Koa', '42-Kou', '43-nGa', '44-nGaa', '45-nGi', '46-nGee', '47-nGu', '48-nGoo', '49-nGe', '5-U', '50-nGae', '51-nGai', '52-nGo', '53-nGoa', '54-nGou', '55-sa', '56-saa', '57-si', '58-see', '59-su', '6-Oo(uu)', '60-soo', '61-se', '62-sae', '63-sai', '64-so', '65-soa', '66-sou', '67-Gna', '68-Gnaa', '69-Gni', '7-e(Ye)', '70-Gnee', '71-Gnu', '72-Gnoo', '73-Gne', '74-Gnae', '75-Gnai', '76-Gno', '77-Gnoa', '78-Gnou', '79-ta', '8-ae', '80-taa', '81-ti', '82-tee', '83-tu', '84-too', '85-te', '86-tae', '87-tai', '88-to', '89-toa', '9-ai', '90-tou', '91-Na', '92-Naa', '93-Ni', '94-Nee', '95-Nu', '96-Noo', '97-Ne', '98-Nae', '99-Nai']
        #label=["fifty","fivehundred","hundred","ten","twenty","twohundred"]
        path2=self.file
        print(path2)
        test_image = image.load_img(path2, target_size = (128, 128))        
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = loaded_model.predict(test_image)
        
        fresult=np.max(result)
        label2=label[fresult.argmax()]
        print(label2)
        self.textEdit.setText(label2)
    
    def trainingFunction(self):
        self.textEdit.setText("Training under process...")
        #basic cnn for tamil alphabet
        model = Sequential()
        model.add(Conv2D(32, kernel_size = (3, 3), activation='relu', input_shape=(128,128, 3)))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2D(96, kernel_size=(3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2D(32, kernel_size=(3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Dropout(0.2))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.3)) # over fitting  the prevention
        model.add(Dense(247, activation = 'softmax'))

        model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])



        train_datagen = ImageDataGenerator(rescale = None,
                                           shear_range = 0.2,
                                           zoom_range = 0.2,
                                           horizontal_flip = True)

        test_datagen = ImageDataGenerator(rescale = 1./255)

        training_set = train_datagen.flow_from_directory('E:\Data-----Science\DS AI DL ML Project for 30 Days\Character recognition using PyQt5 GUI\Dataset\Train',
                                                         target_size = (128, 128),
                                                         batch_size = 8,
                                                         class_mode = 'categorical')
        #print(test_datagen);
        labels = (training_set.class_indices)
        print(labels)
        

        test_set = test_datagen.flow_from_directory('E:\Data-----Science\DS AI DL ML Project for 30 Days\Character recognition using PyQt5 GUI\Dataset\Test',
                                                    target_size = (128, 128),
                                                    batch_size = 8,
                                                    class_mode = 'categorical')

        labels2 = (test_set.class_indices)
        print(labels2)
        #self.textEdit.setText(labels2)

        model.fit(training_set,
                            steps_per_epoch = 100,
                            epochs = 10,
                            validation_data = test_set,
                            validation_steps = 125)


       # Part 3 - Making new predictions

        model_json=model.to_json()
        with open("model.json", "w") as json_file:
           json_file.write(model_json)
       # serialize weights to HDF5
           model.save("model.h5")
           print("Saved model to disk")
           self.textEdit.setText("Saved model to disk")
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
