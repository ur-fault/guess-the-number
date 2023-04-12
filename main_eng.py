while (inp := input('1 - guess the number\n2 - think of a number\n3 - exit\n> ').lower()) != '3':
	if inp == ('1', guess_count := 0)[0]:
		from random import randint; num = randint(1, 100)
		while (guess := input('your tip: ')) != str(num):
			try: print(f'number is smaller' if int(guess) > num else 'number is larger'); guess_count += 1
			except ValueError: print(f'"{guess}" is not an integer'); guess_count -= 1
	if inp == ('2', window := (1, 100), guess_count := 0)[0]:
		while (ans := input(f'I guess {(window[0] + window[1]) // 2}, is the number "smaller", "bigger" or "right"? ').lower()) != 'right':
			guess_count += 1; window = (window[0], (window[0] + window[1]) // 2) if ans == 'smaller' else ((window[0] + window[1]) // 2, window[1]) if ans == 'bigger' else (window, print(f'expected: "smaller", "bigger", "right"'), guess_count := guess_count - 1)[0]
	if inp in ('1', '2'): print(f'right, the number of attempts: {guess_count}')