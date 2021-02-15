# 校长一再强调，胸前除了校徽别别别的
# 小龙女来到了杨过小时候生活的地方，深情地说：我也想过过过过过过的生活
# vim pycharm
# 2019年横扫天下的Transformer,迁移学习

# ############################################################
#                           文本预处理                         #
# ############################################################
# 文本处理的基本方法：分词 词性标注 命名实体识别
# 文本张量表示方法： one-hot         Word2vec           Word Embedding
# 文本语料的数据分析： 标签数量分布  句子长度分布   词频统计与关键词词云
# 文本特征处理： 添加n-gram特征  文本长度规范
# 数据增强方法： 回译数据增强法

import jieba
content = "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
jieba.cut(content, cut_all=False)  # cut_all默认为False,精确模式分词 将返回一个生成器对象<generator object.Tokenizer.cut at 0x7f065c19e318>
# 若需直接返回列表内容，使用jieba.lcut
jieba.lcut(content, cut_all=False)

jieba.cut(content, cut_all=True) # 全模式分词
jieba.lcut(content, cut_all=True)

jieba.cut_for_search(content)   # 在精确模式的基础上，对长词再次切分，提高召回率
jieba.lcut_for_search(content)

# 中文繁体分词
content1 = "煩惱即是菩提，我暫且不提"
jieba.lcut(content1)   # 默认精确模式

#####         使用自定义词典，一行三部分
# 词语 词频（可省略） 词性（可省略）
#    云计算 5 n
#  将该词典存为userdict.txt


# >>> import hanlp
# >>> tokenizer = hanlp.load('CTB6_CONVSEG')
# >>> tokenizer("工信处...")

# >>> tokenizer = hanlp.utils.rules.tokenize_english
# >>> tokenizer("Mr...")

# 命名实体：专有名词，    如周杰伦，黑山县，孔子学院
# Named Entity Recognition 就是识别出一段文本中可能存在的命名实体

# 中文命名实体识别
# import hanlp
# >>> recognizer = hanlp.load(hanlp.pretrained.ner.MSRA_NER_BERT_BASE_ZH)
# >>> list('上海华安工业（集团）公司董事长谭旭光和秘书张晚霞来到美国纽约现代艺术博物馆参观。')
# >>> recognizer(list('上海华安工业（集团）公司董事长谭旭光和秘书张晚霞来到美国纽约现代艺术博物馆参观。'))

# 英文命名实体识别
# >>> import hanlp
# >>> recognizer = hanlp.load(hanlp.pretrained.ner.CONLL03_NER_BERT_BASE_UNCASED_EN))
# >>> recognizer(["President", "Obama", "is", "speaking", "at", "the", "White", "House"])

# 使用jieba进行中文词性标注(Part-Of-Speech tagging)
# >>> import jieba.posseg as pseg
# >>> pseg.lcut("我爱北京天安门")

# 使用hanlp进行中文词性标注
# 使用hanlp进行英文词性标注
# >>> import hanlp
# >>> tagger = hanlp.load(hanlp.pretrained.pos.PTB_POS_RNN_FASTTEXT_EN)
# >>> tagger(['I', 'banked', '2', 'dollars', 'in', 'a', 'bank', '.'])
