# encoding=utf-8
#! python3
# randomQuizGenerator.py Create quizzes with questions and answers in random order,
# along with the answer key.
import random
# The quiz data,keys are provinces and values are their capitals.
capitals={'福建':'福州','北京':'北京','浙江':'杭州','上海':'上海','江苏':'南京','安徽':'合肥',
'江西':'南昌','广东':'广州','广西':'南宁','云南':'昆明','海南':'海口','西藏':'拉萨'
,'新疆':'乌鲁木齐','宁夏':'银川','湖南':'长沙','湖北':'武汉','重庆':'重庆','内蒙古':'呼和浩特',
'陕西':'西安','山西':'太原','河南':'郑州','贵州':'贵阳','甘肃':'兰州','青海':'西宁','四川':'成都',
'山东':'济南','河北':'石家庄','吉林':'长春','辽宁':'沈阳','台湾':'台北'
}
print('总题目数：'+str(len(capitals.keys())))

#Generate 35 quiz files.
for quizNum in range(35):
    #TODO:Create the quiz and answer key files.
    quizFile=open('capitalsquiz%s.txt'%(quizNum+1),'w')
    answerFile=open('capitalsquiz_answers%s.txt'%(quizNum+1),'w')
    #TODO:Write out the header for the quiz.
    quizFile.write('姓名:\n\n日期:\n\n分数等级:\n\n')
    quizFile.write((' '*20)+'中国省会试题 (卷 %s)'%(quizNum+1))
    quizFile.write('\n\n')
    #TODO:Shuffle the order of the provinces.
    provinces=list(capitals.keys())
    random.shuffle(provinces)
    #TODO:Loop through all provinces,making a questions for each.
    for questionNum in range(len(provinces)):
        #Get right and wrong answers.
        correctAnswer=capitals[provinces[questionNum]]
        wrongAnswers=list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers=random.sample(wrongAnswers,3)
        answerOptions=wrongAnswers+[correctAnswer]
        random.shuffle(answerOptions)
        #Write the question and answer options to the quiz file.
        quizFile.write('%s.%s的省会是哪座城市？\n'%(questionNum+1,provinces[questionNum]))
        for i in range(4):
            quizFile.write('%s. %s\n'%('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')
        #Write the answer key to a file.
        answerFile.write('%s. %s\n'%(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()
print('出卷完成')