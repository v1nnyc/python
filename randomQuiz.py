#! python3
# randomQuiz.py

import random
import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
	test = open('/Users/VINCENT/desktop/test%s.txt' % quizNum, 'w')
	ans = open('/Users/VINCENT/desktop/ans%s.txt' % quizNum, 'w')

	test.write('Name:\n\nDate:\n\nPeriod: \n\n')
	test.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
	test.write('\n\n')

	states = list(capitals.keys())
	random.shuffle(states)

	for questionNum in range(50):
		correctAnswer = capitals[states[questionNum]]
		wrong = list(capitals.values())
		del wrong[wrong.index(correctAnswer)]
		wrong = random.sample(wrong, 3)
		answerOptions = wrong + [correctAnswer]
		random.shuffle(answerOptions)
		test.write('%s. What is the capital of %s\n' % (questionNum +1, states[questionNum]))
		for i in range(4):
			test.write(' %s. %s\n' % ('ABCD' [i], answerOptions[i]))
		test.write('\n')
		ans.write(' %s. %s\n' %(questionNum + 1, 'ABCD' [answerOptions.index(correctAnswer)]))
	test.close()
	ans.close()