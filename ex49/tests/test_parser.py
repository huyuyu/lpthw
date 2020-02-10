from nose.tools import *

from src.parser import *

def test_get_type():
    test_list1 = [('verb', 'open'), ]

    assert_equal(get_type(test_list1), 'verb')

    test_list2 = [('', 'kill'), ('verb', 'open')]
    assert_equal(get_type(test_list2), '')

    test_list3 = [(None, None), ]
    assert_equal(get_type(test_list3), None)

def test_match():
    test_list1 = [
        ('verb', 'open'),
        ('stop', 'the'),
        ('noun', 'door'),
        ]

    assert_equal(match(test_list1, 'verb'),
                ('verb', 'open'))
    assert_equal(match(test_list1, 'stop'),
                 ('stop', 'the'))

    test_list2 = [(None, None), ]
    assert_equal(match(test_list2, 123),
                 None)
    assert_equal(test_list2, [])
    assert_equal(match(test_list2, 123),
                 "list Null")

def test_skip():
    test_list1 = [
        ('verb', 'open'),
        ('stop', 'the'),
        ('noun', 'door'),
        ]

    skip(test_list1, 'verb')

    assert_equal(test_list1[0], ('stop', 'the'))
    assert_equal(test_list1[0][0], 'stop')
    assert_equal(test_list1[0][0][0], 's')
    # 这里，我顺带测试了test_list1的第一层内部元素。很棒。

    test_list2 = [
        ('1', 'AAAA'),
        ('1', 'tDFWERhe'),
        ('noun', 'door'),
        ]

    skip(test_list2, '1')
    assert_equal(test_list2, [('noun', 'door'),])
    # 最后一个逗号加不加都一样。

    test_list3 = [
        ('2', 'AAAA'),
        ('1', 'tDFWERhe'),
        ('noun', 'door'),
        ]
    skip(test_list3, '1')
    assert_equal(test_list3[0], ('2', 'AAAA'))



def test_parse_verb():
    test_list1 = [
        ('stop', 'the'),
        ('verb', 'open'),
        ('noun', 'door'),
        ]

    assert_equal(parse_verb(test_list1),
                 ('verb', 'open'))

    assert_raises(ParserError, parse_verb, test_list1)
    # **本句含义为：让系统判断，parse_verb(test_list1)执行后
    #            是不是返回ParserError错误。

    # assert_raises参数详解：
    # 1参数：错误的类型，如本例中为片定义的ParserError
    # 2参数：你预计会出错的那个函数名。本例中，test_list1
    #       只剩下('noun', 'door')这一元素，按理运行parse_verb
    #       后肯定报错，所以将parse_verb放在2参数。注意别加括号！
    # 3、4、5参数：填入“预计会出错的那个函数，所需要的参数”。
    #       可拓展，与2参数实际需要的函数对应。
    # 现在你可以看懂上面标**的那句解释了。

    test_list2 = [
        ('noun', 'door'),
        ('a', 'b')
        ]
    assert_raises(ParserError, parse_verb, test_list2)

def test_parse_object():
    test_list1 = [
        ('noun', 'door'),
        ('direction', 'b')
        ]
    assert_equal(parse_object(test_list1), ('noun', 'door'))
    assert_equal(parse_object(test_list1), ('direction', 'b'))
    assert_raises(ParserError, parse_object, test_list1)

def test_parse_subject():
    test_list1 = [
        ('stop', 'the'),
        ('verb', 'open'),
        ('noun', 'door'),
        ]

    assert_equal(parse_subject(test_list1), ('noun', 'player'))
    parse_verb(test_list1)
    assert_equal(parse_subject(test_list1), ('noun', 'door'))
    assert_raises(ParserError, parse_subject, test_list1)

def test_parse_sentence():
    test_list1 = [
        ('stop', 'the'),
        ('verb', 'open'),
        ('noun', 'door'),
        ]

    sentence = parse_sentence(test_list1)
    assert_equal(sentence.subj,  'player')
    assert_equal(sentence.verb,  'open')
    assert_equal(sentence.obj,  'door')

    test_list2 = [
        ('verb', 'kill'),
        ('noun', 'you'),
        ('stop', 'and'),
        ('verb', 'eat'),
        ('noun', 'bear'),
    ]
    sentence2 = parse_sentence(test_list2)
    assert_equal(sentence2.subj, 'player')
    assert_equal(sentence2.verb, 'kill')
    assert_equal(sentence2.obj, 'you')

    sentence3 = parse_sentence(test_list2)
    assert_equal(sentence3.subj, 'player')
    assert_equal(sentence3.obj, 'bear')
