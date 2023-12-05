import sys
from PyQt5.QtWidgets import QApplication
from Manager import ManagerView

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = ManagerView()
        window.setupUi(window)  # Llama a setupUi para configurar la interfaz
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error in main: {str(e)}")