from typing import List, Tuple
from random import shuffle


def get_name(x: Tuple[str, int]) -> str:
    return x[0]


def get_vote_count(x: Tuple[str, int]) -> int:
    return x[1]


def main() -> None:
    print('Type the options line by line. Enter empty line to finish.')
    k = 0
    options: List[Tuple[str, int]] = []
    # noinspection PyTypeChecker
    all_pairs: List[Tuple[str, str]] = []
    user_has_been_warned = False

    # Read options
    while True:
        line = input(f'{k + 1}: ')
        if not line:
            if k == 0:
                print('It wouldn\'t hurt if you used your keyboard. '
                      'Please enter at least one option.')
                continue
            break
        if line in map(get_name, options):
            if user_has_been_warned:
                print('What the fuck.')
            else:
                print('I assumed you already knew that you have to name '
                      'things differently. Try again with another name.')
                user_has_been_warned = True
            continue
        options.append((line, 0))
        k += 1

    option_count = len(options)

    # Generate pair list
    if option_count > 1:
        k = 0
        for opt1, _ in options:
            k += 1
            for opt2, _ in options[k:]:
                if opt1 == opt2:
                    print('[!] Repeated value found.')
                    continue
                pair = [opt1, opt2]
                shuffle(pair)
                # noinspection PyTypeChecker
                all_pairs.append(tuple(pair))
    else:
        all_pairs = [(options[0][0], options[0][0])]

    # Vote
    print('\nTime to vote!\nA pair of options will be prompted each time.')
    print('Enter a \'1\' to select the left option, \'2\' for right.')

    # The total count of pairs is (n * (n - 1)) / 2
    # but I use len() just in case
    pair_count = len(all_pairs)
    shuffle(all_pairs)

    k = 0
    user_has_been_warned = False
    while k < pair_count:
        opt1, opt2 = all_pairs[k]
        resp = input(f'=> {k + 1}/{pair_count}: {opt1} VS {opt2} ')
        if resp == '1':
            choice = opt1
        elif resp == '2':
            choice = opt2
        else:
            if user_has_been_warned:
                print('What the fuck.')
            else:
                print('I thought I was clear with my instructions. Enter '
                      '\'1\' or \'2\'.')
                user_has_been_warned = True
            continue
        for i, item in enumerate(options):
            if item[0] == choice:
                options[i] = (item[0], item[1] + 1)
                break
        k += 1

    options.sort(key=get_vote_count, reverse=True)

    print('\nResults:')
    for i, item in enumerate(options):
        print(f'{i + 1}: {item[0]} ({item[1]})')

    if option_count == 1:
        # Credits to Metracrepas for this one, it's amazing
        print('\nCongratulations, you compared one element to itself. Are you happy? '
              'Are you satisfied? Did you think it was funny? What the fuck did you '
              'expect? Go outside, touch some grass, watch a movie, call your mom. '
              'You\'re better than this.')
    elif option_count == 2:
        print('\nI admire your conviction of using technology to the advantage of '
              'humankind. However, I ponder, are you really aware of what it means to '
              'deliberately use a Python program to help your ass decide from a pool of '
              'no more than two options? Have you considered using your brain for this? '
              'Mind you that this script is a tool that breaks down the options into '
              'pairs, in order to ask for a preference in each pair. In other words, it '
              'is none other than YOU, THE USER who picks the winner in the end. I simply '
              'do not understand. Did you think I was going to evaluate the decision with '
              'a trained model, or something? The fact that you rely on this tool to '
              'throw out a result that you kind of already knew from the start is '
              'concerning. If I may, I advise you to please reconsider everything you\'ve '
              'done in your life so far.')


if __name__ == '__main__':
    main()
