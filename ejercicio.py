def hanoi(n, source, target, auxiliary, moves):
    if n > 0:
        # Move n-l discs from source to auxiliary
        hanoi(n-1, source, auxiliary, target, moves)
        # Move the nth disc from source to target
        target.append(source.pop())
        moves.append((source.copy(), auxiliary.copy(), target.copy()))
        # Move the n-l discs from auxiliary to target
        hanoi(n-1, auxiliary, target, source, moves)
    # Initialize the towers and moves list
    A = [6,5,4,3,2,1] # Initial state for N = 6
    B = []
    C = []
    moves = [(A.copy(), B.copy(), C.copy())]
    # Run the recursive function
    hanoi(6, A, C, B, moves)
    # Print all moves
    for move in moves:
        print(f"A: {move[0]}, B: {move[1]}, C: {move[2]}")
    # Print the number of moves
    print(f"Number of moves: {len(moves)}")