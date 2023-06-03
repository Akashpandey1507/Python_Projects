a = input('Enter the 1st name of participate: ') # Where is a means Participant1
b = input('Enter the 2nd name of participate: ') # Where is a means Participant2
print(f'There is the 2 Candidates as {a} and {b}') # print

# voter ID
voter = [1,2,3,4,5,6]

# Length of Voter
lenOfVoter = len(voter)

# Counting vote for both candidates after complete the election
aVote = 0
bVote = 0

while True:
    if voter == []: 
        print('Voting has ended')
        # condtions, if candidate1  has more than candidate 2
        if aVote > bVote: 
            print(f'Congratulations the {a} has won the elections with {aVote} Votes')
            break
        # condtions, if candidate2  has more than candidate 1
        elif bVote>aVote:
            print(f'Congratulations the {b} has won the elections with {bVote} Votes')
            break
        # The both candidate get equal votes
        elif aVote==bVote:
            print(f'Congratulations the both candidate {a} and {b} has gotten equal votes')
            break

        # verify voter id
    ask_Voter_ID = int(input('Tell me your Voter ID: ')) 
    # check voter id availability
    if ask_Voter_ID in voter:
        print('you are eligible for voting')
        voter.remove(ask_Voter_ID)
        choose = input(f'''
Press 1 for {a} and 
Press 2 for {b}
''')

        # Voting
        if choose == '1':
            aVote += 1
            print(f'''You'r voting for {a}.''')
        elif choose =='2':
            bVote += 1
            print(f'''You'r voting for {b}.''')
        elif choose > '2':
            print(f'''Invalid Voter ID No.''')