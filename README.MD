# customized_jieba使用说明

## 简介
~~中文文本处理中常常需要对长文本进行分词。但是默认的jieba在特定领域的分词效果并不佳。  
除了通过设定用户词典外，对给定语料进行统计重新生成hmm模型，可以进一步提高jieba分词在该特定领域的分词效果。~~  

需要用cgo在目标机器上对gojieba进行编译，不如直接用cppjieba编译动态库。  
通过反推hmm模型的参数来做客制化，效率不够高。  
日后还是自己编写一个vocab+CRF的分词插件为好。  
  
~~- 更改自[gojieba](https://github.com/yanyiwu/gojieba)~~  
~~- 用户词典相同时，效果和python原生jieba效果相同，性能提高~~  
~~- 根据用户词典重新统计hmm模型数据后，效果略优于原版jieba（具体可看对比测试）~~   

## 文件结构
```
...
|
|--cfgdata                          -config data文件夹
|    |--dict                        -jieba会用到的dict文件夹
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
|--cfgdata_coreword.txt             -对比测试中python_jieba用到的用户词典
|
|--README.MD 
|
|--test1.py                         -对比测试1
|
|--test2.py                         -对比测试2    
```

## 对比测试

### 测试1
    pyjieba：设定用户词典

    cus_jieba：设定用户词典，用该词典训练hmm模型

### 测试2
    pyjieba：不做任何改动（调用了默认的字典）

    cus_jieba：设定用户词典，用该词典训练hmm模型

### 数据来源
    25条长短不一的商品名称

### 测试结果
    cus_jieba的效果要明显优于默认pyjieba（因为用户词典的效果），略微优于更改词典后的jieba（因为自己重新生成的hmm模型）。

    cus_jieba的运行速度大约是pyjieba的8~10倍。
    
    举例：
    输入： 小米8全网通版内存蓝色
    python jieba： ['小米', '8', '全', '网通', '版', '内存', '蓝色']
    python jieba + set_dictionary：  ['小米', '8', '全网', '通版', '内存', '蓝色']
    cus_jieba(set_dictionary + generate hmm model): ['小米', '8', '全网通版', '内存', '蓝色']
    

## 使用说明
    test文件中已经有调用的范例。但是也有注意点。
    1. cus_jieba读取dict的路径是相对路径。它读取的是运行程序当前目录中的cfgdata/dict/... 因此cfgdata和dict不能更改。如果这样的设定不够方便，以后可以再更改。
    2. jieba.dict.utf8中，每一行的末尾有一个“n”。其实是词性标注。用于原来jieba中词性标注等功能。但是当前nlp中这些人物通常是后续的dl处理的，因此直接都标了n.  
    3. modelus文件夹的名字是可以改的，和正常编程时一样。
