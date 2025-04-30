from windows_toasts import Toast, WindowsToaster

toaster = WindowsToaster('Python')

newToast = Toast()

newToast.text_fields = ['Hello, world!']

newToast.on_activated = lambda _: print('Toast clicked!')

toaster.show_toast(newToast)