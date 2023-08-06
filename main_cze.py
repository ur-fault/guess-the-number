while (inp := input('1 - hádej číslo\n2 - mysli na číslo\n3 - exit\n> ').lower()) != '3':
	if inp == ('1', guess_count := 0)[0]:
		from random import randint; num = randint(1, 100)
		while (guess := input('tvůj tip: ')) != str(num):
			try: print(f'číslo je menší' if int(guess) > num else 'číslo je větší'); guess_count += 1
			except ValueError: print(f'"{guess}" není celé číslo'); guess_count -= 1
	if inp == ('2', window := (1, 100)):
		while (ans := input(f'hádám {(window[0] + window[1]) // 2}, je číslo "menší", "větší" nebo "správně"? ').lower()) != 'správně':
			guess_count += 1; window = (window[0], (window[0] + window[1]) // 2) if ans == 'menší' else ((window[0] + window[1]) // 2, window[1]) if ans == 'větší' else (window, print(f'očekávano: "menší", "větší", "správně"'), guess_count := guess_count - 1)[0]
	if inp in ('1', '2'): print(f'správně, počet pokusů: {guess_count}')
