class Function:
    def __init__(self, x_limit, text='',f_str=None, f=None):
        if f is None and f_str is not None:
            self.f = None
            self.f_str = f_str
        # 使用函数原型作为参数
        else:
            self.f = f
            self.f_str = None
        self.x_limit = x_limit
        self.text = text
