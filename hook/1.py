import frida
import sys

### 以后这个代码不需要动### ### ###
rdev = frida.get_remote_device()
session = rdev.attach("车智赢+")  # 写上要hook的app的名字
### 以后这个代码不需要动### ###



# 要改动的地方,js语法
scr = """
Java.perform(function () {
    //找到类 反编译的首行+类名：com.autohome.ahkit.utils下的
    var SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");
    
    //替换类中的方法，方法有几个参数，就要传几个参数
    SecurityUtil.encodeMD5.implementation = function(str){
        console.log("参数：",str); // 传入的参数打印了，我们猜是明文密码
        var res = this.encodeMD5(str); //调用原来的函数
        console.log("返回值：",res);  // 打印出正常执行这个方法，返回的结果
        return str; // 通过hook技术--》把传入的明文，直接返回--》抓包抓到的密码就是明文
    }
});
"""



####下面代码完全不需要动
script = session.create_script(scr)
def on_message(message, data):
    print(message, data)
script.on("message", on_message)
script.load()
sys.stdin.read()



'''

参数： 1234567
返回值： fcea920f7412b5da7be0cf42b8c93759  
抓包抓到的密码，一定是：fcea920f7412b5da7be0cf42b8c93759
 
'''