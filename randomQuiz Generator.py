import random
# the quiz data. Keys are states and values are their capitals
capitals={'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix',
            'Arkansas':'Little Rock','California':'Sacramento','Colorado':'Denver',
            'Connecticut':'Hartford','Delaware':'Dover','Florida':'Tallahassee'}
#generate 35 quiz files
for quizNum in range(35):
    quizFile=open('capitalsquiz%s.txt'%(quizNum+1),'w')
    answerKeyFile=open('capitalsquiz_answers%s.txt'%(quizNum+1),'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((''*20)+'State Capitals Quiz (Form %s)'%(quizNum+1))
    quizFile.write('\n\n')
    states=list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(9):
        correctAnswer=capitals[states[questionNum]]
        wrongAnswers=list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers=random.sample(wrongAnswers,3)
        answerOptions=wrongAnswers+[correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write('%s.what is the capital of %s?\n'%(questionNum+1,states[questionNum]))
        for i in range(4):
            quizFile.write('%s.%s\n'%('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')
        answerKeyFile.write('%s.%s\n'%(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()
