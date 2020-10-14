conftest.py ~~中的driver 承载整个会话的句柄，保证整个会话是同一个句柄，不会出现打开两个浏览器的情况
        method 方法继承dirver，将drvier修饰成一个类变量~~ 
        不能讲driver放在conftest中，否则后续类似于dirver的其他方法封装必须吧封装方法当成一个测试用例去执行
        
        将一些公共的测试用例放在conftest中，例如登录的cookie存放，登录等公共用例。
basemethod  对selenium中的find方法进行二次封装
