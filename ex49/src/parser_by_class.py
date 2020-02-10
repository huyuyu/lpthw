class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subj, verb, obj):
        self.subj = subj[1]
        self.verb = verb[1]
        self.obj = obj[1]

class Parse(object):
    def __init__(self, word_list):
        # self.sentence = Sentence()
        self.word_list = word_list

    def get_type(self):
        # 读取的类型，如：返回('nouns', 'door')中的'nouns'
        if  self.word_list:
            word =  self.word_list[0]
            #从元组构成的列表中取出第一个元组元素。
            return word[0]
            #从元组元素中返回第一个字符串
        else:
            return None

    def match(self, expecting):
        # 传入由多个元组构成的列表，查看第1个元组是不是expect想找的元组
        # 如果是，取走该元组。不是，则删除该元组
        if self.word_list:
            word = self.word_list.pop(0)
            # 读取列表中的第1个元素，这个元素是一个元组，如('nouns', 'door')。

            if word[0] == expecting:
                return word
                # 本例中，元组第1元素表示的是类型，
                # 如果这个类型是我们要找的类型，就把这个元组返回
            else:
                return None
                # 不管找没找到，都使word_list元素减少了1个
        else:
            return "list Null"

    def skip(self, word_type):
        # 从word_list中跳过word_type类型的元组，直到list的第1个元素不是word_type
        while self.get_type() == word_type:
            self.match(word_type)
            # 因为match总会pop掉一个元素，才使得这个函数得以成立
            # 换成pop(word_list.pop(0))更好
            # 但我感觉函数之前的相互依赖性又太强了。match做了匹配之外更多的事情。


    def get_verb(self):
        # 先跳过stop类的词组（无用但合法）,考察第1个元素是不是动词
        # 如果是，则取走；如果不是，不取走，报错。
        self.skip('stop')
        word_type = self.get_type()

        if word_type == 'verb':
            return self.match('verb')
            # 找到就取走
        else:
            raise ParserError("Expected a verb next.")

    def get_object(self):
        self.skip('stop')
        word_type = self.get_type()

        if word_type == 'noun':
            return self.match('noun')
        elif word_type == 'direction':
            return self.match('direction')
        else:
            raise ParserError("Expected a noun or direction next.")

    def get_subject(self):
        self.skip('stop')
        word_type = self.get_type()

        if word_type == 'noun':
            return self.match('noun')
        elif word_type == 'verb':
            return ('noun', 'player')
            # 当第1个词是动词是，默认地认为主语为player，也没有取走第1个元素
            # 这是合情合理的。
        else:
            raise ParserError("Expected a verb next.")

    def get_sentence(self):
        subj = self.get_subject()
        verb = self.get_verb()
        obj = self.get_object()

        return Sentence(subj, verb, obj)