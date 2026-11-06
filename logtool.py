import random #导入随机模块

levels=['INFO','WARNING','ERROR']
msgs=[
    '用户登录成功',
    '数据库连接超时',
    '缓存未命中',
    '接口返回 500',
    '任务执行完成',
    '配置加载失败'
]
with open('sample.log','w',encoding='utf-8') as f:
    for i in range(1,51):
        lv=random.choice(levels)  #把levels中的元素随机一个分配到lv
        msg=random.choice(msgs)   #把msgs中的元素随机一个分配到msg
        f.write(f'2026-11-02 14:{i:02d}:00[{lv}]{msg}\n')  #for循环遍历取值，i:02d(01--02--03...),然后再把lv和msg随机的数据引进并换行
print('已生成 sample.log')
# import random:导入随机模块
# random.choice():括号内的数据(levels)随机挑一个赋予变量lv


total = 0
i1 = 0
w1 = 0
e1 = 0
with open('sample.log','r',encoding='utf-8') as f:
    for i in f:
        total+=1
        i=i.strip()
        level=i.split('[')[1].split(']')[0]
        #使用split指定'['进行切除创建列表，并且选中下标为1的元素再进行']'切除并且选中下标为0的元素
        if level=='INFO':
            i1+=1
        elif level=='WARNING':
            w1+=1
        elif level=='ERROR':
            e1+=1
print(f'总行数:{total}')
print(f'INFO:{i1}')
print(f'WARNING:{w1}')
print(f'ERROR:{e1}')

with open('sample.log','r',encoding='utf-8') as old_f,open('report.txt','w',encoding='utf-8') as f:
    print(f'->共{e1}条ERROR:')
    for line in old_f:
        line=line.strip()
        lv=line.split('[')[1].split(']')[0]
        if lv == 'ERROR':
            f.write(f'{line}\n')
            print(f'->{line}')
print('->报告已写入report.txt')
