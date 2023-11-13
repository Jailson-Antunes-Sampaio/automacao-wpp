# import tkinter as tk

# def criar_notificacao():
#     root = tk.Tk()
#     root.title("Notificação")
#     label = tk.Label(root, text="Clique na notificação")
#     label.pack()

#     def fechar_notificacao():
#         print("Robo")
#         root.destroy()

#     label.bind("<Button-1>", lambda e: fechar_notificacao())
#     root.mainloop()

# # Simulando o recebimento de uma notificação
# criar_notificacao()


import time
# from windows_toasts import Toast, WindowsToaster

# # def click():
# #     print("robo")
# #     time.sleep(10)

# # toaster = WindowsToaster('Python')
# # newToast = Toast()
# # newToast.text_fields = ['Hello, world!']

# # newToast.onactivated = lambda : click()
# # toaster.show_toast(newToast)
# # time.sleep(5)



# from win10toast import ToastNotifier
# toaster = ToastNotifier()
# toaster.show_toast("Hello World!!!",
#                    "Python is 10 seconds awsm!",
#                    icon_path=None,
#                    duration=10)

# toaster.show_toast("Example two",
#                    "This notification is in it's own thread!",
#                    icon_path=None,
#                    duration=5,
#                    threaded=True)
# # Wait for threaded notification to finish
# while toaster.notification_active(): time.sleep(0.1)

from win10toast_click import ToastNotifier

def open_notification():
    print("clicou na notificação")

toaster = ToastNotifier()

toaster.show_toast(
    "Execução robo",  # title
    "Ataquem sigi!",  # message
    icon_path=None,  # 'icon_path'
    duration=10,  # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True,  # True = run other code in parallel; False = code execution will wait till notification disappears
    callback_on_click=open_notification  # click notification to run function
)
