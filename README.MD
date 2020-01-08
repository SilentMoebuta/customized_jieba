# _jieba使用说明

## 效果简介
- 更改自cppjieba
- 用户词典相同时，效果和原版jieba完全一样，速度快8倍
- 根据用户词典重新统计hmm模型数据后，效果略优于原版jieba（具体可看对比测试）

## 文件结构
```
...
|
|--cfgdata                          -config data文件夹
|    |--dict                        -jieba会用到的dict文件夹
|        |--original_file_backup    -备份原版词典和hmm模型的文件夹
|        |--hmm_model.utf8          -由jieba.dict.utf8生成的hmm模型
|        |--jieba.dict.utf8         -jieba调用的词典，可以换成自己的
|        |--re_gen_hmm.py           -根据词典生成hmm模型的py程序
|        |--...                     -jieba其他功能用到的文件
|
|--modules                          -modules文件夹
|    |--jieba.dll                   -jieba.dll
|    |--jieba.h                     -jieba的头文件
|    |--jieba.py                    -封装dll的py文件
|
|--cfgdata_coreword.txt             -测试中用到的用户词典
|
|--README.MD 
|
|--test.py                          -对比测试1
|
|--test1.py                         -对比测试2    
```

## 对比测试

### 测试1
    pyjieba：设定用户词典

    _jieba：设定用户词典，用该词典训练hmm模型

### 测试2
    pyjieba：不做任何改动（调用了默认的字典）

    _jieba：设定用户词典，用该词典训练hmm模型

### 数据来源
    从新疆商品品名学习的反馈数据中，抽取25条长短不一的品名进行测试。

### 测试结果
    _jieba的效果要明显优于默认pyjieba（因为用户词典的效果），略微优于更改词典后的jieba（因为自己重新生成的hmm模型）。

    _jieba的运行速度大约是pyjieba的8~10倍。

    详细可见表格文件。

## 使用说明
    test文件中已经有调用的范例。但是也有注意点。
    1. _jieba读取dict的路径是相对路径。它读取的是运行程序当前目录中的cfgdata/dict/... 因此cfgdata和dict不能更改。如果这样的设定不够方便，以后可以再更改。
    2. jieba.dict.utf8中，每一行的末尾有一个“n”。其实是词性标注。不用管它就行了。因为原本的数据还标注了不同的词性，是用来做词性标注的。因为给自定义词典标词性也不太现实，全部标“n”就可以了。 
    3. modelus文件夹的名字是可以改的，和正常编程时一样。

## 作者
```
    cppjieba作者
    https://github.com/yanyiwu/cppjieba
```