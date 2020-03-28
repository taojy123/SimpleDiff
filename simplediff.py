
import os
import time


if not os.path.isdir('target'):
    print('请将要比对的 .txt 文件放到 target 目录中')


filenames = os.listdir('target')

names = []
for filename in filenames:
    if filename.endswith('.txt'):
        names.append(filename)

if not len(names):
    print('请在 target 目录中放入两个 .txt 文件')


path1 = os.path.join('target', names[0])
path2 = os.path.join('target', names[1])

lines1 = open(path1).readlines()
lines2 = open(path2).readlines()

lines1 = [line.strip() for line in lines1]
lines2 = [line.strip() for line in lines2]


total = len(lines1) + len(lines2)

print('--------')
diffs1 = []
i = 0
for line in lines1:
    i += 1
    if line not in lines2:
        diffs1.append((i, line))

    percent = int(100 * i / total)
    b = int(percent / 4)
    w = 25 - b
    print('\b' * 100, end='', flush=True)
    print('█' * b, end='', flush=True)
    print('░' * w, end='', flush=True)
    time.sleep(0.001)

diffs2 = []
i = 0
for line in lines2:
    i += 1
    if line not in lines1:
        diffs2.append((i, line))

    percent = int(100 * (i + len(lines1)) / total)
    b = int(percent / 4)
    w = 25 - b
    print('\b' * 100, end='', flush=True)
    print('█' * b, end='', flush=True)
    print('░' * w, end='', flush=True)
    time.sleep(0.001)


print()
print('======== 对比完成，报告差异内容 ========')

if diffs1:
    print(path1, '中')
    for i, line in diffs1:
        print('第', i, '行:\t', line)

if diffs2:
    print(path2, '中')
    for i, line in diffs2:
        print('第', i, '行:\t', line)


if not diffs1 and not diffs2:
    print('两文件内容一致')



input()

