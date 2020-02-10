from nose.tools import *

from src.parser_by_class import *

def test_get_type():
    test_list1 = [('verb', 'open'), ]
    list1 = Parse(test_list1)
    assert_equal(list1.get_type(), 'verb')

    test_list2 = [('', 'kill'), ('verb', 'open')]
    list2 = Parse(test_list2)
    assert_equal(list2.get_type(), '')

    test_list3 = [(None, None), ]
    list3 = Parse(test_list3)
    assert_equal(list3.get_type(), None)

def test_match():
    test_list1 = [
        ('verb', 'open'),
        ('stop', 'the'),
        ('noun', 'door'),
        ]
    list1 = Parse(test_list1)

    assert_equal(list1.match('verb'),
                 ('verb', 'open'))
    assert_equal(list1.match('stop'),
                 ('stop', 'the'))

    test_list2 = [(None, None), ]
    list2 = Parse(test_list2)
    assert_equal(list2.match(123),
                 None)
    assert_equal(list2.word_list, [])
    assert_equal(list2.match(123),
                 "list Null")

def test_skip():
    test_list1 = [
        ('verb', 'open'),
        ('stop', 'the'),
        ('noun', 'door'),
        ]
    list1 = Parse(test_list1)
    list1.skip('verb')

    assert_equal(test_list1[0], ('stop', 'the'))
    assert_equal(test_list1[0][0], 'stop')
    assert_equal(test_list1[0][0][0], 's')
    # 这里，我顺带测试了test_list1的第一层内部元素。很棒。

    test_list2 = [
        ('1', 'AAAA'),
        ('1', 'tDFWERhe'),
        ('noun', 'door'),
        ]
    list2 = Parse(test_list2)

    list2.skip('1')
    assert_equal(test_list2, [('noun', 'door'),])
    # 最后一个逗号加不加都一样。

    test_list3 = [
        ('2', 'AAAA'),
        ('1', 'tDFWERhe'),
        ('noun', 'door'),
        ]
    list3 = Parse(test_list3)
    list3.skip('1')
    assert_equal(test_list3[0], ('2', 'AAAA'))
    assert_equal(list3.word_list[0], ('2', 'AAAA'))

def test_get_verb():
    test_list1 = [
        ('stop', 'the'),
        ('verb', 'open'),
        ('noun', 'door'),
        ]
    list1 = Parse(test_list1)

    assert_equal(list1.get_verb(),
                 ('verb', 'open'))

    assert_raises(ParserError, list1.get_verb)

    test_list2 = [
        ('noun', 'door'),
        ('a', 'b')
        ]
    list2 = Parse(test_list2)
    assert_raises(ParserError, list2.get_verb)

def test_get_object():
    test_list1 = [
        ('noun', 'door'),
        ('direction', 'b')
        ]
    list1 = Parse(test_list1)

    assert_equal(list1.get_object(), ('noun', 'door'))
    assert_equal(list1.get_object(), ('direction', 'b'))
    assert_raises(ParserError, list1.get_object)

def test_get_subject():
    test_list1 = [
        ('stop', 'the'),
        ('verb', 'open'),
        ('noun', 'door'),
        ]
    list1 = Parse(test_list1)

    assert_equal(list1.get_subject(), ('noun', 'player'))
    list1.get_verb()
    assert_equal(list1.get_subject(), ('noun', 'door'))
    assert_raises(ParserError, list1.get_subject)

def test_get_sentence():
    test_list1 = [
        ('stop', 'the'),
        ('verb', 'open'),
        ('noun', 'door'),
        ]
    list1 = Parse(test_list1)
    # sentence = test_list1.get_sentence
    sentence = list1.get_sentence()
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
    list2 = Parse(test_list2)

    sentence2 = list2.get_sentence()
    assert_equal(sentence2.subj, 'player')
    assert_equal(sentence2.verb, 'kill')
    assert_equal(sentence2.obj, 'you')

    # 下面针对list2 继续操作。
    sentence3 = list2.get_sentence()
    assert_equal(sentence3.subj, 'player')
    assert_equal(sentence3.obj, 'bear')