#-*- coding:utf8 -*-

def command():
    commands = {}

    def register(command):
        def _register(fn):
            if command in commands:
                raise Exception('command {} is exist'.format(command))
            commands[command] = fn # 把函数存储到commands字典的values中
            print(commands[command])
            return fn
        return _register

    def default_fn():
        print('command not found')

    def run():
        while True:
            cmd= input('<<')
            if cmd.strip() == 'quit':
                return
            commands.get(cmd.strip(),default_fn)()

    return register,run

register, run = command()

@register('haha') # 添加一条命令
def haha():
    print('haha')


run()