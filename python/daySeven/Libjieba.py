'''
jieba 库 -- 中文切割工具包
'''
import jieba as jb
ls = jb.lcut("中华人民共和国是伟大的。")  # 能够切分出每个词，但是有些词可以在进行切分
print("精准模式：",ls)

ls = jb.lcut("中华人民共和国是伟大的。", cut_all=True) # 全模式是可以切出最多的词语
print("全模式：", ls)

ls = jb.lcut_for_search("中华人民共和国是伟大的") # 按搜索方式进行的切分模式
print("搜索模式： ", ls)