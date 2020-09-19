"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime



###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    paragraphs = [paragraphs[i] for i in range(len(paragraphs)) if select(paragraphs[i])]
    if k > len(paragraphs) - 1:
        return ''
    else:
        return paragraphs[k]
        
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def help(p):
        # p = p.split(' ')
        p = lower(remove_punctuation(p))
        for word in p.split():
            if word in topic:
                return True
        return False
        # p = p.split(' ')
        # for element in topic:
        #     if ''+element+*  in lower(p):
        #         return True
        # return False

    return help
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***" # although passed, not graceful
    count = 0
    l1 = len(typed_words)
    l2 = len(reference_words)
    if l1 <= l2:
        l = l1
    else:
        l = l2
    for i in range(l):
        # print(typed_words)
        if typed_words[i] == reference_words[i]:
            count += 1
    if l1 == 0 or l2 == 0:
        return 0.0
    return count * 100 / len(typed_words) 
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 / elapsed * 60
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5 # 
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        valid = [[index,word] for index,word in enumerate(valid_words) if diff_function(user_word, word, limit) <= limit]
        diff = [diff_function(user_word, word[1], limit) for index,word in enumerate(valid)]
        # print(valid)
        # print(diff)
        if not valid: 
            return user_word
        # print(min(diff))
        # print(valid)
        # print(diff)
        return valid[diff.index(min(diff))][1]



    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    start = list(start)
    goal = list(goal)
    l_diff = abs(len(start) - len(goal))
    def helper(start, goal, count, limit, l_diff):
        if count > limit:
            return count
        elif len(start) == 0 or len(goal) == 0:
            return l_diff
        elif start[0] != goal[0]:
            return 1 + helper(start[1:], goal[1:], count + 1, limit, l_diff)
        else:
            return helper(start[1:], goal[1:], count, limit, l_diff)

    return  helper(start, goal, 0, limit, l_diff)

    # l_start = len(start)
    # l_goal = len(goal)
    # l_min = min(l_start,l_goal)
    # st = list(start)
    # go = list(goal)
    # if l_start == l_goal:
    #     count = 0
    #     for i in range(l_min):
    #         if st[i] != go[i]:
    #             count += 1
    #     return count
    # else:
    #     count = 0
    #     for i in range(l_min):
    #         if st[i] != go[i]:
    #             count += 1
    #     return  count + abs(l_start - l_goal)
    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'
    '''i want to edit word from start to goal form, at first, ican compute the num_diff 
    as finally it have to be used. 也即是说缺多少就必须补多少，多多少就必须删多少，再看不多不少的那一部分
    如果每个字母都有，'''
    start = list(start)
    goal  = list(goal)
    l_diff = abs(len(start) - len(goal))
    if start in goal:
        return len(goal) - len(start)
    def helper(start, goal, limit, count, l_diff):
        st = list(start)
        go = list(goal)
        l_s = len(st)
        l_g = len(go)
        # if st[0] != 

    # if start in goal : # Fill in the condition
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"

    #     return 0
    #     # END

    # elif start in goal: # Feel free to remove or add additional cases
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"

    #     # END

    # else:
    #     add_diff = ...  # Fill in these lines
    #     remove_diff = ... 
    #     substitute_diff = ... 
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    count = 0
    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            count += 1
        else:
            break
    # print(count)
    # print(prompt)
    progress = count / len(prompt) 
    info = {'id': id, 'progress': progress}
    send(info)
    return progress

 
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)