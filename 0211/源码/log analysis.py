def extract(line):
    ret = []
    tmp = []
    split = True
    names = ['remot', '', '', 'time', 'requst', 'status', 'length', '', 'ua'] #日志文件分为九个部分，每个部分对应的名字
    for c in line:
        if c == '[':
            split = False
            continue # [后面空格不作为分割符
        if c == '"':
            split = not split
            continue # "之间空格不作为分割符
        if c == ']':
            split = True
            continue # ]之后的空格作为分割符
        if c == ' ' and split:
            ret.append(''.join(tmp)) # 把空格之间的数据添加到ret中，等待返回
            tmp.clear()
        else:
            tmp.append(c) # 非空格字符保存到tmp中，等待添加到ret中
    ret.append(''.join(tmp)) # 把tmp中剩余的数据添加到ret中
    result = {}
    for i, name in enumerate(names): # 把数据和名字对应起来存入字典中
        result[name] = ret[i]
    result.pop('', None) # 删除key  ''
    return result # 返回结果
