
import frida

#1  获取设备信息  必须手机端启动了frida-server并且做了端口转发
rdev = frida.get_remote_device()

# 2 枚举所有的进程
# processes = rdev.enumerate_processes()
# for process in processes:
#     print(process)


# 3 打印出前台在运行的app
front_app = rdev.get_frontmost_application()
print(front_app)
# Application(identifier="com.topjohnwu.magisk", name="Magisk", pid=23019, parameters={})
# Application(identifier="com.anhuitong.manage", name="爱学生", pid=24988, parameters={})
# 会使用，包名和应用名